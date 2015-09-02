from twython import Twython
from twiconfig import APP_KEY, ACCESS_TOKEN
import sqlite3
from datetime import datetime, timedelta
import time
conn = sqlite3.connect("twitwords.db")
c = conn.cursor()
conn.execute("CREATE TABLE IF NOT EXISTS tweets (word, time, user, twtext, twid)")
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
import pprint
pp = pprint.PrettyPrinter()
queries = [datetime.now() + timedelta(minutes=-15 + n / 30, seconds=n*2) for n in xrange(440) ]
for word in open('words.txt', 'rt'):
	word = word.strip()
	max_id = None
	seen = 0
	while True:
		fifteenminutes = datetime.now() + timedelta(minutes=-15)
		queries = [query for query in queries if query >= fifteenminutes]
		if len( queries ) > 440:
			print "Throttling"
			time.sleep(10)
			continue
		if max_id:
			data =  twitter.search(
							q='#' + word, 
							result_type='recent', 
							count=100, 
							max_id=max_id-1)
		else:
			data =  twitter.search(
							q='#' + word, 
							result_type='recent', 
							count=100, 
							until='2015-03-04')
		print "Got data for " + word
		queries.append( datetime.now() )
		
		too_old = False
		for status in data['statuses']:
			date = datetime.strptime( status['created_at'], "%a %b %d %H:%M:%S +0000 %Y")
			if date.day != 3:
				too_old = True
				break
			seen += 1
			c.execute("INSERT INTO tweets VALUES (?, ?, ?, ?, ?)", 
				(	word, 
					status['created_at'], 
					status['user']['screen_name'], 
					status['text'],
					status['id'] ) )
			max_id = status['id'] - 1
		conn.commit()
		print "#"+word, seen, date, max_id
		if too_old or len( data['statuses'] ) < 100:
			break
		