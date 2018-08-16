# Reddit Word-Counter & Word-Cloud-Display
Counts and ranks top words found in titles of the selected subreddits and displays a wordcloud for each subreddit

# Setup 
1. Create a [reddit personal use script application](https://www.reddit.com/prefs/apps/).

2. Add a `config.py` file to your working directory and add your applications credentials.
	 
	 ID='YOUR_ID'  
	 SECRET='YOUR_SECRET'  
	 AGENT='Example Bot by /u/example_bot'  

3. Run `pip install -r requirements.txt`

Optional: edit stopwords.py (words that are excluded from word count)
	 
# Run
Run: word_counter.py
  
  
# Example console ouput:

###############################
### Reddit Wordcounter v1.0 ###
###############################
Subreddit(s) to search in (separated by space): cryptocurrency bitcoin ethereum nanocurrency
Number of submissions to crawl through: 100
Crawling through titles in subreddit: NANOCURRENCY

RANK CRYPTOCURRENCY      BITCOIN             ETHEREUM            NANOCURRENCY        
#1   ('Crypto', 10)      ('BTC', 7)          ('blockchain', 6)   ('Nano', 25)        
#2   ('Bitcoin', 9)      ('2018', 5)         ('decentralized', 6)('NANO', 14)        
#3   ('Ethereum', 7)     ('Coinbase', 5)     ('Vitalik', 5)      ('August', 9)       
#4   ('Blockchain', 7)   ('Cryptocurrency', 5)('ETH', 5)          ('2018', 8)         
#5   ('Million', 6)      ('crypto', 4)       ('Casper', 4)       ('Daily', 7)        
#6   ('blockchain', 6)   ('Buy', 4)          ('Blockchain', 4)   ('General', 7)      
#7   ('Coinbase', 6)     ('Market', 4)       ('crypto', 4)       ('Discussion', 7)   
#8   ('Token', 5)        ('Lightning', 4)    ('Buterin', 3)      ('London', 6)       
#9   ('2018', 4)         ('learn', 3)        ('Coinbase', 3)     ('nano', 5)         
#10  ('Vitalik', 4)      ('Investors', 3)    ('Trinity', 3)      ('new', 4)          
#11  ('new', 4)          ('ETF', 3)          ('Protocol', 3)     ('Hunt', 3)         
#12  ('Fund', 4)         ('cryptocurrency', 3)('contracts', 3)    ('node', 3)         
#13  ('crypto', 4)       ('world', 3)        ('Smart', 3)        ('Block', 3)        
#14  ('Price', 4)        ('new', 3)          ('Contracts', 3)    ('2', 3)            
#15  ('August', 3)       ('Blockchain', 3)   ('Centralized', 3)  ('best', 3)         
#16  ('AT&T', 3)         ('needs', 2)        ('Read', 2)         ('thanks', 3)       
#17  ('$224', 3)         ('August', 2)       ('tweet', 2)        ('Weekly', 2)       
#18  ('Buterin', 3)      ('process', 2)      ('history', 2)      ('good', 2)         
#19  ('Classic', 3)      ('buy', 2)          ('Future', 2)       ('Update', 2)       
#20  ('Cryptocurrencies', 3)('American', 2)     ('Google', 2)       ('Treasure', 2)     


