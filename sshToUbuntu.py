import subprocess
import sys

############# LINUX to UBUNTU
#HOST = "ubuntu@ec2-3-21-35-235.us-east-2.compute.amazonaws.com"
HOST = "ubuntu@3.22.234.128"
results = []

# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND='java -jar /home/ubuntu/java_programs/GiveCreatureLifeLinux.jar'

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

results = ssh.stdout.readlines()

if results == []:
    error = ssh.stderr.readlines()
    print(sys.stderr, "ERROR: %s" % error )
else:
    for i in results:
       print( i.strip())
