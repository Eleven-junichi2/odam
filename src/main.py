import PySimpleGUI as sg
from pathlib import Path


def main():
    sg.theme("DarkBlack1")
    layout = [
        [sg.Text(
            "Select the directory contains files you want to auto-number:")],
        [sg.Input(), sg.FolderBrowse()],
        [sg.Text("Style of number:")],
        [sg.Radio("1, 2, 3...", "prefix_style", default=True),
         sg.Radio("a, b, c...", "prefix_style")],
        [sg.Checkbox(
            "Separate prefix and filename with space", default=True)],
        [sg.Button("Ok")]]
    window = sg.Window("Odam", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        dir_path = Path(values[0])
        file_path_list = list(
            [path_ for path_ in dir_path.iterdir() if path_.is_file()])
        print(file_path_list)
        for number, file_path in enumerate(file_path_list):
            print(file_path)
            file_path.rename(file_path.parent.joinpath(
                f"{number} {file_path.name}"))
        print('You entered ', values[0])
        print('You entered ', values[1])
        print('You entered ', values[2])
    window.close()


if __name__ == "__main__":
    main()
