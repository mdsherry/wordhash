import sqlite3

conn = sqlite3.connect('twitsmall.db')
c = conn.cursor()

minutes = ["{:02}:{:02}".format( h, m ) for h in xrange(24) for m in xrange(60)]

def chunk(it, n):
	while it:
		yield it[:n]
		it = it[n:]


from collections import defaultdict
histdata = defaultdict( lambda: dict( [x,0] for x in minutes ) )

words = ['military', 'chocolate', 'pray', 'lion', 'architecture', 'endless', 'pet', 'engineering']
for word in words:
	for row in c.execute("SELECT word, time FROM minitweets where word = ?", (word,)):
		histdata[row[0]][row[1][11:16]] += 1

	total = 0
	for ms in chunk(minutes, 15):
		for m in ms:
			current = histdata[word][m]
			total += current
		histdata[word][ms[0]] = (current, total)

todump = []
for m in minutes[::15]:
	data = dict( (word, histdata[word][m][1]) for word in words )
	data['time_'] = m
	todump.append(data)

import json
with open('data.json','wb') as f:
	json.dump( {'words': words, 'data': todump}, f )