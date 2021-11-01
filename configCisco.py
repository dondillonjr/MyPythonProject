import paramiko
import time
############# Linux to Cisco Router
host = "3.138.187.74"
port = 22
username = "ubuntu"

commands1 = [ "term length 0\n",
              "show ip int brief\n",
              "config t\n",
              "int lo0\n",
              "no shutdown\n"]

commands2 = [  "show ip int brief",
               "config t",
               "ip address 1.1.1.1 255.255.255.0",
               "no shutdown",
               "int loopback1",
               "ip address 5.5.5.5 255.255.255.0",
               "no shut",
               "do sh ip int brief",
               "exit" ]

commands3 = [ "show run int lo0",
              "show run int lo1" ]

def cisco_exec( host, commands):
    try:
        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, port, username)

        print(f"\n{'#'*50}\nConnecting to Host {host} \n{'#'*50}")

        for cmd in commands:
            DEVICE_ACCESS.send(f'{cmd}\n')
            time.sleep(5)
            output = DEVICE_ACCESS.recv(65000)
            print(output.decode(), end=' ')

        ssh.close()

    except:
        print(Unable to connect to Device")

############## MAIN ######
cisco_exec( host, commands1 )
cisco_exec( host, commands2 )
cisco_exec( host, commands3 )
