import paramiko
import time

class Commands:
    commands = ["df -k", "ls -ltr", "df -k"]

    #def get_cmds_(self)->[]:
    def get_cmds_(self)->commands:
        return self.commands

class Connect:
    port = 22

    def __init__(self, host, uname):
        self.host = host
        self.uname = uname
        self.cmd = []

    def get_commands(self):
        c = Commands()
        self.cmd = c.get_cmds_()

    def run_commands(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"\n{'#'*50}\nConnecting to Host {self.host} \n{'#'*50}")
        ssh.connect(self.host, self.port, self.uname)

        DEVICE_ACCESS = ssh.invoke_shell()

        for command in self.cmd:
            DEVICE_ACCESS.send(f'{command}\n')
            time.sleep(2)
            output = DEVICE_ACCESS.recv(65000)
            print
            print (output.decode(),end=' ')

        ssh.close()

cnn = Connect( "18.216.119.62" , "ec2-user")
cnn.get_commands()
cnn.run_commands()