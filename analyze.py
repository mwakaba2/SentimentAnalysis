import json 
import time

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_pos = [0]*12
monthly_neg = [0]*12
count = [0]*12

with open('fb_comments_data.json') as data_file:
	data = json.load(data_file, strict=False)["data"]
	# monthly analysis
	for comment in data:
		comment_time = int(comment["time"])
		blob = TextBlob(comment["text"], analyzer=NaiveBayesAnalyzer())
		sentiment_results = blob.sentiment
		pos_result = sentiment_results.p_pos
		neg_result = sentiment_results.p_neg
		month = time.localtime(comment_time).tm_mon - 1

		monthly_pos[month]+=pos_result
		count[month]+=1
		monthly_neg[month]+=neg_result

	avg_monthly_pos = [ p / c for p, c in zip(monthly_pos, count)]
	avg_monthly_neg = [ n / c for n, c in zip(monthly_neg, count)]

	print(avg_monthly_pos)
	print(avg_monthly_neg)

# yearly analysis

