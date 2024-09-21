import os 


items = os.listdir(".")
paths_to_files = set()

def build_path(item, path_string="."):
    path = path_string + "/" + item
    if os.path.isfile(path):
        paths_to_files.add(path) 
        return
    for item in os.listdir(path):
        build_path(item, path_string=path)

for item in items:
    # ignore hidden  directories
    if item[0] == ".": continue 
    if os.path.isfile(item):
        paths_to_files.add("./"+item)
    else:
        build_path(item)

hyperlinks = []
for path in paths_to_files:
    hyperlinks.append(f'<a href="{path[1:]}">{path[1:]}</a>')

html = f"""
<html>
<head>
    <title>Index</title>
</head>
<body>
    {"<br>".join(hyperlinks)}
</body>
</html>
"""


with open("index.html", "w") as fl:
    fl.write(html)

print("Written to index.html")