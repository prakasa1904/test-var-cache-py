import time
import json
import requests, sys, urllib2
from config import endpoint

class PostModel:
	def getPostData(self):
		tic = time.clock()
		req = requests.get(endpoint.POST)
		if req.status_code == 200:
			toc = time.clock()
			print 'Response Time Our API is %s' % (toc - tic)
			return req.json()
		else:
			data = {
				'message' : 'Failed',
				'status': req.status_code
			}
			return json.dumps(data)