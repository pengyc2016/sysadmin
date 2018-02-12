# coding:utf-8
import paramiko
# import os


def command(ip, pwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip, username='root', password=pwd)
    except:
        ssh.connect(hostname=ip, username='root', password="pengyc")
    stdin, stdout, stderr = ssh.exec_command('mkdir /soft;mount -t cifs  //22.188.62.20/soft /soft  -o username=samba,'
                                             'password=samba; ')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    with open('/tmp/out.txt', 'w+') as f:
        f.write(stdout.read())
    stdin, stdout, stderr = ssh.exec_command('umount /soft')
    ssh.close()

