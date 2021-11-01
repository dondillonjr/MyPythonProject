import paramiko
import time
############# LINUX TO UBUNTU
# Call paramiko.SSHClient() to create a new SSHClient.
# Call paramiko.SSHClient.set_missing_host_key_policy(policy)
# with policy as paramiko.AutoAddPolicy() to allow the
# Python script to SSH to a remote server with unknown SSH keys.
#
# Call paramiko.SSHClient.connect(host, port, username, password)
# to connect the client to the server host:port with the credentials username and password.
#
# Call paramiko.SSHClient.exec_command(command) to execute the command on the
# remote server and return a 3-tuple containing the stdin, stdout, and stderr from the server.
#
# Call paramiko.channel.ChannelFile.readlines() with paramiko.channel.ChannelFile as
# stdout to return the output from the command.
host = "3.22.234.128"
#host = 'ec2-3-21-35-235.us-east-2.compute.amazonaws.com'
port = 22
username = "ubuntu"
password = ""
javaExe = 'java -jar /home/ubuntu/java_programs/GiveCreatureLifeLinux.jar'
commands1 = [ javaExe, "top -b -n1 | head -3 | tail -1", "df -k /home | tail -1", "pwd", "date"]
commands2 = [ "ls -ltr", "uname -a" ]

def ssh_conn( host, commands):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    print(f"\n{'#'*50}\nConnecting to Host {host} \n{'#'*50}")

    for i in commands:
        stdin, stdout, stderr = ssh.exec_command(i)
        print(stdout.read().decode())
        print("\n")
        time.sleep(8)

    ssh.close()
############## MAIN ######
ssh_conn( host, commands1 )
ssh_conn( host, commands2 )
