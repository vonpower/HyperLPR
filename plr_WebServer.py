#pip install hyperlpr
#pip install tornado
#ab -n 100 -c 10 -p ab_post.txt -T 'application/json' 49.4.85.8:8022/plr/
import tornado.ioloop
import tornado.web
from hyperlpr import pipline
import cv2
import numpy as np
import json
import base64
import uuid

def readb64(uri):
	encoded_data = uri.split(',')[1]
	nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	return img


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('''You should use post method.''')
	
		
class PLR(tornado.web.RequestHandler):
	def get(self):
		self.write('''You should use post method.''')
		
	def post(self):
		try:
			param = self.request.body.decode('utf-8')
			prarm = json.loads(param)
			image = readb64(prarm["pic"])
			filename=str(uuid.uuid1()).replace("-", "")
			cv2.imwrite("./pics/"+filename+'.png', image)
			#self.set_header("Content-Type", "text/plain")
			#self.write("You wrote " + self.get_argument("pic"))
			r=pipline.RecognizePlateJson(image)
			
			print(r)
			self.finish({'result': r,'status':'ok'})
		except:	
			self.finish({'result':'unknown error.','status':'error'})
			
def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
		(r"/plr/", PLR),
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(8022)
	tornado.ioloop.IOLoop.current().start()