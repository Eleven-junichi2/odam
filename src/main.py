import PySimpleGUI as sg
from pathlib import Path
import sys
import os

script_dir = Path(__file__).absolute().parent
assets_dir_name = "assets"
assets_dir = script_dir / assets_dir_name

def asset_path(asset_file_name):
    if hasattr(sys, '_MEIPASS'):
        print(f"meipass: {sys._MEIPASS}")
        return os.path.join(sys._MEIPASS, asset_file_name)
    return assets_dir / asset_file_name


def rename_files_with_auto_num(
        dir_path: Path, prefix_style="number", separater=""):
    file_path_list = list(
        [path_ for path_ in dir_path.iterdir() if path_.is_file()])
    for number, file_path in enumerate(file_path_list):
        if prefix_style == "number":
            prefix = number
        else:
            raise ValueError("That prefix style is unavaliable.")
        file_path.rename(file_path.parent.joinpath(
            f"{prefix}{separater}{file_path.name}"))


def main():
    sg.theme("DarkBlack1")
    layout = [
        [sg.Text(
            "Select the directory contains files you want to auto-number:")],
        [sg.Input(key="path_to_auto-number", readonly=True),
         sg.FolderBrowse()],
        [sg.Text("Style of number:")],
        [sg.Radio("1, 2, 3...", "prefix_style",
                  key="number_prefix", default=True),
         sg.Radio("a, b, c...", "prefix_style",
                  key="alphabet_prefix", disabled=True)],
        [sg.Checkbox(
            "Separate prefix and filename with space",
            key="separate_with_space", default=True)],
        [sg.Button("Ok")]
    ]
    icon_path = asset_path("icon.ico")
    window = sg.Window("Odam", layout, icon=icon_path)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if values["path_to_auto-number"] == "":
            sg.popup_ok("Please select the directory.")
            continue
        else:
            dir_path = Path(values["path_to_auto-number"])
        use_number_as_prefix = values["number_prefix"]
        use_alphabet_as_prefix = values["alphabet_prefix"]
        use_space_as_separetor = values["separate_with_space"]
        if use_number_as_prefix:
            prefix_style = "number"
        elif use_alphabet_as_prefix:
            prefix_style = "alphabet"
        else:
            raise ValueError("Please select style of number")
        if use_space_as_separetor:
            separater = " "
        else:
            separater = ""
        try:
            rename_files_with_auto_num(dir_path, prefix_style, separater)
        except Exception as e:
            sg.popup_error(e)
            raise(e)
        else:
            sg.popup_ok("The files was successfully renamed.")
    window.close()


if __name__ == "__main__":
    main()
