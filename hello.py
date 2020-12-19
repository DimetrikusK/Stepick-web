def wsgi_application(environ, start_response):
    print(environ)
    # status = '200 OK'
    # headers = [
    #     ('Content-Type', 'text/plain')
    # ]
    # body = 'Hello, world!'
    # start_response(status, headers)
    # return [body]