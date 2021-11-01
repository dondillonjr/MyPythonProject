import paramiko
import time

############### TO UBUNTU
#host = '3.21.35.235'
host  = 'ec2-3-22-234-128.us-east-2.compute.amazonaws.com'
port  = 22
username = "ubuntu"
java_command = 'java -jar /home/ubuntu/java_programs/GiveCreatureLifeLinux.jar'
commands = [java_command, "df -k", "ls -l"]

def ssh_conn():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"\n{'#' * 50}\nConnecting to Host {host} \n{'#' * 50}")
    ssh.connect(host, port, username)

    DEVICE_ACCESS = ssh.invoke_shell()

    for command in commands:
        DEVICE_ACCESS.send(f'{command}\n')
        time.sleep(2)
        output = DEVICE_ACCESS.recv(65000)
        print (output.decode(), end=' ')
        print("\n")

    ssh.close()

######## MAIN ##########
ssh_conn()
