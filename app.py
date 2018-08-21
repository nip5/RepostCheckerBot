# packages that need to be pip installed
import praw

# packages that come with python
import sqlite3
import random
import sys

# other files
import config
import database

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)

subreddit = reddit.subreddit(config.subreddit)

conn = sqlite3.connect('Posts'+config.subreddit+'.db')

c = conn.cursor()

# the main function
def findPosts():
    while True:
        try:
            print('Starting searching...')
            post = 0
            # first get 1000 posts from the top of the subreddit
            for submission in subreddit.top('all', limit=1000):
                post += 1
                print('{} --> Starting new submission {}'.format(post, submission.id))
                result = database.isLogged(conn, submission.url, submission.media, submission.selftext, submission.permalink, submission.created_utc)
                if result != [['delete',-1,-1,-1]] and (result == [] or submission.created_utc != result[0][2]):
                    database.addPost(conn, submission.created_utc, submission.url, submission.media, submission.permalink, submission.selftext)
                    print('Added {}'.format(submission.permalink))
            post = 0
            # then get 1000 posts from new of the subreddit
            for submission in subreddit.new(limit=1000):
                post += 1
                print('{} --> Starting new submission {}'.format(post, submission.id))
                result = database.isLogged(conn, submission.url, submission.media, submission.selftext, submission.permalink, submission.created_utc)
                if result != [['delete',-1,-1,-1]] and (result == [] or submission.created_utc != result[0][2]):
                    database.addPost(conn, submission.created_utc, submission.url, submission.media, submission.permalink, submission.selftext)
                    print('Added {}'.format(submission.permalink))
            post = 0
            # then check posts as they come in
            for submission in subreddit.stream.submissions():
                post += 1
                print('{} --> Starting new submission {}'.format(post, submission.id))
                result = database.isLogged(conn, submission.url, submission.media, submission.selftext, submission.permalink, submission.created_utc)
                if result != [['delete',-1,-1,-1]] and (result == [] or submission.created_utc != result[0][2]):
                    database.addPost(conn, submission.created_utc, submission.url, submission.media, submission.permalink, submission.selftext)
                    print('Added {}'.format(submission.permalink))
                if result != [] and result != [['delete',-1,-1,-1]] and post > 1:
                        print('reported')
                        # report and make a comment
                        submission.report('REPOST ALERT')
                        cntr = 0
                        table = ''
                        for i in result:
                            table = table + str(cntr) + '|[post](https://reddit.com' + i[0] + ')|' + i[1] + '|' + str(i[3]) + '%' + '\n'
                            cntr += 1
                        fullText = 'I have detected that this may be a repost: \n\nNum|Post|Date|Match\n:--:|:--:|:--:|:--:\n' + table + '\n*Beep Boop* I am a bot | [Source](https://github.com/xXAligatorXx/repostChecker) | Contact u/XXAligatorXx for inquiries.'
                        doThis = True
                        while doThis:
                            try:
                                submission.reply(fullText)
                                doThis = False
                            except:
                                doThis = True
        except ValueError as e:
            if '503' in str(e):
                print('503 from server')
            else:
                f = open('errs.txt', 'a')
                f.write(str(e)) 

database.initDatabase(conn)
findPosts()
print(database.getAll(conn))
