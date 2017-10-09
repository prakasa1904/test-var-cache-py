import time
import os.path
from os import curdir, sep
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from config import HOST, PORT, MIME_TYPES_PERMITTED, MEMORY_KEY
from cache import Cache
from fetch import PostModel

MEMORY_DATA = {}

class ServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		cache = Cache(MEMORY_DATA)
		post = PostModel()
		""" Let's Count Our API Peformance """
		cacheData = cache.get(MEMORY_KEY)
		if cacheData != False:
			print "========= MEMORY DATA ========="
			print "%s" % cacheData
			print "========= MEMORY DATA ========="
		else:
			jsonData = post.getPostData()
			cache.set(MEMORY_KEY, jsonData)
		""" Let's Count Our API Peformance """

if __name__ == '__main__':
	server = HTTPServer((HOST, PORT), ServerHandler)
	print time.asctime(), "Server Starts - %s:%s" % (HOST, PORT)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		server.server_close()
		print time.asctime(), "Server Stops - %s:%s" % (HOST, PORT)