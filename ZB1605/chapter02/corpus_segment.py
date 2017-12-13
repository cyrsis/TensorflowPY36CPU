# -*- coding: utf-8 -*-

import sys  
import os 
import jieba

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
	
corpus_path = "train_corpus_small/"  # 未分词分类语料库路径
seg_path = "train_corpus_seg/"      # 分词后分类语料库路径

catelist = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录

# 获取每个目录下所有的文件
for mydir in catelist:
	class_path = corpus_path+mydir+"/"    # 拼出分类子目录的路径
	seg_dir = seg_path+mydir+"/"          # 拼出分词后语料分类目录
	if not os.path.exists(seg_dir):       # 是否存在目录，如果没有创建
			os.makedirs(seg_dir)	
	file_list = os.listdir(class_path)    # 获取class_path下的所有文件
	for file_path in file_list:           # 遍历类别目录下文件
		fullname = class_path + file_path   # 拼出文件名全路径
		content = readfile(fullname).strip()  # 读取文件内容
		content = content.replace("\r\n","") # 删除换行和多余的空格
		content_seg = jieba.cut(content.strip())		# 为文件内容分词
		savefile(seg_dir+file_path," ".join(content_seg))  # 将处理后的文件保存到分词后语料目录

print "中文语料分词结束！！！"