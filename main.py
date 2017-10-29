import cgi
import time
import json
import middleware
from os import path, curdir, sep
from repository import repoValidation
from config import SERVER_NAME, HOST, PORT
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

middlewareHandle = middleware.security.Authorize()

class ServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.server_version = SERVER_NAME
		if self.path == '/':
			self.path = '/index.html'
			extension = path.splitext(self.path)[-1]
			mimeTypes = middlewareHandle.authMimeTypes(extension)
			try:
				if mimeTypes['status']:
					file = open(curdir + sep + self.path, 'rb')
					self.send_response(200)
					self.send_header('Content-type', mimeTypes['mimeTypes'])
					self.end_headers()
					self.wfile.write(file.read())
					file.close()
				return
			except IOError:
				self.send_error(404, "File Not Found %s" % self.path)
				return

		elif self.path == '/favicon.ico':
			extension = path.splitext(self.path)[-1]
			mimeTypes = middlewareHandle.authMimeTypes(extension)
			try:
				if mimeTypes['status']:
					file = open(curdir + sep + self.path, 'rb')
					self.send_response(200)
					self.send_header('Content-type', mimeTypes['mimeTypes'])
					self.end_headers()
					self.wfile.write(file.read())
					file.close()
				return
			except IOError:
				self.send_error(404, "File Not Found %s" % self.path)
				return

	def do_POST(self):
		self.server_version = SERVER_NAME
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
		if ctype == 'multipart/form-data':
			postVars = cgi.parse_multipart(self.rfile, pdict)
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers.getheader('content-length'))
			postVars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
		elif ctype == 'application/json':
			length = int(self.headers.getheader('content-length', 0))
			postVars = json.loads(self.rfile.read(length))
		else:
			postVars = {}
		
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		repoHandler = repoValidation(postVars)
		if repoHandler.is_valid_hook() == False:
			self.wfile.write(repoHandler.error())
			return
		self.wfile.write(repoHandler.success())
		return

if __name__ == '__main__':
	server = HTTPServer((HOST, PORT), ServerHandler)
	print time.asctime(), "Server Starts - %s:%s" % (HOST, PORT)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		server.server_close()
		print time.asctime(), "Server Stops - %s:%s" % (HOST, PORT)