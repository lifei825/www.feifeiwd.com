# -*- coding: utf-8 -*-
import os
import sys
  
from tornado.options import options, define, parse_command_line
# import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

Port = sys.argv[1]
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = "ffwdsite.settings"
  
define('port', type=int, default=Port)


class MonitorHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('aaaaaa')

    
def main():
    parse_command_line()
      
    wsgi_app = tornado.wsgi.WSGIContainer(
        get_wsgi_application())
        # django.core.handlers.wsgi.WSGIHandler())
        
    tornado_app = tornado.web.Application([
        (r'.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        (r'/monitor', MonitorHandler),
                ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
           
if __name__ == '__main__':
        main()
