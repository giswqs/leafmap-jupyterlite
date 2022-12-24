"""This script copies all notebooks from the leafmap repo and replaces the leafmap installation instructions with JupyterLite instructions.
"""


import glob
import os
import shutil
import leafmap

url = 'https://github.com/giswqs/leafmap/archive/refs/heads/master.zip'
out_zip = 'leafmap-master.zip'
leafmap.download_file(url, out_zip)

in_dir = 'leafmap-master/docs'
out_dir = 'content'
notebook_dir = os.path.abspath(os.path.join(out_dir, 'notebooks'))
workshop_dir = os.path.abspath(os.path.join(out_dir, 'workshops'))

shutil.copytree(in_dir + '/notebooks', out_dir + '/notebooks', dirs_exist_ok=True)
shutil.copytree(in_dir + '/workshops', out_dir + '/workshops', dirs_exist_ok=True)
shutil.copytree(in_dir + '/data', out_dir + '/data', dirs_exist_ok=True)

cwd = os.getcwd()

os.chdir(notebook_dir)
cmd = "jupytext --to myst *.ipynb"
os.system(cmd)

os.chdir(workshop_dir)
cmd = "jupytext --to myst *.ipynb"
os.system(cmd)

os.chdir(cwd)


notebooks = glob.glob(out_dir + '/notebooks/*.md')
workshops = glob.glob(out_dir + '/workshops/*.md')

files = notebooks + workshops

for file in files:
    with open(file, 'r') as f:
        lines = f.readlines()

    out_lines = []
    for index, line in enumerate(lines):
        if line.strip() == '# !pip install leafmap' or line.strip() == '# !pip install -U leafmap':
            out_lines.append('%pip install -q leafmap\n')
        elif (
            line.strip()
            == 'Uncomment the following line to install [leafmap](https://leafmap.org) if needed.'
        ):
            pass
        elif 'colab-badge.svg' in line and 'jupyterlite' not in lines[index-1]:
            badge = (
                '[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)]'
            )
            baseurl = 'https://demo.leafmap.org/lab/index.html?path='
            base_dir = os.path.basename(os.path.dirname(file))
            basename = os.path.basename(file).replace('.md', '.ipynb')
            url = baseurl + base_dir + '/' + basename
            badge_url = f"{badge}({url})\n"
            out_lines.append(badge_url)
            out_lines.append(line)
        elif ':id:' in line:
            pass
        elif line.strip() == '# leafmap.update_package()':
            pass
        elif line.strip() == '# !pip install geopandas':
            out_lines.append('import piplite\n')
            out_lines.append(
                "await piplite.install(['geopandas', 'shapely', 'pyproj'], deps=False)\n"
            )
        elif "display_name" in line:
            out_lines.append("  display_name: Python (Pyodide)\n")
        elif 'name: python3' in line:
            out_lines.append('  name: python\n')
        else:
            out_lines.append(line)

    with open(file, 'w') as f:
        f.writelines(out_lines)


os.chdir(notebook_dir)
cmd = "jupytext --to ipynb *.md"
os.system(cmd)

os.chdir(workshop_dir)
cmd = "jupytext --to ipynb *.md"
os.system(cmd)

os.chdir(cwd)

for file in files:
    os.remove(file)

files = [file.replace('.md', '.ipynb') for file in files]

for file in files:
    with open(file, 'r') as f:
        lines = f.readlines()

    out_lines = []
    for index, line in enumerate(lines):
        if '"id":' in line:
            pass
        else:
            out_lines.append(line)

    with open(file, 'w') as f:
        f.writelines(out_lines)

shutil.rmtree('leafmap-master')
os.remove('leafmap-master.zip')

# extra = {
# "cell_type": "code",
# "execution_count": None,
# "metadata": {},
# "outputs": [],
# "source": [
#     "import piplite\n",
#     "await piplite.install('leafmap-lite')\n",
#     "await piplite.install(['leafmap', 'geopandas', 'shapely', 'pyproj'], deps=False)",
# ]
# },
# for nb in notebooks:
#     with open(nb, 'r') as f:
#         data = json.load(f)
#         cells = data['cells']
#         print(len(cells))
#         new_cells = []
#         added = False
#         for cell in cells:
#             if cell['cell_type'] == 'code':
#                 if not added:
#                     new_cells.append(extra)
#                     added = True
#                 new_cells.append(cell)
#             else:
#                 new_cells.append(cell)

#         data['cells'] = new_cells

#     print(len(data['cells']))
#     out_nb = os.path.join(out_dir, "notebooks", os.path.basename(nb))
#     # print(data)
#     with open(out_nb, 'w') as f:
#         json.dump(data, f)
