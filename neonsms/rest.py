import os
import urllib
import urllib2
from neonsms import NeonException, NeonRestException


def find_credentials(environ=None):
    """
    Look in the current environment for Neon credentials

    :param environ: the environment to check
    """
    environment = environ or os.environ
    try:
        account = environment["NEON_USERNAME"]
        token = environment["NEON_PASSWORD"]
        return account, token
    except KeyError:
        return None, None


class Messages(object):
    def __init__(self, account, token, base):
        self.account = account
        self.token = token
        self.base = base

    def create(self, to=None, from_=None, body=None):
        url = '{}/sms.php?user={}&clipwd={}&text={}&to={}'.format(
            self.base, self.account, self.token, urllib.quote(body), to
        )
        try:
            resp = urllib2.urlopen(url)
            if resp.getcode() != 200:
                raise NeonRestException('Unable to GET {}, {} recieved'.format(
                    url, resp.getcode())
                )
        except urllib2.URLError, e:
            raise NeonRestException(e.reason)



class NeonRestClient(object):
    def __init__(self, account=None, token=None,
                 base="https://api.neonsolutions.ie"):
        # Get account credentials
        if not account or not token:
            account, token = find_credentials()
            if not account or not token:
                raise NeonException("""
Neon could not find your account credentials. Pass them into the
NeonRestClient constructor like this:

    client = NeonRestClient(account='AC38135355602040856210245275870',
                              token='2flnf5tdp7so0lmfdu3d')

Or, add your credentials to your shell environment. From the terminal, run

    echo "export NEON_USERNAME=AC3813535560204085626521" >> ~/.bashrc
    echo "export NEON_PASSWORD=2flnf5tdp7so0lmfdu3d7wod" >> ~/.bashrc

and be sure to replace the values for the Account SID and auth token with the
values from your Neon Account at http://www.neonsms.ie
""")
        self.messages = Messages(account, token, base)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("{} <to number>".format(sys.argv[0]))
    else:
        client = NeonRestClient()
        client.messages.create(to=sys.argv[1], body="Hi there")
