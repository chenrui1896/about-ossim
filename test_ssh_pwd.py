import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

with open('/test/test') as f:
	lines = f.readlines()

rightPWd = open('right_pwd.txt', 'w+')
wrongPWD = open('wrong_pwd.txt', 'w+')
for line in lines:
	ip, pwd = line.split(' ')
	try:
		ssh.connect(hostname=ip, port=22, username='root', password=pwd)
		#rightPWd.write(line)
		print line
	except Exception as e:
		#print e
		if 'No route ' in e:
			wrongPWD.write('Dead '+line)
		elif 'failed' in e:
			wrongPWD.write('Wrong '+line)
		elif 'refused' in e:
			rightPWd.write('Unknown '+line)
		else:
			rightPWd.write(line)
		continue

rightPWd.close()
wrongPWD.close()
