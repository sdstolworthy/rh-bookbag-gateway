
class BaseConfig(object):
  DEBUG = False
  FAKED = False

class FakedConfig(object):
  FAKED = True
  DEBUG = True