from plot_init import plotInit

def parseDb():
	labels = []
	edges = []
	index = 1
	with open('shortlistedTopics.md', 'r') as f:
		lines = f.readlines()
		for line in lines:
			topic_list = line.split('.')
			print(topic_list)
			labels.append('t'+str(index))
			dependencies = topic_list[1].strip().replace('\n','').split(' ')
			print('depend'+str(dependencies))
			for t in dependencies:
				if(t!=''):
					edges.append(('t'+str(index), 't'+str(t)))


			index = index + 1
	f = open('adaptiveSystem','a')
	for edge in edges:
		f.write('caused learnAfter('+edge[0]+','+edge[1]+').'+'\n')
	print(labels)
	print(edges)	

	plotInit(labels,edges)

