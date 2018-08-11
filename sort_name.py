import os
import sys
from PIL import Image
#-------------------------------------------------------------------------------
# Name:        sort_name
# Purpose:     format image file name to sequential format
# Author:      Aixi WAng
# Created:     2018-08-11
#
#-------------------------------------------------------------------------------

#---------------------
# dir_loop1
#---------------------
def dir_loop1(sub_dir):
    dst_path = sub_dir 
    
    
    i = 0
    for r, d, files in os.walk(dst_path):
        #print('r:',r, ' d:',d, ' files:',files)
        for file in files:
            #print(r,d,file)
            #print 'file:',file
            
            p = r + '\\' + file
            #print('========================================================================================')
            new_name = "%05d.jpg" %(i)
            new_full_name = r + '\\' + new_name
            cmd_s = 'mv ' + p + ' '  + new_full_name
            print(cmd_s)
            #os.system(cmd_s)
            try:
                os.rename(p, new_full_name)
            except Exception as e:
                print('exception:',str(e))
                s = raw_input('any key to continue...')
            i += 1
            


    i = 0
    for r, d, files in os.walk(dst_path):
        for file in files:
            p = r + '\\' + file        
            try: 

                img = Image.open(p)
                img2 = img.resize((448,448),Image.ANTIALIAS)
                #p2 = '.\\temp\\' + file
                img2.save(p)
                
                 
                print('resize file:',p)            
            except Exception as e:
                #os.remove(p)
                print('exception:',str(e))
                s = raw_input('any key to continue...')
            i += 1

            
            

            
dir_loop1(sys.argv[1])
            