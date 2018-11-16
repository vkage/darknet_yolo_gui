import sys
import os
import subprocess


Num_classes = int(sys.argv[1])
classes = str(sys.argv[2:])

wd = os.getcwd()

cfg_file = open('gui.cfg','r').readlines()
gui_cfg = open('gui.cfg','w')


filter_list =[]
for i in range(9):
	filter_list.append(int(sys.argv[i+1]))

train_flag = 0
test_flag = 0
f = 0

print('recieved filters list = ',filter_list)

for line in cfg_file:

    if train_flag != 0:
        train_flag-=1
        continue

    if test_flag != 0:
        test_flag-=1
        continue

    if line.find('Testing') != -1:
        gui_cfg.write('#Testing\n#batch=1\n#subdivisions=1\n')
        test_flag = 2
        continue

    if line.find('Training') != -1:
        # for tiny subdivision = 2 else 16
        gui_cfg.write('#Training\nbatch=64\nsubdivisions=2\n')
        train_flag = 2
        continue

    if line.find('filters') != -1:
    	# print('index',f)
    	gui_cfg.write('filters=%d\n'%filter_list[f])
    	f+=1
    	continue


    gui_cfg.write(line)

# print(filter_list)

gui_cfg.close()