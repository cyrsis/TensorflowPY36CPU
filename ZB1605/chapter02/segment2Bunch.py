# -*- coding: utf-8 -*-

import sys  
import os 
import jieba
import cPickle as pickle
from sklearn.datasets.base import Bunch

# 配置utf-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

# 保存至文件
def savefile(savepath,content):
	fp = open(savepath,"wb")
	fp.write(content)
	fp.close()
	
# 读取文件	
def readfile(path):
	fp = open(path,"rb")
	content = fp.read()
	fp.close()
	return content
	
# Bunch类提供一种key,value的对象形式
# target_name:所有分类集名称列表
# label:每个文件的分类标签列表
# filenames:文件路径
# contents:分词后文件词向量形式	
bunch = Bunch(target_name=[],label=[],filenames=[],contents=[])	

wordbag_path = "train_word_bag/train_set.dat"  # 未分词分类语料库路径
seg_path = "train_corpus_seg/"      # 分词后分类语料库路径

catelist = os.listdir(seg_path)  # 获取seg_path下的所有子目录
bunch.target_name.extend(catelist)
# 获取每个目录下所有的文件
for mydir in catelist:
	class_path = seg_path+mydir+"/"    # 拼出分类子目录的路径
	file_list = os.listdir(class_path)    # 获取class_path下的所有文件
	for file_path in file_list:           # 遍历类别目录下文件
		fullname = class_path + file_path   # 拼出文件名全路径
		bunch.label.append(mydir)
		bunch.filenames.append(fullname)
		bunch.contents.append(readfile(fullname).strip())		# 读取文件内容
		
#对象持久化                                                                                              
file_obj = open(wordbag_path, "wb")
pickle.dump(bunch,file_obj)                      
file_obj.close()

print "构建文本对象结束！！！"