from instapy import InstaPy
import json
import input_cred

input_cred.cred_input("credentials.json") #comment this line if youre deploying this to a server


#loading credentials
with open('credentials.json') as c:
    data = json.load(c)

#logging in
session = InstaPy(username = data["username"], password = data["password"])
session.login()

#session tasks
session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=15,
                              peak_likes_daily=100,
                               peak_comments_hourly=9,
                               peak_comments_daily=36,
                                peak_follows_hourly=1,
                                peak_follows_daily=None,
                                 peak_unfollows_hourly=15,
                                 peak_unfollows_daily=100,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)
session.set_smart_hashtags(['poetry', 'writing', 'writers'], limit=3, sort='top', log_tags=True)
session.like_by_tags(["writers", "writersofinstagram", "poetry", "writer", "writerscommunity", "writing", "writersofig", "poets", "authors", "wordporn"], amount=5, use_smart_hashtags=True)
session.set_do_comment(True, percentage=60)
session.dont_include(['user1', 'user2', 'user3', 'user3'])
session.set_dont_unfollow_active_users(enabled=True, posts=3)
session.set_skip_users(skip_private=True,
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=100)
                       
session.set_delimit_liking(enabled=True, max_likes=300, min_likes=20)
session.set_comments([u"Woah! :heart_eyes", "Awesome! :heart_eyes", "This is real good! :heart_eyes", "Lovely :100"])
session.set_relationship_bounds(enabled=True, max_followers=5000)
session.unfollow_users(amount=60, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="FIFO", unfollow_after=90*60*60, sleep_delay=501)
session.set_use_clarifai(enabled=True, api_key=data["clarifai_api"])
session.clarifai_check_img_for(['nsfw', 'naked'])
session.end()


