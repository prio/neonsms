from neonsms import (
    NeonException, TwilioException, NeonRestException, TwilioRestException
)
import unittest


class TestExceptions(unittest.TestCase):
    def test_a_neonexception_behaves_like_a_twilio(self):
        try:
            raise NeonException
        except TwilioException:
            pass
        else:
            self.fail("Exception should have been caught")

    def test_a_neonrestexception_behaves_like_a_twilio(self):
        try:
            raise NeonRestException
        except TwilioRestException:
            pass
        else:
            self.fail("Exception should have been caught")

    def test_a_neonrestexception_behaves_like_a_twilioexception(self):
        try:
            raise NeonRestException
        except TwilioException:
            pass
        else:
            self.fail("Exception should have been caught")
