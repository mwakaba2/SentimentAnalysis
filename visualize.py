import plotly
import plotly.graph_objs as go


def visualize(x_coords, y1_coords, y2_coords, file_name):

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
	    yaxis=dict(
	        range=[0, 0.6]
	    ),
	    barmode='group',
	    bargap=0.3,
	)

	fig = go.Figure(data=data, layout=layout)
	plot_url = plotly.offline.plot(fig, filename=file_name)



if __name__ == '__main__':
	m_x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	m_y1 = [0.4885, 0.5698, 0.5837, 0.5085, 0.4392, 0.5043, 0.5000, 0.4719, 0.4883, 0.4448, 0.4255, 0.5152]
	m_y2 = [0.5115, 0.4302, 0.4163, 0.4915, 0.5608, 0.4956, 0.4999, 0.5281, 0.5117, 0.5552, 0.5745, 0.4848]

	y_x = [2013, 2014, 2015, 2016]
	y_y1 = [0.4864558250322787, 0.5152354313311347, 0.4472422999772394, 0.4605680911092713]
	y_y2 = [0.5135441749677212, 0.48476456866886547, 0.5527577000227606, 0.5394319088907287]
	
	# visualize(m_x, m_y1, m_y2, "monthly_barchart")
	visualize(y_x, y_y1, y_y2, "yearly_barchart")