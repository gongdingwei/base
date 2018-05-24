#!/usr/bin/env python
# encoding: utf-8
"""
tensorflow :generate my own dataset
@author: mengping
"""


import requests #首先导入库
import  re
import os
import urllib


def dowmloadPic(html,keyword):
    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    print '找到关键词:'+keyword+'的图片，现在开始下载图片...'
    for each in pic_url:
        print '正在下载第'+str(i+1)+'张图片，图片地址:'+str(each)
        try:
            pic= requests.get(each, timeout=30)
        except requests.exceptions.ConnectionError:
            print '【错误】当前图片无法下载'
            continue
        foldername = 'car_56'
        folder_dir = './'+" " + foldername
        ext = os.path.exists(folder_dir)
        if ext == False:
            os.mkdir(folder_dir)

        # string = './F16-3/'+str(i) + '.jpg'
        string = folder_dir + '/' + foldername + '-' + str(i) + '.jpg'
        print string
        #resolve the problem of encode, make sure that chinese name could be store
        fp = open(string.decode('utf-8').encode('cp936'),'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':
    word = raw_input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    result = requests.get(url)
    dowmloadPic(result.text,word)