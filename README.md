# tweet-a-legislator
Tweets all U.S. Legislators on Twitter. Gets current legislator social media data from [congress-legislators](https://github.com/unitedstates/congress-legislators) and tweets your message to all legislators with a Twitter account.

### Setup
Create virtualenv, install `requirements.txt`

### Run
`python main.py`

### Configure
Set environment variables with Twitter App information or put them into a `.env` file.
You'll need:
  - `access_token_key`
  - `access_token_secret`
  - `consumer_key`
  - `consumer_secret`

Don't have these? Set up a Twitter [application](https://apps.twitter.com/)
