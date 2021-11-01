import paramiko
import time

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
#host = "ec2-3-21-35-235.us-east-2.compute.amazonaws.com"
host = "3.22.234.128"
port = 22
username = "ubuntu"
password = ""
command = 'java -jar /home/ubuntu/java_programs/GiveCreatureLifeLinux.jar'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
time.sleep(5)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print()
print(lines)
print()
stdin, stdout, stderr = ssh.exec_command("pwd")
lines = stdout.readlines()

print(lines)
print()
stdin, stdout, stderr = ssh.exec_command("date")
lines = stdout.readlines()
print(lines)
ssh.close