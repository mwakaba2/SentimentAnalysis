import json 
import time

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


def analyze(type):
	
	if type=="monthly":
		monthLst = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
		monthly_pos = [0]*12
		monthly_neg = [0]*12
		monthly_count = [0]*12
	else:
		yearLst = [2013, 2014, 2015, 2016]
		yearly_pos = [0]*4
		yearly_neg = [0]*4
		yearly_count = [0]*12
	
	with open('fb_comments_data.json') as data_file:
		data = json.load(data_file, strict=False)["data"]
		# monthly and yearly analysis
		for comment in data:
			comment_time = int(comment["time"])
			blob = TextBlob(comment["text"], analyzer=NaiveBayesAnalyzer())
			sentiment_results = blob.sentiment
			pos_result = sentiment_results.p_pos
			neg_result = sentiment_results.p_neg
			
			if type=="monthly":
				month = time.localtime(comment_time).tm_mon - 1
				monthly_pos[month]+=pos_result
				monthly_neg[month]+=neg_result
				monthly_count[month]+=1
			else:
				year = time.localtime(comment_time).tm_year - 2013
				yearly_pos[year]+=pos_result
				yearly_neg[year]+=neg_result
				yearly_count[year]+=1
			
			
		if type=="monthly":
			avg_monthly_pos = [ p / c for p, c in zip(monthly_pos, monthly_count)]
			avg_monthly_neg = [ n / c for n, c in zip(monthly_neg, monthly_count)]	
			print(avg_monthly_pos)
			print(avg_monthly_neg)
		else:
			avg_yearly_pos = [ p / c for p, c in zip(yearly_pos, yearly_count)]
			avg_yearly_neg = [ n / c for n, c in zip(yearly_neg, yearly_count)]
			print(avg_yearly_pos)
			print(avg_yearly_neg)
		
if __name__ == '__main__':
	# analyze("monthly")
	analyze("yearly")

