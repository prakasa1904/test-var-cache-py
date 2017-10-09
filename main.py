import time
import os.path
from os import curdir, sep
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from config import HOST, PORT, MIME_TYPES_PERMITTED
from cache import KEY
from fetch import PostModel

class ServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		"""Respond to a GET request."""
		if self.path == '/':
			post = PostModel()
			""" Let's Count Our API Peformance """
			post.getPostData()
			""" Let's Count Our API Peformance """
			self.path = '/index.html'
			""" LOGING ONLY """
			print "============ my file access ==========="
			print os.path.splitext(self.path)[0]
			print self.path
			print "============ my file access ==========="

		try:
			extension = os.path.splitext(self.path)[-1]
			mimeTypes = MIME_TYPES_PERMITTED.get(extension)
			isAvailable = mimeTypes is not None
			if isAvailable == True:
				""" LOGING ONLY """
				print "============ my condition ==========="
				print " IS HERE %s" % mimeTypes
				print "============ my condition ==========="
				#file=open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type',mimeTypes)
				#self.wfile.write(file.read())
				self.wfile.write("<html><head><title>Title goes here.</title></head>")
				self.wfile.write("<body><p>This is a test.</p>")
				self.wfile.write("<p>You accessed path: %s</p>" % self.path)
				self.wfile.write("</body></html>")
				#file.close()
			return
		except IOError:
			self.send_error(404, "File Not Found %s" % self.path)

if __name__ == '__main__':
	server = HTTPServer((HOST, PORT), ServerHandler)
	print time.asctime(), "Server Starts - %s:%s" % (HOST, PORT)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		server.server_close()
		print time.asctime(), "Server Stops - %s:%s" % (HOST, PORT)