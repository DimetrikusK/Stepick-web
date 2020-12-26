<<<<<<< HEAD
def app(environ, start_response):
     status = '200 OK'
     headers = [
         ('Content-Type', 'text/plain')
          ]
     body = [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding='utf8')]
     start_response(status, headers)
     return body
=======
#/usr/bin/env python3
#from urllib.parse import parse_qs

# python 2
#from cgi import parse_qs, escape
from re import sub

def app(environ, start_response):
    """wsgi minimal app.
    $ gunicorn hello:app
    """
    #parameters = parse_qs(environ.get('QUERY_STRING', ''))

    #output = ''
    #for p in parameters:
    #    for r in parameters[p]:
    #        output += p + '=' + r + '\n'

    # no parsing needed
    output = sub('&', '\n', environ.get('QUERY_STRING', ''))

    start_response('200 OK', [('Content-Type', 'text/plain')])
    return iter([str.encode(output)])
>>>>>>> 8c7649973076d0663cf048c1f510efdf5b0bdee4
