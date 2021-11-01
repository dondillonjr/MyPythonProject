from typing import List
import paramiko
import time
import platform
import os.path


class Commands:
    commands = []

    def read_file(self) -> list:
        os_type = platform.system()
        if os_type == "Windows":
            filename = "c:/temp/cmd.txt"
        else:
            filename = '/temp/cmd.txt'

        if os.path.isfile(filename):
            with open(filename, "r") as file:
                for line in file:
                    self.commands.append(line)
        else:
            print(f"file {filename} does not exist")
            exit(1)

        return self.commands

    def get_cmds(self) -> list:
        return self.read_file()


class Connect:
    port = 22

    def __init__(self, host, uname):
        self.host = host
        self.uname = uname
        self.cmd = []

    def get_commands(self):
        c = Commands()
        self.cmd = c.get_cmds()

    def run_commands(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"\n{'#' * 50}\nConnecting to Host {self.host} \n{'#' * 50}")
        ssh.connect(self.host, self.port, self.uname)
        DEVICE_ACCESS = ssh.invoke_shell()

        for command in self.cmd:
            DEVICE_ACCESS.send(f'{command}\n')
            time.sleep(2)
            output = DEVICE_ACCESS.recv(65000)
            print
            print(output.decode(), end=' ')

        ssh.close()


################## MAIN #################
cnn = Connect("3.22.234.128", "ubuntu")
cnn.get_commands()
cnn.run_commands()
print()
print()
cnn = Connect("18.216.119.62", "ec2-user")
cnn.get_commands()
cnn.run_commands()