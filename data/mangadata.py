import os
# I cannot remember what is this for. Seems useless now.
directory = r'label'
for filename in os.listdir(directory):
    if filename.endswith(".txt") :
        print(os.path.join( filename))
    dot_index = filename.index(".")
    final_filename = "graph/" + filename[0: dot_index] + "_feature" + ".txt"
    print(final_filename)
    a_f = open("label/" + filename,'r')
    b_f = open(final_filename,'w+')
    for line in a_f:
        print(line)
        sharp_index = line.index("#")
        asap_value = line[0:sharp_index]
        b_f.write(asap_value + "\n")
    a_f.close()
    b_f.close()