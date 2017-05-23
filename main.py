import praw
import threading
from ttll import t_to_l

secret = False


def title_monitor(name, words_to_search, subreddits):
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit(subreddits)
    for post in subreddit.stream.submissions():
        for word in words_to_search:
            if word in post.title.lower():
                try:
                    if secret:
                       print(t_to_l(post.title) + '\n') 
                    if not secret:
                       print(name + ':' + post.title + '\n')
                except:
                    pass
                
                break
                
def comment_monitor(name, words_to_search, subreddits):
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit(subreddits)
    for comment in subreddit.stream.comments():
        for word in words_to_search:
            if word in comment.body.lower():
                try:
                    if secret:
                        print(t_to_l(comment.body) + '\n')
                    if not secret:
                        print(name + ':' +comment.body + '\n')
                except:
                    pass
                
                break

def main(name, words_to_search, subreddits):
    subreddits = '+'.join(subreddits)
    title = threading.Thread(target = title_monitor, args =[name, words_to_search, subreddits]).start()
    comment = threading.Thread(target = comment_monitor,args = [name, words_to_search, subreddits]).start()

amd_wrds = ['amd', 'lisa su', 'advanced micro devices', ]
g_sts = ['wallstreetbets','investing','robinhood','gaming','stocks']



main('AMD', amd_wrds, g_sts)
main('ETHER', ['eth'], ['ethtrader', 'ethinsider', 'etherium', 'cryptomarkets', 'cryptocurrency', 'golemproject'])

def devon():
    
    words = input('What words should I search for?\n Seperate by a comma and don\'t add spaces between words and commas \n ENTER WORDS HERE ->').lower().split(',')
    subreddits = input('\nWhat sub? \n again, Seperate by a comma and don\'t add spaces between subs and commas\n').lower().split(',')
    name = input('What do you want to call this search?')
    secret_us = input('Scrabled eggs? y/n')
    if 'y' in secret_us.lower():
        global secret
        secret = True
    main(name,words,subreddits)

