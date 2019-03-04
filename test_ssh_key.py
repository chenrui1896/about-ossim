import paramiko
  
private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/smysec')
  

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open('/test/test.txt') as f:
	lines = f.readlines()

installed = open('installed.txt', 'w+')
not_installed = open('not_installed.txt', 'w+')
for line in lines:
	ip= line.strip()
	try:
		ssh.connect(hostname=ip, port=22, username='root', pkey=private_key)
		stdin, stdout, stderr = ssh.exec_command('whoami')

		result = stdout.read()

  		if result:
  			installed.write(ip + result)

		ssh.close()
	except Exception as e:
		print e

installed.close()
not_installed.close()
