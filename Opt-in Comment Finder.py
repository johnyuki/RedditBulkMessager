import praw
import sqlite3
import time
import config

commentFooter = ('\n\n---\n\n^This ^message ^was ^sent ^by ^a ^script. ^If ^there ^is ^an ^issue, ^please ^message ^/u/{}'
                 .format(config.main_account))


def connect_to_database(): # Connects to the Database
    conn = sqlite3.connect('Subscriber List.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Subscribers(Username)')
    conn.commit()
    c.execute('CREATE TABLE IF NOT EXISTS OldComments(Comment)')
    return c, conn


def connect_to_reddit(): # Connects to Reddit account
    reddit = praw.Reddit(username=config.username, password=config.password, client_id=config.client_id,
                            client_secret=config.client_secret, user_agent=config.user_agent)
    return reddit


def get_old_comments(c, conn): # Takes old comment id's from database to make sure it doesn't send duplicate replies.
    oldComments = set()
    c.execute('SELECT Comment FROM OldComments')
    for username in c.fetchall():
        oldComments.add(username[0])
    return oldComments


def get_subscribed_users(c, conn): # Gets a list of users that are already subscribed so that it doesn't add them to the list again.
    subscribers = set()
    c.execute('SELECT Username FROM Subscribers')
    for username in c.fetchall():
        subscribers.add(username[0])
    return subscribers


def add_to_old_comments(c, conn, comment): # Adds comment ID to database
    c.execute('INSERT INTO OldComments VALUES(?)',(comment,))
    conn.commit()
    print('Added comment to old comments list.')


def add_user_to_database(c, conn, username): # Adds user to database
    c.execute('INSERT INTO Subscribers VALUES(?)',(username,))
    conn.commit()
    print('Added new user to subscriber list.')


def look_for_comments(reddit): # Searches through the comments in the post
    c, conn = connect_to_database()
    while True:
        submission = reddit.submission(id=config.thread_id)
        submission.comments.replace_more(limit=0)
        subscribers = get_subscribed_users(c, conn)
        oldComments = get_old_comments(c, conn)
        for comment in submission.comments.list():
            if config.keyword in comment.body and comment.author.name not in subscribers and comment.id not in oldComments:
                add_to_old_comments(c, conn, comment.id)
                add_user_to_database(c, conn, comment.author.name)
                comment.reply('Okay, I have added you to my list.'+commentFooter)
                print('Replied to new subscribed user')
            elif config.keyword in comment.body and comment.author.name in subscribers and comment.id not in oldComments:
                add_to_old_comments(c, conn, comment.id)
                comment.reply('I already have you on my list'+commentFooter)
                print('Replied to old subscribed user')
            elif config.keyword not in comment.body and comment.id not in oldComments:
                add_to_old_comments(c, conn, comment.id)



def main():
    reddit = connect_to_reddit()
    look_for_comments(reddit)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print('Critical error - '+str(e))
            print('System Message - Sleeping for 1 minute.')
            time.sleep(60)
