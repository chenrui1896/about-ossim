import paramiko
  
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/smysec')
  

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open('../installed.txt') as file:
	lines = file.readlines()

for line in lines:
	print 'running %s' % line
	try:
		ip = line.strip()
		ssh.connect(hostname=ip, port=22, username='root', pkey=private_key)
		
		#cmd2 = 'rm -f -r /var/ossec'
		
		stdin, stdout, stderr = ssh.exec_command('/var/ossec/bin/ossec-control restart')
		result = stdout.read()
		print result

		ssh.close()
	except Exception as e:
		print e
