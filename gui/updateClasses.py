import sys
import os
import subprocess


Num_classes = int(sys.argv[1])
classes = str(sys.argv[2:])

wd = os.getcwd()

#--------------------------------------------------------------------
# creating voc.names file as voc_gui.names
#--------------------------------------------------------------------
voc_gui = open('voc_gui.names','w')
for l in sys.argv[2:]:
    voc_gui.write(l+'\n')
voc_gui.close()

#--------------------------------------------------------------------
# Converting scripts/voc_label.py
#--------------------------------------------------------------------
voc_label = open('%s/scripts/voc_label.py'%(wd),'r').readlines()
voc_label_gui = open('%s/voc_label_gui.py'%(wd), 'w')
for line in voc_label:
    if line.find('classes') == 0:
        voc_label_gui.write('classes = '+classes+'\n')
    else:
        voc_label_gui.write(line)
voc_label_gui.close()

#--------------------------------------------------------------------
# Creating train file 
#--------------------------------------------------------------------
print("\n calling python voc_label_gui.py\n")
subprocess.call('python voc_label_gui.py',shell=True)


#--------------------------------------------------------------------
# Converting cfg/voc.data
#--------------------------------------------------------------------
voc_data_gui = open('%s/voc_gui.data'%(wd),'w')

voc_data_gui.write('classes = '+str(Num_classes)+'\n')
voc_data_gui.write('train  = train.txt\n')
voc_data_gui.write('valid  = 2007_test.txt\n')
voc_data_gui.write('names  = voc_gui.names\n')
voc_data_gui.write('backup  = backup\n')

voc_data_gui.close()

#--------------------------------------------------------------------
# Converting cfg/yolov3-voc.cfg
#--------------------------------------------------------------------
input_cfg = open('yolov2-tiny-voc.cfg','r').readlines()
#gui_cfg = open('cfg/yolov3-%s'%(file_name)+'.cfg', 'w')
gui_cfg = open('gui.cfg', 'w')

train_flag = 0
test_flag = 0

class_index = []
filter_index = []
index = 0

for line in input_cfg:
    if line.find('classes') != -1:
        class_index.append(index)
    if line.find('filters') != -1:
        filter_index.append(index)
    index+=1

fp =[]
flag = 0
for ci in class_index:
    flag = 0
    for fi in filter_index:
        if ci<fi and flag == 0:
            flag = 1
            fp.append(filter_index[filter_index.index(fi)-1])
fp.append(filter_index[-1])

index = 0

print("------ xoxoxo -------")
print('class_index = ',class_index)
print('filter_index = ',filter_index)
print('fp = ',fp)
print("------ xoxoxo -------")

for line in input_cfg:

    if train_flag != 0:
        train_flag-=1
        index+=1
        continue

    if test_flag != 0:
        test_flag-=1
        index+=1
        continue

    if line.find('Testing') != -1:
        gui_cfg.write('#Testing\n#batch=1\n#subdivisions=1\n')
        test_flag = 2
        index+=1
        continue

    if line.find('Training') != -1:
        # for tiny subdivision = 2 else 16
        gui_cfg.write('#Training\nbatch=64\nsubdivisions=2\n')
        train_flag = 2
        index+=1
        continue

    if index in fp:
        gui_cfg.write('filters=%d'%(5*(Num_classes+5))+'\n')
        index+=1
        continue
    if index in class_index:
        gui_cfg.write('classes=%d'%(Num_classes)+'\n')
        index+=1
        continue
    # print(index,line)
    gui_cfg.write(line)
    index+=1

gui_cfg.close()