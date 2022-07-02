import os 
import sys
import shutil
from shutil import copyfile
import argparse


label_location  = "labels/"


def evaluate_label(MII, II, number):
    if "systolic" in label_dir:
        if II == MII:
            return True
        else: 
            return False
    if II == MII:
        return True
    elif MII+1 == II and number > 1:
        return True

    return False

parser = argparse.ArgumentParser(description='Process label filter parameter.')
parser.add_argument("-r", "--raw_graph_directory", default="cgra_me/transformered_graph",  help="the home directory of transformered graph")
parser.add_argument("-l", "--label_dir", default="cgra_me_4_4",  help="the home directory of labels, under data/labels/")

args = parser.parse_args()
raw_graph_directory =   args.raw_graph_directory
label_dir = label_location + args.label_dir
print("raw graph  directory:", args.raw_graph_directory)
print("label directory:", args.label_dir)
enable_filter = True

#filter label
good_label = []
label_eval_file = open(label_dir + "/label_evaluate.txt",'r')
lines  = label_eval_file.readlines()
for line in lines:
    tmp = line.strip().split()
    graph_id, MII, II, number = list(map(int, tmp))
    # print((graph_id, MII, II, number))
    # if graph_id < 1000:
    if enable_filter and evaluate_label(MII, II, number):
        good_label.append(graph_id)
    if not enable_filter:
        good_label.append(graph_id)
label_eval_file.close()


#write log
if enable_filter:
    label_filter_log = open('./label_filter_log.txt', 'a+')
    label_filter_log.write(label_dir + " all label: "  + str(len(lines)) + " after filter:" +str(len(good_label)) +"\n")
    label_filter_log.close()
print("all label: ", len(lines), "after filter:", len(good_label))

training_data_dir = ""
if  enable_filter:
    training_data_dir = os.path.join("training_dataset", args.label_dir)
else:
    training_data_dir = os.path.join("training_dataset", args.label_dir +"_no_filter")


if os.path.exists(training_data_dir):
        shutil.rmtree(training_data_dir)

training_data_dir = os.path.join(training_data_dir, "raw")

os.makedirs(training_data_dir)
os.makedirs(training_data_dir+"/label")

shutil.copytree(raw_graph_directory, training_data_dir + "/graph")

for id in good_label:
    copyfile(label_dir+"/"+str(id)+".txt", training_data_dir+"/label"+"/"+str(id)+".txt")

print("done")






    