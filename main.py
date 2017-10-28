import time
from os import path, curdir, sep
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import middleware
from config import SERVER_NAME, HOST, PORT

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

if __name__ == '__main__':
	server = HTTPServer((HOST, PORT), ServerHandler)
	print time.asctime(), "Server Starts - %s:%s" % (HOST, PORT)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		server.server_close()
		print time.asctime(), "Server Stops - %s:%s" % (HOST, PORT)