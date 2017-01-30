from twitter import Api, TwitterError
from dotenv import load_dotenv, find_dotenv

import os


load_dotenv(find_dotenv())


class Tweeter(object):

    def __init__(self):
        creds = {
            'consumer_key': os.environ.get('consumer_key'),
            'consumer_secret': os.environ.get('consumer_secret'),
            'access_token_key': os.environ.get('access_token_key'),
            'access_token_secret': os.environ.get('access_token_secret')
        }

        for name, cred in creds.iteritems():
            if cred is None:
                raise Exception(
                    'Misconfiguration error, Twitter creds missing %s' % name)
        self.api = Api(**creds)

    def tweet(self, to, message):
        try:
            tweet_body = '@%s %s' % (to, message)
            self.api.PostUpdate(tweet_body)
            print 'Posted: %s' % tweet_body
        except TwitterError as e:
            print 'Unable to post: %s' % str(e)


if __name__ == '__main__':
    t = Tweeter()
    t.tweet('kahankahan', 'asdf')
