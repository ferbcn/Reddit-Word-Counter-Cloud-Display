#!/usr/bin/python

import praw
import sys

from config import ID, SECRET, AGENT
from stopwords import stopwords

from wordcloud import WordCloud
import matplotlib.pyplot as plt

top = 20 #number of top words to display in ranking

def CountWords(sub, LIM):
    reddit = praw.Reddit(client_id=ID, client_secret=SECRET, user_agent=AGENT)
    reddit.read_only = True
    subreddit = reddit.subreddit(sub)
    # print to console without new line
    mes = ('Crawling through titles in subreddit: ' + sub.upper ())
    sys.stdout.write ('\r' + (mes))

    counter=0
    allTitles = []
    allComments = []
    allWords = []
    allWordsStr = ""

    #every submission in this subreddit
    for submission in subreddit.hot(limit=LIM):
        counter+=1
        #print('-------------- '+str(i)+' --------------')
        #print(counter,'/',LIM,' - Title: ', submission.title, end='\r')
        #print("Text: ", submission.selftext)
        #print("Score: ", submission.score)
        #print("---------------------------------\n")
        allTitles.append(submission.title)

        # extract all top level comments (very slow)
        """# read every comment for this submission
        for top_level_comment in submission.comments:
            try:
                #print (top_level_comment.body)
                allComments.append (top_level_comment.body)
            except Exception as e:
                print (e)

    # extract every word from all comments and append to allWords
    for comment in allComments:
        words = str(comment).split()
        for word in words:
            if word.lower() not in stopwords:
                allWords.append(word)
                allWordsStr += word + " "
    """

    # extract every word from all titles and append to allWords
    for title in allTitles:
        words = title.split()
        for word in words:
            if not word.lower() == sub.lower() and word.lower() not in stopwords:
                allWords.append(word)
                allWordsStr += word + " "
    allWordsStr.replace (sub.lower(), '')

    # count all words by putting words and results in a dictionary
    countedWords = {}
    for word in allWords:
        if word not in countedWords.keys():
            countedWords[word] = 1
        else:
            countedWords[word] += 1

    # sort the counted word dictionary and put it in a list
    words_sorted_by_value = sorted(countedWords.items(), key=lambda kv: kv[1], reverse=True)
    return words_sorted_by_value[0:top], allWordsStr

if __name__ == '__main__':
    print('###############################')
    print('### Reddit Wordcounter v1.0 ###')
    print ('###############################')
    #subs = "cplusplus java python javascript golang ruby brainfuck swift"
    #lim = 100

    # get user input
    lsubs = 0
    while (lsubs==0 or lsubs>9):
        subs = input("Subreddit(s) to search in (separated by space): ")
        lsubs = len(subs.split())
        if lsubs > 9:
            print("Max number of subreddits is 9!")
    lim=0
    while (lim<=0 or lim>1000):
        lim = int (input ("Number of submissions to crawl through: "))
        if lim > 1000:
            print("Max number of submissions is 1000!")

    results = {} #ranked results: dictionary of subreddits containing a list of tuples (top words: frquency) for each subreddit
    allWords = {} #all words concatenatet as a string (needed for cloudword module input)

    # get the data
    subs = subs.split()
    for sub in subs:
        results[sub], allWords[sub] = CountWords(sub, lim)
    print("\n")


    header = "RANK"
    for sub in subs:
        header = ('{0:5}{1:20}'.format (header, sub.upper()))
    print (header)

    # Print results as table
    for r in range(top):
        rowString = "#"+str(r+1)+" "
        for sub in subs:
            column = results[sub]
            rowString = ('{0:5}{1:20}'.format (rowString, str(column[r])))
        print(rowString)


    # draw wordclouds with wordcloud module and matplotlib
    # define sublots, rows (max. = 3), columns (max. = 3)... i am sure there are more elegant ways to do this
    l = len(subs)
    # define rows
    rows = 1
    if l > 3:
        rows = 2
    if l > 6:
        rows = 3
    # define columns
    if l > 3:
        cols = 3
    else:
        cols = l

    # draw the figure/canvas
    fig = plt.figure (figsize=(18, 10))
    fig.canvas.set_window_title ('Reddit Wordclouds 1.0')
    subplotcounter = 1
    #draw each wordcloud in a subplot
    for sub in subs:
        #print(allWords[sub])
        plt.subplot (rows, cols, subplotcounter)
        subplotcounter += 1
        wordcloud = WordCloud (width=800, height=600, margin=0).generate (allWords[sub])
        # Display the generated image:
        plt.imshow (wordcloud, interpolation='bilinear')
        plt.axis ("off")
        plt.title(sub)
        plt.margins (x=0, y=0)

    plt.show ()