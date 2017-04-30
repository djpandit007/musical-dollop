from plotGraoph import plot_init

def parseDb():
	labels = {}
	edges = []
	index = 1
	with open('Shortlisted topics.md', 'r') as f:
		line = f.read()
		topic_list = line.split('.')
		labels.append(topic_list[0])
		dependencies = topic_list[1].split(',')

		for t in dependenices: 
			edges.append(('t'+str(index), 't'+str(index)))


		index = index + 1
	f = open('adaptiveSystem')
	for edge in edges:
		f.write('caused learnAfter('+edge[0]+edge[1]+').')
		

	plot_init(labels,edges)

