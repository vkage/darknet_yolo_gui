import sys
import os
import re

# cfg_file = open('cfg/yolov3-voc.cfg','r').readlines()
cfg_file = open('yolov2-tiny-voc.cfg','r').readlines()
weight = open('gui_weights.txt','w')
res1 = open('cmp2','w')
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
# No route/shortcut/upsample/yolo layer in YOLO V2
#------------------------------------------------------------------
# def route(lst,layer_no):

# 	if len(lst)==1:
# 		temp = layer_out[lst[0]]
# 	else:
# 		temp = layer_out[lst[0]] + layer_out[lst[1]]

# 	return temp
	#print(temp)
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


	# elif line.find('classes') != -1:
	# 	classes = int( line[line.find('=')+1:] )
	# 	#print(classes)
	elif line.find('channels') != -1:
		c0 = int( line[line.find('=')+1:] )

print('\n\nfilters_list')
print(filters_list)
print('\nsize_list')
print(size_list)
print('\n')

layer_in.update({0:c0})

for line in cfg_file:
	line = line.strip()
	if line.find('convolutional') != -1:
		conv_count+=1
		layer_count+=1
		if conv_count > 0:
			layer_in.update({layer_count:filters_list[conv_count-1]})
		if temp > 0:
			layer_in.update({layer_count:temp})
			temp = -1
		layer_out.update({layer_count:filters_list[conv_count]})
		dic.update({layer_count:conv_count})
		res1.write(str(+[layer_count])+ " "+ str(layer_out[layer_count]) + '\n')
		flag = 1
		continue

	if line.find('[route]') != -1 :
		flag = 2
		layer_count+=1
		continue

	if line.find('[shortcut]') != -1 :
		layer_count+=1
		layer_in.update({layer_count:filters_list[conv_count]})
		layer_out.update({layer_count:filters_list[conv_count]})
		continue

	if line.find('[upsample]') != -1 :
		layer_count+=1
		layer_in.update({layer_count:filters_list[conv_count]})
		layer_out.update({layer_count:filters_list[conv_count]})
		continue

	if line.find('[yolo]') != -1 :
		layer_count+=1
		filters_list[dic[layer_count-1]] = 3*(classes+5)
		layer_out.update({layer_count-1:3*(classes+5)})
		continue

	if flag == 1 and prev_conv != conv_count:
		prev_conv+=1

	if flag == 2 and line.find('layers') != -1:
		ls = re.split('=|= | = |, | , | ', line)
		ls.remove('layers')
		toLayer = [int(item) if int(item)>0 else layer_count + int(item) for item in ls]
		temp = route(toLayer,layer_count)
#------------------------------------------------------------------
for key in dic:
	a = size_list[dic[key]]*size_list[dic[key]]
	num_of_weights += a*layer_in[key]*layer_out[key]+layer_out[key]
#------------------------------------------------------------------
num_of_weights += 78917
Mb = num_of_weights*4/1000000.0

# print('Total number of weights : %d\n'%(num_of_weights))
# print('Total number of weights in bytes : %d bytes\n'%(num_of_weights*4))

print('Weights in Mbytes : {0:3.6f} Mbytes\n'.format(Mb))

# weight.write('Total number of weights : %d\n'%(num_of_weights))
# weight.write('Weights in bytes : %d bytes\n'%(num_of_weights*4))
# weight.write('Weights in Mbytes : {0:3.6f} Mbytes\n'.format(Mb))

weight.write('{0:3.6f}\n'.format(Mb))

weight.close()
res1.close()

#print(filters_list)