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
                       print(name +'- Post :' + t_to_l(post.title) + '\n') 
                    if not secret:
                       print(name +'- Post :' + post.title + '\n')
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
                        print(name + '- Comment :' +t_to_l(comment.body) + '\n')
                    if not secret:
                        print(name + '- Comment :' +comment.body + '\n')
                except:
                    pass
                
                break

def main(name, words_to_search, subreddits, which = 'pc' ):
    subreddits = '+'.join(subreddits)
    if 'p' in which:
        title = threading.Thread(target = title_monitor, args =[name, words_to_search, subreddits]).start()
    if 'c' in which:
        comment = threading.Thread(target = comment_monitor,args = [name, words_to_search, subreddits]).start()
    return



amd_wrds = ['amd', 'lisa su', 'advanced micro devices', ]
g_sts = ['wallstreetbets','investing','robinhood','gaming','stocks']



main('AMD', amd_wrds, g_sts, 'pc')
main('ETHER', ['eth'], ['ethtrader', 'ethinsider', 'ethereum', 'cryptomarkets', 'cryptocurrency', 'golemproject'], 'pc')

def devon():
    
    words = input('What words should I search for?\n Seperate by a comma and don\'t add spaces between words and commas \n ENTER WORDS HERE ->').lower().split(',')
    subreddits = input('\nWhat sub? \n again, Seperate by a comma and don\'t add spaces between subs and commas\n').lower().split(',')
    name = input('What do you want to call this search?')
    secret_us = input('Scrabled eggs? y/n')
    which = input('Type \'p\' for posts and \'c\' for comments, type \'pc\' for both').lower()
    
    if 'y' in secret_us.lower():
        global secret
        secret = True
    main(name,words,subreddits, which)


