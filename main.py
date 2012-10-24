import logging
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from django.template import TemplateDoesNotExist
#os.environ['DJANGO_SETTINGS_MODULE'] = 'horstsc.be.settings'

from google.appengine.dist import use_library


class HomePage(webapp.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write('coming soon, in 2014 ...\n\n')
        values = {}
        self.response.out.write(template.render("templates/index.html", values))

# loading the mappings
mappings = [
            ('/', HomePage)
            ]

# initialize the app with the mappings
application = webapp.WSGIApplication(mappings,debug=True)


def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    #logging.getLogger().setLevel(logging.DEBUG)
    run_wsgi_app(application)

if __name__ == '__main__':
  main()
