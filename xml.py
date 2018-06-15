#encoding:utf-8
import os
def generate(dir):
  files = os.listdir(dir)
  files.sort()
  print '****************'
  print 'input :',dir
  print 'start...',files
  for file in files:
     fileType = os.path.splitext(file)
     Olddir = os.path.join(dir, file)
     print Olddir
     newname = os.path.join(dir, str(fileType[0]).zfill(4))+ '.xml'
     print newname
     os.rename(Olddir, newname)


if __name__ == '__main__':
     generate('./xml')