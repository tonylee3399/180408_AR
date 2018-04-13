import os
import cv2
import numpy
import scipy

"""
# open file ~~  39 folder : 64~65 pics / for_each_folder

deal with data~

"""
path = 'CroppedYale/'

train_data = []
test_data = []
train_label = []
test_label = []

man_flag=0

for filename in os.listdir(path):
    print(path+'/'+filename)
    paths, dirs, files = os.walk(path+'/'+filename).next()
    file_count = len(files)
    print(file_count)
    count_data=0
    #temp_train=[]
    #temp_test=[]
    for pic_name in os.listdir(path+'/'+filename):
        #print(path+'/'+filename+'/'+pic_name)
        if count_data==0:
            tmp = cv2.imread(path+'/'+filename+'/'+pic_name)
            #tmp = numpy.array(tmp)
        if count_data<35:
            img = cv2.imread(path+'/'+filename+'/'+pic_name)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = numpy.array(img)
            img = img.ravel()
            train_data.append(img)
            train_label.append(man_flag)
        elif count_data>=35 and count_data<64:
            img = cv2.imread(path+'/'+filename+'/'+pic_name)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = numpy.array(img)
            img = img.ravel()
            test_data.append(img)
            test_label.append(man_flag)
        count_data+=1
    man_flag+=1
    #train_data.append(temp_train)
    #test_data.append(temp_test)
print(train_data)
print(len(train_data))
train_data=numpy.array(train_data)
print('aaaaa', train_data)
print('aaaaa', train_data.shape)
quit()
test_data=numpy.array(test_data)
train_label=numpy.array(train_label)
test_label=numpy.array(test_label)
train_data=train_data.astype(int)
test_data=test_data.astype(int)
train_label=train_label.astype(int)
test_label=test_label.astype(int)
print("train_label.shape    : {}".format(train_label.shape))
print("test_label.shape     : {}".format(test_label.shape))
print("train_data.shape     : {}".format(train_data.shape))
print("test_data.shape      : {}".format(test_data.shape))
print("len(train_data)      : {}".format(len(train_data)))
print("len(test_data)       : {}".format(len(test_data)))
print("train_data[0])       : {}".format(train_data[0]))
print("test_data[0]         : {}".format(test_data[0]))
print("abs( test_data[0] - train_data[0] ) = {}".format(abs( test_data[0] - train_data[0] )))
print("test_data[0] - train_data[0]        = {}".format(test_data[0] - train_data[0]))

quit()
"""
    SAD
"""

ans=0
temp=0
for i in range( len(test_data) ):
    mins=10000000
    flag=0
    #print(i," ",temp)
    for j in range( len(train_data) ):
        temp = numpy.sum( abs( test_data[i].astype(int) - train_data[j].astype(int) ) )
        if temp<mins:
            flag = train_label[j]
            mins = temp
    if flag == test_label[i]:
        ans+=1
print('SAD  accuracy : ',ans/(38*29))

"""
    SSD
"""

ans=0
temp=0
for i in range( len(test_data) ):
    mins=numpy.sum( ( test_data[i].astype(int) - train_data[0].astype(int) )**2 )
    flag=0
    #print(i," ",temp)
    for j in range( len(train_data) ):
        temp = numpy.sum( ( test_data[i].astype(int) - train_data[j].astype(int) )**2 )
        
        if temp<mins:
            flag = train_label[j]
            mins = temp
    if flag == test_label[i]:
        ans+=1
print('SSD  accuracy : ',ans/(38*29))
