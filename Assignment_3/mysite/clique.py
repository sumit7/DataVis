node_list = []
edge_list = []
edge = []

def makegraph():
 f = open("log-graph.out", "rb")
 while True:
	x = f.readline()
	if not x: 
            break

	x = x.split(" ")
	if x[1] == 'node':
		node_list.append(int(x[2].split(",")[0]))
             

	if x[1] == 'edge':
		a = x[2].split("-")
		edge = [int(a[0]), int(a[1].split("\r\n")[0])]
                if edge[0] == edge[1]:
                   continue	
                edge_list.append(edge)
  
 f.close()


def adjlist(node):
 temp_list = []
 for i in range(len(edge_list)):
     if (edge_list[i][0] == node):
        temp_list.append(edge_list[i][1])
     elif (edge_list[i][1] == node):
        temp_list.append(edge_list[i][0])
 return temp_list       


def find_clique(node):
 clique_list = [node]
 common_list = adjlist(node)
 while len(common_list): 
  index = 0
  maximum = 0
  for i in range(len(common_list)):
    temp = len(list(set(common_list).intersection(adjlist(common_list[i]))))
    if maximum < temp:
      index = i
      maximum = temp     
  clique_list.append(common_list[index])
  common_list = list(set(common_list).intersection(adjlist(common_list[index])))
 return clique_list


def wrapper():
 cluster_no = 0
 fw = open("cluster.out","rw+")
 while len(node_list):
   ret_list = find_clique(node_list[0])
   for i in range(len(ret_list)):
       if len(ret_list) > 6:
         fw.write(str(ret_list[i]))
         fw.write(",")  
       j=0
       print(str(len(edge_list)))
       while j<len(edge_list):
#           print(str(len(edge_list)) + " ha " + str(j))    
#           print(str(edge_list[j][0]) + " " + str(edge_list[j][1]))         
           if (edge_list[j][0] == ret_list[i]) or (edge_list[j][1] == ret_list[i]):
              edge_list.pop(j)
           else: j=j+1
       node_list.remove(ret_list[i])
   if len(ret_list) > 6:
    cluster_no = cluster_no+1
    fw.write(str(cluster_no))   
    fw.write("\n")
 fw.close()


makegraph()
wrapper()
