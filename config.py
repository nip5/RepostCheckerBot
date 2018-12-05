import os
# your reddit app client id
client_id = 'client_id'
client_secret = 'client_secret'
user_agent = 'BotName'
# username and password of account to post under
username = 'Username'
password = 'Pass'
subSettings = [
    [
        'RepostBotTest',
        int(os.environ['BOT_TOP_DAYS']) if 'BOT_TOP_DAYS' in os.environ else None,
        int(os.environ['BOT_HOT_DAYS']) if 'BOT_HOT_DAYS' in os.environ else None,
        int(os.environ['BOT_NEW_DAYS']) if 'BOT_NEW_DAYS' in os.environ else None,
        int(os.environ['BOT_TOP_NUM_POSTS']) if 'BOT_TOP_NUM_POSTS' in os.environ else 1000,
        int(os.environ['BOT_HOT_NUM_POSTS']) if 'BOT_HOT_NUM_POSTS' in os.environ else 1000,
        int(os.environ['BOT_NEW_NUM_POSTS']) if 'BOT_NEW_NUM_POSTS' in os.environ else 1000,
        int(os.environ['BOT_THRESH']) if 'BOT_THRESH' in os.environ else 5,
    ],
    [
        os.environ['BOT_SUBREDDIT2'],
        int(os.environ['BOT_TOP_DAYS2']) if 'BOT_TOP_DAYS2' in os.environ else None,
        int(os.environ['BOT_HOT_DAYS2']) if 'BOT_HOT_DAYS2' in os.environ else None,
        int(os.environ['BOT_NEW_DAYS2']) if 'BOT_NEW_DAYS2' in os.environ else None,
        int(os.environ['BOT_TOP_NUM_POSTS2']) if 'BOT_TOP_NUM_POSTS2' in os.environ else 1000,
        int(os.environ['BOT_HOT_NUM_POSTS2']) if 'BOT_HOT_NUM_POSTS2' in os.environ else 1000,
        int(os.environ['BOT_NEW_NUM_POSTS2']) if 'BOT_NEW_NUM_POSTS2' in os.environ else 1000,
        int(os.environ['BOT_THRESH2']) if 'BOT_THRESH2' in os.environ else 5,
    ] if 'BOT_SUBREDDIT2' in os.environ else None,
]
