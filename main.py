import praw
import threading


def title_monitor(name, words_to_search, subreddits):
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit(subreddits)
    for post in subreddit.stream.submissions():
        for word in words_to_search:
            if word in post.title.lower():
                
                print(name +' - POST ' + str(post))
                try:
                    print(post.title + '\n')
                except:
                    pass
                
                break
                
def comment_monitor(name, words_to_search, subreddits):
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit(subreddits)
    for comment in subreddit.stream.comments():
        for word in words_to_search:
            if word in comment.body.lower():
                print(name + ' - COMMENT ' + str(comment))
                try:
                    print(comment.body + '\n')
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
main('ETHER', ['eth'], ['ethtrader', 'ethinsider', 'etherium', 'cryptomarkets', 'cryptocurrency'])
    
