import PySimpleGUI as sg
from pathlib import Path


def main():
    sg.theme("DarkBlack1")
    layout = [
        [sg.Text(
            "Select the directory contains files you want to auto-number:")],
        [sg.Input(key="path_to_auto-number"), sg.FolderBrowse()],
        [sg.Text("Style of number:")],
        [sg.Radio("1, 2, 3...", "prefix_style",
                  key="number_prefix", default=True),
         sg.Radio("a, b, c...", "prefix_style",
                  key="alphabet_prefix", disabled=True)],
        [sg.Checkbox(
            "Separate prefix and filename with space",
            key="separate_with_space", default=True)],
        [sg.Button("Ok")]]
    window = sg.Window("Odam", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        print(values)
        dir_path = Path(values["path_to_auto-number"])
        # use_number_as_prefix = values["number_prefix"]
        # use_alphabet_as_prefix = values["alphabet_prefix"]
        use_space_as_separetor = values["separate_with_space"]
        # if use_number_as_prefix:
        # prefix_style = "number"
        if use_space_as_separetor:
            separater = " "
        else:
            separater = ""

        file_path_list = list(
            [path_ for path_ in dir_path.iterdir() if path_.is_file()])
        print(file_path_list)
        for number, file_path in enumerate(file_path_list):
            prefix = number
            file_path.rename(file_path.parent.joinpath(
                f"{prefix}{separater}{file_path.name}"))
    window.close()


if __name__ == "__main__":
    main()
