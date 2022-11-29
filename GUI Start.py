import PySimpleGUI as sg
import paramiko as pk
import getpass as gp
import time

def OpenCommand(client,host,user,password):
    
        client = pk.SSHClient()
        client.set_missing_host_key_policy(pk.AutoAddPolicy())
        client.connect(hostname=host, username=user,password=password)
    
        layout1 = [
        [sg.InputText('Command',key='Command',size=(75,45)),sg.Button('Run',)],
        [sg.Multiline('',key='Output',size=(90,30),disabled=True)],
        [sg.Text('Status: Online',key='Status')],
        [sg.Button('Reconnect',),sg.Button('Disconnect',)],
        ]

        windowCommand = sg.Window('Command',layout=layout1,size=(600,600),element_justification='c')
        
        while True:
            event, values =windowCommand.read()
            if event == sg.WIN_CLOSED:
                client.close()
                break
            elif event == 'Run':
                command= values['Command']
                (stdin,stdout,stderr) =client.exec_command(command)
                cmd_out=stdout.read()
                windowCommand['Output'].update(cmd_out)
            elif event == 'Disconnect':
                client.close()
                windowCommand['Status'].update('Status: Offline')
            elif event == 'Reconnect':
                client = pk.SSHClient()
                client.set_missing_host_key_policy(pk.AutoAddPolicy())
                client.connect(hostname=host, username=user,password=password)
                windowCommand['Status'].update('Status: Online')
        
def StartConnect():
    layout = [
        [sg.InputText('Host',key='Host')],
        [sg.InputText('User',key='User')],
        [sg.InputText('Password',key='Password')],
        [sg.Button('Connect',),sg.Button('Exit')],
        [sg.Text('',key='Err')],
    ]

    windowConnect = sg.Window('Connect',layout=layout,size=(260,130),element_justification='c')

    while True:
        event, values =windowConnect.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Exit':
            break
        elif event=='Connect':
                host = values['Host']
                user = values['User']
                password = values['Password']
                
                err=''
                
                try:
                    client = pk.SSHClient()
                    client.set_missing_host_key_policy(pk.AutoAddPolicy())
                    client.connect(hostname=host, username=user,password=password)
                except Exception as err:
                    windowConnect['Err'].update(err)

               
                if err == '':
                    OpenCommand(client,host,user,password)
               


StartConnect()
