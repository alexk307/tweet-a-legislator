from clone_data import clone
from social import get_information
from tweet import Tweeter


def get_tweet_body_from_user():
    return raw_input('What would you like to say? [Reminder: Tweet body + '
                     '@mention of legislator must be <= 140 chars]\n')


def main():
    body = get_tweet_body_from_user()
    tweeter = Tweeter()
    clone()
    data = get_information()
    for legislator_id, legislator in data.iteritems():
        name = legislator.get('name')
        job = legislator.get('job')
        party = legislator.get('party')
        title = '%s %s %s' % (party, job, name)
        twitter_handle = legislator.get('twitter')
        if twitter_handle is None:
            print '%s has no twitter account' % title
            continue

        handle = legislator.get('twitter')
        try:
            tweeter.tweet(handle, body)
        except Exception as e:
            print 'Unable to post tweet: %s' % str(e)

if __name__ == '__main__':
    main()
