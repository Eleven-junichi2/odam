import PySimpleGUI as sg


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
        print('You entered ', values[0])
        print('You entered ', values[1])
        print('You entered ', values[2])
    window.close()


if __name__ == "__main__":
    main()
