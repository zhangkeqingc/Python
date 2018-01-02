import socket

# Address
HOST = ''
PORT = 8000

# Prepare HTTP response
text_content = '''HTTP/1.x 200 OK 
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</html>
'''

# Read picture, put into HTTP format
f = open('test.jpg', 'rb')
pic_content = '''
HTTP/1.x 200 OK 
Content-Type: image/jpg

'''
# pic_content = pic_content + f.read()
pic_content = pic_content.encode('UTF-8') + f.read()

f.close()

# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# infinite loop, server forever
while True:
    # 3: maximum number of requests waiting
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    method = request.split(' ')[0]
    src = request.split(' ')[1]

    # deal with GET method
    if method == 'GET':
        # ULR
        if src == '/test.jpg':
            content = pic_content
        else:
            content = text_content.encode()

        print('Connected by', addr)
        print('Request is:', request)
        conn.sendall(content)
    # close connection
    conn.close()
ver()


