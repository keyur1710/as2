import webapp2
import urllib
import os
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),'index.html')
        context = {}
        self.response.out.write(template.render(path,context))
    def post(self):
        pincode = self.request.get('input')
        path = 'https://api.postalpincode.in/pincode/'+pincode
        data = urllib.urlopen(path).read()
        data = json.loads(data)
        context = {
            'post_office':data[0]['PostOffice'][0]['Name'],
            'state':data[0]['PostOffice'][0]['State'],
            'district':data[0]['PostOffice'][0]['District']
        }
        path = os.path.join(os.path.dirname(__file__),'result.html')
        self.response.out.write(template.render(path,context))

class AboutPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__),'about.html')
        self.response.out.write(template.render(path,{}))


app = webapp2.WSGIApplication([('/',MainPage),('/about',AboutPage)],debug=True)

