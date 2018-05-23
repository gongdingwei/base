#encoding:utf-8
import os
def generate(dir):
  files = os.listdir(dir)
  files.sort()
  print '****************'
  print 'input :',dir
  print 'start...',files
  listText = open(dir+'/'+'list.txt','w')
  for file in files:
     fileType = os.path.splitext(file)
     # fileType = os.path.split(file)
     if fileType[1] == '.txt':
         continue
     name = fileType[0] +'\n'
     listText.write(name)
  listText.close()


if __name__ == '__main__':
     generate('./voc')