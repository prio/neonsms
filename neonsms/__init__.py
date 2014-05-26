

__author__ = 'Jonathan Harrington'
__version__ = '0.0.2'
__license__ = 'BSD'


class TwilioException(Exception):
    pass


class NeonException(TwilioException):
    pass


class TwilioRestException(TwilioException):
    pass


class NeonRestException(TwilioRestException):
    pass
