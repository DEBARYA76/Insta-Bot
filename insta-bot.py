from instapy import InstaPy
import json

#loading credentials
with open('credentials.json') as c:
    data = json.load(c)

#logging in
session = InstaPy(username = data["username"], password = data["password"], headless_browser= True)
session.login()

#session tasks
session.set_quota_supervisor(enabled=True, peak_comments_daily= 60, peak_comments_hourly=10, peak_likes_daily=60, peak_likes_hourly=10)
session.like_by_tags(["writers", "writersofinstagram", "poetry", "writer", "writerscommunity", "writing", "writersofig", "poets", "authors", "wordporn"], amount=5)
session.set_do_comment(True, percentage=60)
session.set_comments(["Woah! :heart_eyes", "Awesome! :heart_eyes", "This is real good! :heart_eyes"])
session.set_relationship_bounds(enabled=True, max_followers=5000)
session.set_use_clarifai(enabled=True, api_key=data["clarifai_api"])
session.clarifai_check_img_for(['nsfw', 'naked'])
session.end()


