import os, sys

graph_mapped_bool = []
for i in range(0, 1000):
  graph_mapped_bool.append(False)

label_dir = str(sys.argv[1])
label_eval_file = open(label_dir + "/label_evaluate.txt",'r')
lines  = label_eval_file.readlines()
for line in lines:
    tmp = line.strip().split()
    graph_id, MII, II, number = list(map(int, tmp))
    graph_mapped_bool[graph_id] = True

unmapped_file = open("unmapped_file.txt",'a+')
unmapped_file.write(label_dir+" ")
num_unmaped = 0
unmapped_file.write("[")
for i in range(1000):
  if not graph_mapped_bool[i]:
    print(i)
    num_unmaped +=1
    if num_unmaped <=  20:
      unmapped_file.write(str(i) + ",")
unmapped_file.write("]\n")
unmapped_file.close()




