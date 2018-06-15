# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os,urllib2
import requests,sys
from tutorial.settings import IMAGES_STORE

img_index=0

class TutorialPipeline(object):
    def process_item(self, item, spider):
        global img_index
        imgPath=sys.path[0] + item["image_path"]  # 下载图片的保存路径
        if not os.path.isdir(imgPath):
            os.makedirs(imgPath)

        for url in item["image_url"]:
            print("download:", url)
            # 未能正确获得网页 就进行异常处理
            try:
                res = urllib2.urlopen(url)
                if str(res.status) != '200':
                    #print('download failure:', url)
                    continue
            except Exception as e:
                print('download failure..:', url)
            filename = os.path.join(imgPath, str(img_index) + '.jpg')
            with open(filename, 'wb') as f:
                f.write(res.read())
                print('download OK \n')
                img_index += 1
        return item


        return item
