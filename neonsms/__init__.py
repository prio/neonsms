

class TwilioException(Exception):
    pass


class NeonException(TwilioException):
    pass


class TwilioRestException(TwilioException):
    pass


class NeonRestException(TwilioRestException):
    pass

