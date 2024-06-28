import socket

HOST = '127.0.0.1'
PORT = 4321
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
  s.bind((HOST ,4321))
  s.listen(1)
  print("wait for connection...")
  conn , addr = s.accept()
  print('Connect baby:', addr)
  name = socket.gethostname()

  while True:
    command = input(name + ':')
    if command == 'stop':
        conn.send(command.encode())
        conn.close()
        break
        
    
    if command == 'help':
        a = 'dir' + ' ' + '--'  + ' ' + 'содержимое директории'
        b = 'mkdir' + ' ' + '--' + ' ' + 'создание директории в определенном месте'
        c = 'sysinfo' + ' ' + '--'  + ' ' + 'информация о системе'
        d = 'stop'  + ' ' + '--' +  ' ' + 'завершить сессию'
        e = 'download' + ' ' + '--' + ' ' + 'скачать файл из интернета файл'
        f = 'move' + ' ' + '--' + ' ' + 'переместить файл в заданную директорию'
        g = 'upload' + ' ' + '--' + ' ' + 'скачать файл из компьютера клиента'
        h = 'send' + ' ' + '--' + ' ' + 'скачать файл на компьютера клиента с сервера'
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
    
    while command == 'dir':
           cmd_directory = input('dir' + ' ')
           if cmd_directory == 'exit':
               command = input(name + ':') 
           if cmd_directory != 'exit':
               conn.send(command.encode())
               conn.send(cmd_directory.encode())
               ot = conn.recv(1024)
               if ot.decode() == 'yes':  
                 list= conn.recv(1024)
                 print(list.decode())
                 command = 'dir'
               if ot.decode() =='error!':
                 print(ot.decode())
                 command = 'dir'

    if command == 'mkdir':
          cmd_workdirec = input('where?' + ' ')
          cmd_newdirec = input('what?' + ' ')
          conn.send(command.encode())
          conn.send(cmd_workdirec.encode())
          conn.send(cmd_newdirec.encode())
          tdirect = conn.recv(1024)
          tdirect = tdirect.decode()
          print(tdirect.encode())

    if command == 'sysinfo':
           conn.send(command.encode())
           syst = conn.recv(1024)

           ver = conn.recv(2048)
           rel = conn.recv(1024)

           node = conn.recv(1024)

           mach = conn.recv(1024)
          
           proc = conn.recv(1024)
        
           print(syst.decode() , ver.decode() , rel.decode() , node.decode() , proc.decode() , mach.decode())

    if command == 'download':
           conn.send(command.encode())
           url = input('link for download:')  
           dfile = input('downloaded file:')
           wfile = input('where download file:')
           conn.send(url.encode())
           conn.send(dfile.encode())
           conn.send(wfile.encode())

    if command == 'move':
         conn.send(command.encode())
         movefile = input('file to move:')
         wherefile = input('where move:')
         conn.send(movefile.encode())
         conn.send(wherefile.encode())
    
    if command == 'upload':
      conn.send(command.encode())
      filename = input('file for upload:')
      wfile = input('where save uploaded file:')
      conn.send(filename.encode())
      file = open(wfile , 'wb')
      file_data = conn.recv(1024)
      file.write(file_data)
      file.close()

    if command == 'send':
      conn.send(command.encode())
      filename = input('file for send:')
      wfile = input('where save sended file:')
      conn.send(wfile.encode())
      file = open(filename, 'rb')
      file_data = file.read(1024)
      conn.send(file_data)

        
        

       
       

