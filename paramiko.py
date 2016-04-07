
def stock(code_store):
	products = productModel().all()
	try:
		path_pem = "file.pem"
		response = urllib2.urlopen('https://s3.amazonaws.com/%s' % path_pem)
	    data = response.read()
	    keyfile = StringIO.StringIO(data)
	    mykey = paramiko.RSAKey.from_private_key(keyfile)
	    ssh = paramiko.SSHClient()
	    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	    ssh.connect('ec2-54-00-00-000.compute-1.amazonaws.com', username='ubuntu', pkey=mykey)
	    stc_count = 0
	    for x in products:
	        code = str(code_store) + str(x.idSTC)
	        comando = 'grep "' + str(code) + '" SERIEINV.TXT'
	        stdin, stdout, stderr = ssh.exec_command(str(comando))
	        try:
	            result = stdout.read()
	            val = result.split()
	            for cad in val:
	                callvalstock = cad.endswith("M")
	                if callvalstock:
	                    stock = sub("\D", "", cad)
	                    stc_count += int(stock)
	        except:
	            stc_count = stc_count
	            pass
	    ssh.close()
	except Exception, e:
		print e