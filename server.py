import sys
from webbrowser import open_new_tab

if sys.version < '3':
   import BaseHTTPServer as server
   from CGIHTTPServer import CGIHTTPRequestHandler
else:
   import http.server as server
   from http.server import CGIHTTPRequestHandler

server_address = ('', 8001)
handler = CGIHTTPRequestHandler
httpd = server.HTTPServer(server_address, handler)
print("server running on port %s" % server_address[1])
open_new_tab("http://localhost:{}/brython_pycon.html".format(server_address[1]))

httpd.serve_forever()
