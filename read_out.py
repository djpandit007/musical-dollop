import linecache
import re
from plot_graph import plotGraoph

def parseOut():

    start_line_num = 13
    
    
    num_lines = sum(1 for line in open('out.txt'))
    red_edges = []
    red_lbl_dict = {} 
    
    
    for i in range(start_line_num,num_lines,4):
        line_learn_after = linecache.getline("out.txt", i)
        line_study = linecache.getline("out.txt", i+2)
        
        if "SATISFIABLE" in line_study: 
            break
        
        action = re.search(r'(?<=\().+(?=\))', line_study).group()
        
        
        
        for line in line_learn_after.split("learnAfter"):
            learn_arr = line.strip().replace("\n","").replace("(","").replace(")","").replace(",","").split( )
            if(learn_arr[0] == action):
                tmp_tuple = (learn_arr[0],learn_arr[1])
                red_edges.append(tmp_tuple)
                red_lbl_dict[tmp_tuple] = str(len(red_edges))
                break
        
        
    
    plotGraoph(red_edges,red_lbl_dict)