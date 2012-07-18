import logging
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
#os.environ['DJANGO_SETTINGS_MODULE'] = 'horstsc.be.settings'

from google.appengine.dist import use_library
use_library('django', '1.2')

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Force Django to reload its settings.
#from django.conf import settings
#settings._target = None

#import django.core.handlers.wsgi
#import django.core.signals
#import django.db
#import django.dispatch

# Log errors.
#import logging
#def log_exception(*args, **kwds):
#    logging.exception('Exception in request:')
#
#django.dispatch.Signal.connect(
#    django.core.signals.got_request_exception, log_exception)

# Unregister the rollback event handler.
#django.dispatch.Signal.disconnect(
#    django.core.signals.got_request_exception,
#    django.db._rollback_on_exception)

class HomePage(webapp.RequestHandler):
    def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('coming soon, in 2014 ...\n\n')

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
