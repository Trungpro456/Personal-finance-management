# Python 3 server
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("Open your browser and go to http://localhost:8000/tro-ly-tai-chinh-final.html")
    httpd.serve_forever()
