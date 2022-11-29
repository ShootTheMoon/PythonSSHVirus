import PySimpleGUI as sg
import paramiko as pk
import getpass as gp
import time
import asyncio
import threading


client = pk.SSHClient()

def checkIfAlive():
    try:
        transport = client.get_transport()
        transport.send_ignore()
        return True
    except EOFError:
        return False

def directoryHandler(stdin,stdout,stderr):
    cmd_output = stdout.read().decode()
    splitList = cmd_output.split("\n")
    return splitList[:-1]

def OpenCommand(host,user,password):
        try:
            client.set_missing_host_key_policy(pk.AutoAddPolicy())
            client.connect(hostname=host, username=user,password=password)
        except Exception as err:
            print(err)
        directory = ''
        (stdin,stdout,stderr) = client.exec_command("ls -d -- */")
        files = directoryHandler(stdin,stdout,stderr)
        stdin.close()
        stderr.close()
        stdout.close()
        layout1 = [
        [sg.Text('Path: ' + directory,key='workingDir')],
        [sg.Button('Back',),sg.Button('Go',),sg.Button('Print',)],
        [sg.Listbox(values=files,size=(90,10), select_mode="single", key="folders")],
        [sg.Multiline('',key='Output',size=(90,10),disabled=True)],
        [sg.Text('Command',),sg.InputText('',key='Command',size=(75,45)),sg.Button('Run',)],
        [sg.Text('Status: Online',key='Status')],
        [sg.Button('Reconnect',),sg.Button('Disconnect',),sg.Button('Check Connection',)],
        ]

        windowCommand = sg.Window('Command',layout=layout1,size=(850,650),element_justification='c')
        
        while True:
            event, values = windowCommand.read()
            if event == sg.WIN_CLOSED:
                client.close()
                break
            elif event == 'Run':
                command = values['Command']
                (stdin,stdout,stderr) =client.exec_command(command)
                cmd_output = stdout.read().decode()
                cmd_err = stderr.read().decode()
                if(cmd_err):
                    windowCommand['Output'].update(cmd_err)
                else:
                    windowCommand['Output'].update(cmd_output)
                stdin.close()
                stderr.close()
                stdout.close()
            elif event == 'Disconnect':
                client.close()
                windowCommand['Status'].update('Status: Offline')
            elif event == 'Reconnect':
                client.set_missing_host_key_policy(pk.AutoAddPolicy())
                client.connect(hostname=host, username=user,password=password)
                windowCommand['Status'].update('Status: Online')
            elif event == 'Check Connection':
                if(checkIfAlive()):
                    windowCommand['Status'].update('Status: Online')
                else:
                    windowCommand['Status'].update('Status: Offline')
            elif event == 'Go':
                try:
                    if(directory):
                        (stdin,stdout,stderr) =client.exec_command(f'cd {directory}/{values["folders"][0]}; pwd')
                    else:
                        (stdin,stdout,stderr) =client.exec_command(f'cd {values["folders"][0]}; pwd')
                    cmd_output = stdout.read().decode()
                    cmd_err = stderr.read().decode()
                    if(cmd_err):
                        print("err")
                        windowCommand['Output'].update(cmd_err)
                    else:
                        windowCommand['workingDir'].update(cmd_output)
                        directory = cmd_output.split("\n")[0]
                        (stdin,stdout,stderr) =client.exec_command(f'cd {directory}; ls -a')
                        files = directoryHandler(stdin,stdout,stderr)
                        windowCommand['folders'].update(files)
                        stdin.close()
                        stderr.close()
                        stdout.close()
                except Exception as err:
                    print(err)
                    windowCommand['Output'].update(err)
            elif event == 'Back':
                try:
                    if(directory):
                        (stdin,stdout,stderr) =client.exec_command(f'cd {directory}/..; pwd')
                    else:
                        (stdin,stdout,stderr) =client.exec_command(f'cd ..; pwd')
                    cmd_output = stdout.read().decode()
                    cmd_err = stderr.read().decode()
                    if(cmd_err):
                        print("err")
                        windowCommand['Output'].update(cmd_err)
                    else:
                        windowCommand['workingDir'].update(cmd_output)
                        directory = cmd_output.split("\n")[0]
                        (stdin,stdout,stderr) =client.exec_command(f'cd {directory}; ls -a')
                        files = directoryHandler(stdin,stdout,stderr)
                        windowCommand['folders'].update(files)
                        stdin.close()
                        stderr.close()
                        stdout.close()
                except Exception as err:
                    print(err)
                    windowCommand['Output'].update(err)
            elif event == 'Print':
                try:
                    if(directory):
                        (stdin,stdout,stderr) =client.exec_command(f'cat {directory}/{values["folders"][0]}; pwd')
                    else:
                        (stdin,stdout,stderr) =client.exec_command(f'cat {values["folders"][0]}; pwd')
                    cmd_output = stdout.read().decode()
                    cmd_err = stderr.read().decode()
                    if(cmd_err):
                        windowCommand['Output'].update(cmd_err)
                    else:
                        windowCommand['Output'].update(cmd_output)
                    stdin.close()
                    stderr.close()
                    stdout.close()
                except Exception as err:
                    print(err)
                    windowCommand['Output'].update(err)

def StartConnect():
    layout = [
        [sg.Text('Host',key='HostLabel')],
        [sg.InputText(key='Host')],
        [sg.Text('User',key='UserLabel')],
        [sg.InputText(key='User')],
        [sg.Text('Password',key='TextLabel')],
        [sg.InputText(key='Password', password_char='*')],
        [sg.Button('Connect',),sg.Button('Exit')],
        [sg.Text('',key='Err',text_color= 'red')],
    ]

    windowConnect = sg.Window('Connect',layout=layout,size=(260,250),element_justification='c')

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
                
                try:
                    client.set_missing_host_key_policy(pk.AutoAddPolicy())
                    client.connect(hostname=host, username=user,password=password)
                except Exception as err:
                    windowConnect['Err'].update(err)
                else:
                    OpenCommand(host,user,password)


def main():
    StartConnect()


if __name__ == "__main__":
    main()