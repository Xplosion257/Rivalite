import re
import subprocess
import rivalite

pattern = r".+?\(.*?\)"
group_finder = r".+?\((.*?)\)"

modules = rivalite.about()
docs = []
for module in modules:
    docs.append(rivalite.about(module))

functions = []
for doc in docs:
    _functions = re.findall(pattern, doc)
    for _function in _functions:
        functions.append(_function)

for function in functions:
    match = re.match(group_finder, function)
    if match is None:
        continue
    args = match.group(1).split(", ")
    if all("=" in arg for arg in args) or len(args) == 1 and args[0] == "":
        print(subprocess.run(f"""python3 << "EOF"
        import rivalite
        print(rivalite.{function}())
        EOF
        """, shell=True, text=True, capture_output=True).stdout)
