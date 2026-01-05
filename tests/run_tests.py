from pathlib import Path
import os

input("Type enter to continue")

tests_dir = Path(__file__).parent
files = [p.name for p in tests_dir.iterdir() if p.is_file() and p.suffix == ".py" and p.name != "run_tests.py"]
for f in files:
    print(f"=====[{f}]=====")
    os.system(f"python3 \"{f}\"")
    input("Type enter to continue")
