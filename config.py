from decouple import config


HOST = config('HOST', default='127.0.0.1')
PORT = config('PORT', cast=int, default=5000)

CERTFILE = config('CERTFILE', default='ssl/server.crt')
KEYFILE = config('KEYFILE', default='ssl/server.ley')

