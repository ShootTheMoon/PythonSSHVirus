import PySimpleGUI as sg

def OpenCommand():
        layout1 = [
        [sg.InputText('Command',key='Command',size=(75,45)),sg.Button('Run',)],
        [sg.Multiline('Output',key='Output',size=(90,30),disabled=True)],
        [sg.Text('Status: Online',key='Status')],
        [sg.Button('Reconnect',),sg.Button('Disconnect',)],
        ]

        windowCommand = sg.Window('Command',layout=layout1,size=(600,600),element_justification='c')
        
        while True:
            event, values =windowCommand.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Disconnect':
                windowCommand['Status'].update('Status: Offline')
            elif event == 'Reconnect':
                windowCommand['Status'].update('Status: Online')
        
def StartConnect():
    layout = [
        [sg.InputText('IP',key='ip')],
        [sg.InputText('User',key='User')],
        [sg.InputText('Password',key='Password')],
        [sg.Button('Connect',),sg.Button('Exit')],
    ]

    windowConnect = sg.Window('Connect',layout=layout,size=(260,130),element_justification='c')

    while True:
        event, values =windowConnect.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Exit':
            break
        elif event=='Connect':
                OpenCommand()


StartConnect()
