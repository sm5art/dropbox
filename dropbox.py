import tornado
import tornado.ioloop
import tornado.web
import os, uuid
__UL__ = "uploads/"
class Upload(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type","text/html")
        self.write("<form enctype='multipart/form-data' method='POST' action='/upload'><input type='file' name='filearg'/><br/><input type='submit'/></form>")
    
    def post(self):
        file = self.request.files['filearg'][0]
        fname = file['filename']
        f=open(__UL__+fname,'w+')
        f.write(file['body'])
        self.finish(fname)
        
class ViewFiles(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type","text/html")
        for filename in os.listdir(__UL__):
            self.write("<a href='{file}'>{filename}</a><br/>".format(file=__UL__+filename,filename=filename))
            
application = tornado.web.Application([
        (r"/", ViewFiles),
        (r"/upload", Upload),
        (r'/uploads/(.*)',tornado.web.StaticFileHandler, {'path': './uploads'})
        ], debug=True)
if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()