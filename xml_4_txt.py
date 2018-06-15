import os
import re
import cv2
import sys

xmlfilepath = '/home/asus/Annotations';
txtsavepath = '/home/asus/Annotations';
trainval_percent = 0.5; # trainval占整个数据集的百分比，剩下部分就是test所占百分比
train_percent = 0.5; # train占trainval的百分比，剩下部分就是val所占百分比

#
xmlfile = dir(xmlfilepath);
numOfxml = len(xmlfile) - 2; # 减去.和..总的数据集大小

trainval = sort(randperm(numOfxml, floor(numOfxml * trainval_percent)));
test = sort(setdiff(1:numOfxml, trainval));


trainvalsize = len(trainval); # trainval的大小
train = sort(trainval(randperm(trainvalsize, floor(trainvalsize * train_percent))));
val = sort(setdiff(trainval, train));

ftrainval = open([txtsavepath 'trainval.txt'], 'w');
ftest = open([txtsavepath 'test.txt'], 'w');
ftrain = open([txtsavepath 'train.txt'], 'w');
fval = open([txtsavepath 'val.txt'], 'w');

for i in numOfxml:
    if ismember(i, trainval)
        fprintf(ftrainval, '%s\n', xmlfile(i + 2).name(1:end - 4));
        if ismember(i, train)
            fprintf(ftrain, '%s\n', xmlfile(i + 2).name(1:end - 4));
            else
            fprintf(fval, '%s\n', xmlfile(i + 2).name(1:end - 4));
            end
        else
            fprintf(ftest, '%s\n', xmlfile(i + 2).name(1:end - 4));
            end
        end
    ftrainval.close(ftrainval);
    ftest.close(ftrain);
    ftrain.close(fval);
    fval.close(ftest);