import PySimpleGUI as sg


def main():
    sg.theme("DarkBlack1")
    layout = [[sg.Text('Some text on Row 1')],
              [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]
    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        print('You entered ', values[0])

    window.close()


if __name__ == "__main__":
    main()
