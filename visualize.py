import plotly
import plotly.graph_objs as go


def visualize(x_coords, y1_coords, y2_coords):

	pos = go.Bar(
	    x=x_coords,
	    y=y1_coords,
	    name='Positive Score',
	    marker=dict(
	        color='rgb(255,111,111)'
	    )
	)
	neg = go.Bar(
	    x=x_coords,
	    y=y2_coords,
	    name='Negative Score',
	    marker=dict(
	        color='rgb(0,133,255)',
	    )
	)

	data = [pos, neg]
	layout = go.Layout(
		title='Monthy Facebook Comments Sentiment Analysis',
	    xaxis=dict(
	        # set x-axis' labels direction at 45 degree angle
	        tickangle=-45,
	    ),
	    barmode='group',
	)

	fig = go.Figure(data=data, layout=layout)
	plot_url = plotly.offline.plot(fig, filename="monthly_barchart")



if __name__ == '__main__':
	m_x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	m_y1 = [5]*12
	m_y2 = [5]*12

	y_x = [2013, 2014, 2015, 2016]
	y_y1 = [5]*12
	y_y2 = [5]*12
	
	visualize(m_x, m_y1, m_y2)
	# visualize(y_x, y_y1, y_y2)