# Practicing Pathlib:
from pathlib import Path
path = Path("emails")
print(path.exists())
path.mkdir(exist_ok=True)
print(path.absolute())
print(path.as_posix())
for item in path.iterdir():
    print(item)
for item in path.glob("*"):
    print(item)
print(path.is_dir())
print(path.name)
print(path.parent)
print(path.stem)
print(path.suffix)