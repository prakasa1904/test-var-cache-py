import time
import os.path
from os import curdir, sep
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from config import HOST, PORT, MIME_TYPES_PERMITTED, MEMORY_KEY
from cache import Cache
from fetch import PostModel

class ServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):	
		if self.path == '/':
			self.path = '/index.html'
			try:
				extension = os.path.splitext(self.path)[-1]
				mimeTypes = MIME_TYPES_PERMITTED.get(extension)
				isAvailable = mimeTypes is not None
				if isAvailable == True:
					""" LOGING ONLY """
					file = open(self.path)
					self.send_response(200)
					self.send_header('Content-type',mimeTypes)
					self.wfile.write(file.read())
					file.close()
				return
			except IOError:
				self.send_error(404, "File Not Found %s" % self.path)

		elif self.path == '/favicon.ico':
			file = open(self.path)
			self.send_response(200)
			self.send_header('Content-type', "")
			self.wfile.write(file.read())
			file.close()

if __name__ == '__main__':
	server = HTTPServer((HOST, PORT), ServerHandler)
	print time.asctime(), "Server Starts - %s:%s" % (HOST, PORT)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		server.server_close()
		print time.asctime(), "Server Stops - %s:%s" % (HOST, PORT)