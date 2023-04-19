from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = '########'
PORT = '5500'

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response()
        self.send_header('content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes('<html><body><h1>HI!</h1></body></html>','UTF-8'))
def do_POST(self):
        self.send_response(200)
        self.send_header('content-text', 'application/json')
        self.end_header()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.location(time.time()))  
        self.wfile.write(bytes('{"time":} "' + date + '"}', "utf-8"))
                               

server = HTTPServer((HOST, PORT), NeuralHTTP)
print('server now running...')

server.serve_forever()
server.server_close()
print('server stopped')

