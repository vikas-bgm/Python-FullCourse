from pathlib import Path

file_path = Path("data1.txt")

file_path.exists()
file_path.is_file()
file_path.is_dir()
file_path.stat().st_size