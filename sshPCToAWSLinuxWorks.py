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

host = "ec2-18-216-119-62.us-east-2.compute.amazonaws.com"
#host = "3.143.68.154"

port = 22
username = "ec2-user"
command = 'java -jar /home/ec2-user/java_programs/GiveCreatureLifeLinux.jar'
cmd = [ command,"top -b -n1 | head -3 | tail -1",  "df -k /home | tail -1", "pwd", "date"]

def ssh_conn():
    ssh = paramiko.SSHClient()

    #ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #key_file = paramiko.RSAKey.from_private_key_file("/home/ubuntu/.ssh/id_rsa")
    
    ssh.connect(host, port, username)
    #sh.connect(host, port, username, pkey=key_file)
    time.sleep(5)
    print(f"\n{'#'*50}\nConnecting to Host {host} \n{'#'*50}")

    for i in cmd:
        stdin, stdout, stderr = ssh.exec_command( i )
        print(stdout.read().decode())
        print("\n")
        time.sleep(8)

    ssh.close()

############### MAIN ##############
ssh_conn()
