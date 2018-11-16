import sys
import os
import re

cfg_file = open('gui.cfg','r').readlines()
weight = open('gui_weights.txt','w')
#------------------------------------------------------------------
Num_classes = int(sys.argv[1])
num_of_weights = 0
flag = -1
filters_list = []
size_list = []
layer_out = {}
layer_in = {}
layer_count = -1
conv_count = -1
prev_conv = -1
dic = {}
c0 = 3
temp = -1
classes = Num_classes
class_flag = 0
maxpool_flag = 1
#------------------------------------------------------------------
for line in cfg_file:
	if line.find('maxpool') != -1:
		maxpool_flag = 1
	if line.find('convolutional') != -1:
		maxpool_flag = 0

	if line.find('filters') != -1:
		filt = int(line[line.find('=')+1:] )
		filters_list.append(filt)
		
	elif line.find('size') != -1 and maxpool_flag == 0:
		sz = int(line[line.find('=')+1:] )
		size_list.append(sz)

	elif line.find('channels') != -1:
		c0 = int( line[line.find('=')+1:] )

# print('\n\nfilters_list')
# print(filters_list)
# print('\nsize_list')
# print(size_list)
# print('\n')

num_of_weights = pow(size_list[0],2)*c0*filters_list[0];

for i in range(1,len(filters_list)):
	num_of_weights+=pow(size_list[i],2)*filters_list[i-1]*filters_list[i]

num_of_weights+=sum(filters_list)+9173
# num_of_weights+=sum(filters_list)+3461 	# offset for picoyolo
num_of_weights*=4/1000000.0


print('Weights in Mbytes : {0:3.6f} Mbytes\n'.format(num_of_weights))

weight.write('{0:3.6f}\n'.format(num_of_weights))

weight.close()