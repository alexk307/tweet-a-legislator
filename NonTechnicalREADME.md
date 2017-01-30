
- Download this code
  - Run: `git clone http://github.com/alexk307/tweet-a-legislator`
- Download and install [Python 2.7](https://www.python.org/download/releases/2.7/)
- Download and install [Virtualenv](https://virtualenv.pypa.io/en/stable/)
  - Run: `virtualenv env`. This will create your virtual environment
  - Run: `source env/bin/activate`. This is use your newly created environment
  - Run: `pip install -r requirements.txt`. This will install the dependencies needed for this project
  
- Create a Twitter [Application](https://apps.twitter.com/)
- Create a new file `.env` in this directory.
  - Add the following (fill in your credentials)
  ```
  access_token_key=
  access_token_secret=
  consumer_key=
  consumer_secret=
  ```
- Run: `python main.py`
