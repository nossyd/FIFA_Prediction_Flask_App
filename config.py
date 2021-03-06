class Config(object):
    pass

class ProdConfig(Config):
    SECRET_KEY = '\xa2\xde\x86\xb9\xe46a\xb1\xc9tE\xccW\xdbw\x16\xb4\xff\x0e\x88\xee\xb4'
    JSON_SORT_KEYS = False

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = '\xa2\xde\x86\xb9\xe46a\xa2t\xbaatdit\x12y\xea\x16\xb4\xff\x0e\x88\xee\xb4'
    JSON_SORT_KEYS = False