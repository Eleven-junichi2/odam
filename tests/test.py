from src.main import rename_files_with_auto_num
from pathlib import Path

script_dir = Path(__file__).absolute().parent
dir_for_test_path = script_dir / "dir_for_test_file_io"
if not dir_for_test_path.exists():
    dir_for_test_path.mkdir()


def test_rename_files_with_auto_num():
    for i in range(3):
        with open(dir_for_test_path / f"test{i}.txt", "w"):
            pass
    rename_files_with_auto_num(
        dir_for_test_path, prefix_style="number", separater="-")
    file_path_list = list(
        [path_ for path_ in dir_for_test_path.iterdir() if path_.is_file()])
    for number, file_path in enumerate(file_path_list):
        assert file_path.name == f"{number}-test{number}.txt"
        file_path.unlink()
