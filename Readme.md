# Insta Bot
- A simple bot to automate your online experience on Instagram

## Requirements
1. Instapy
2. Mozilla Firefox Browser
3. Python 3.7+

## Installation
```
pip install -r requirements.txt
```

## Run development
```
python insta-bot.py
```

### Quick notes
1. You need a [ClarifAI](https://www.clarifai.com) API key. Paste it in the input field along with your Instagram username and password
2. You can deploy this on [Heroku](https://www.heroku.com) and make sure to add the firefox buildpack before final deployment
3. Don't keep your username, password or api key in the python file itself as this can cause security issues