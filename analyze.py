import json 
import time

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import plotly.plotly as py
import plotly.graph_objs as go

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

		print(monthly_pos)
		print(month)
		monthly_pos[month]+=pos_result
		count[month]+=1
		monthly_neg[month]+=neg_result

	avg_monthly_pos = [ p / c for p, c in zip(monthly_pos, count)]
	avg_monthly_neg = [ n / c for n, c in zip(monthly_neg, count)]

	print(avg_monthly_pos)
	print(avg_monthly_neg)

# yearly analysis

# trace0 = go.Bar(
#     x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
#        'Nov', 'Dec'],
#     y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
#     name='Primary Product',
#     marker=dict(
#         color='rgb(49,130,189)'
#     )
# )
# trace1 = go.Bar(
#     x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
#        'Nov', 'Dec'],
#     y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
#     name='Secondary Product',
#     marker=dict(
#         color='rgb(204,204,204)',
#     )
# )
# data = [trace0, trace1]
# layout = go.Layout(
#     xaxis=dict(
#         # set x-axis' labels direction at 45 degree angle
#         tickangle=-45,
#     ),
#     barmode='group',
# )
# fig = go.Figure(data=data, layout=layout)
# plot_url = py.plot(fig, filename='angled-text-bar')