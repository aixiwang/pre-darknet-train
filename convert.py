# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:55:43 2015

This script is to convert the txt annotation files to appropriate format needed by YOLO 

@author: Guanghan Ning
Email: gnxr9@mail.missouri.edu
"""

import os
from os import walk, getcwd
from PIL import Image
import sys

classes = ["stop","alarm"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
    
"""-------------------------------------------------------------------""" 

""" Configure Paths"""   
#mypath = "labels/stopsign_original/"
#outpath = "labels/stopsign/"
mypath = sys.argv[1]
outpath = sys.argv[2]


cls = sys.argv[3]
if cls not in classes:
    exit(0)
cls_id = classes.index(cls)

wd = getcwd()
list_file = open('%s/%s_list.txt'%(wd, cls), 'w')

print('mypath',mypath)

""" Get input text file list """
txt_name_list = []
#for (dirpath, dirnames, filenames) in walk(mypath):
#    print('filenames',filenames)    
#    txt_name_list.extend(filenames)
    
for r, d, files in os.walk(mypath):
    #print('r:',r, ' d:',d, ' files:',files)
    for file in files:
        #print(r,d,file)
        #print 'file:',file
        
        p = r + '\\' + file
        print('p:',p)
        txt_name_list.append(p)
    #break
print(txt_name_list)

""" Process """
for txt_name in txt_name_list:
    # txt_file =  open("Labels/stop_sign/001.txt", "r")
    
    """ Open input text files """
    #txt_path = mypath + txt_name
    #print("Input:" + txt_path)
    txt_file = open(txt_name, "r")
    lines = txt_file.read().split('\n')   #for ubuntu, use "\r\n" instead of "\n"
    
    """ Open output text files """
    txt_name2 = txt_name.split('\\')[-1]
    txt_outpath = outpath + '\\' + txt_name2
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "w")
    
    
    """ Convert the data to YOLO format """
    ct = 0
    for line in lines:
        #print('lenth of line is: ')
        #print(len(line))
        #print('\n')
        if(len(line) >= 2):
            ct = ct + 1
            print(line + "\n")
            elems = line.split(' ')
            print('elems:',elems)
            xmin = elems[0]
            xmax = elems[2]
            ymin = elems[1]
            ymax = elems[3]
            #
            s1 = wd
            s2 = cls
            s3 = os.path.splitext(txt_name2)[0]
            img_path = str('%s/Images/%s/%s.jpg'%(s1, s2, s3))
            print('img_path:',img_path)
            #t = magic.from_file(img_path)
            #wh= re.search('(\d+) x (\d+)', t).groups()
            im=Image.open(img_path)
            w= int(im.size[0])
            h= int(im.size[1])
            #w = int(xmax) - int(xmin)
            #h = int(ymax) - int(ymin)
            # print(xmin)
            print(w, h)
            b = (float(xmin), float(xmax), float(ymin), float(ymax))
            bb = convert((w,h), b)
            print('bb:',bb)
            txt_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

    """ Save those images with bb into list"""
    if(ct != 0):
        list_file.write('%s/Images/%s/%s.jpg\r\n'%(wd, cls, os.path.splitext(txt_name2)[0]))
                
list_file.close()       
