Collect and do basic analysis on Twitter hashtags based on common nouns collected over a fixed time period.

Uses nouns from http://www.wordfrequency.info/free.asp

---

This program was written after a discussion with a friend about the tendency of people to make #random #words into hashtags on Twitter. 

Some of the frequent hashtags were surprises (#raw, referring to the WWE program, was the most common hashtag). Others (#sex was 4th most common) were not.

Frequency visualization for some of the more interesting common terms can be found at http://alfedenzia.com/tweets/

Future efforts would involve removing more common terms (e.g. #sex, #adult, #win) from consideration, which would save a considerable amount of time - Twitter's API has a limit of 450 requests per rolling 15 minutes; with 100 tweets per request, this means an upper bound of 3000 tweets per minute. This means that #win (with 111579 tweets) took over half an hour to finish retrieving.