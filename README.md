#http://arbu00.blogspot.hk/2017/05/4-tensorflowlenet5.html

This one is really really good

# Working on the study of tensorflow

This is really good one

http://www.jianshu.com/p/86f2a252581a

https://github.com/nfmcclure/tensorflow_cookbook/tree/master/03_Linear_Regression



https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/2-4-variable/

November 25, 2017 4:33 pm

# reinforcement learning is actually CPU the most


#work on this tomorrow

https://morvanzhou.github.io/tutorials/machine-learning/torch/4-04-A-autoencoder/


# TensorflowPY36CPU

RL :

在基于价值这边有 Q learning, Sarsa 
基于概率这边, 有 Policy Gradients

(Monte-Carlo Update)
Monte-carlo learning 和基础版的 policy gradients 等 都是回合更新制 

(Temporal-Difference Update)
Qlearning, Sarsa, 升级版的 policy gradients 等都是单步更新制


在线学习
 Sarsa -
 优化 Sarsa 的算法, 叫做 Sarsa lambda

离线学习
Q learning
根据离线学习的属性, 开发了更强大的算法, 比如让计算机学会玩电动的 Deep-Q-Network

#Find out the score for each game

https://gym.openai.com/envs/


# Working on the TensorFlow for AI, Mostly will be sandbox to get me up and running quicky

#Dates

https://raw.githubusercontent.com/caicloud/tensorflow-tutorial/master/datasets/flowers/flowers.zip

# Show it in Tensorboard

1. # Define path to TensorBoard log files
logPath = "./tb_logs/"

2. tensorboard --log tb_logs 

# Use Name in the variable rather than generateed one

house_size = tf.placeholder("float", name="house_size")
price = tf.placeholder("float", name="price")


# Upgrade the backage

pip install SomePackage --upgrade

#Check Pyton Version 

 python -V
 
#Library will be using (anaconda Python 3.6)

NLTk
XgBoost
scikit-learn
keras
Networkx
Lasagne (Python 2)
Theao
Mxnet
gym
PyMc3
Cmake
pyTorch
CNTK
beautifulsoup
sympy
psycopg2
flask
Pil (Python 2)
pillow
jupyter
ipython
msgpack-python
Requests



tensorpack
pip install -U git+https://github.com/ppwwyyxx/tensorpack.git


Add more changes
ImportError: DLL load failed: The specified module could not be found.

Path set to 
C:\Users\user\AppData\Local\conda\conda\envs\tensorflowGPU\python.exe


Caffee
Open cv
pip install opencv-python (For )

Rx

pip install rx

seaborn
    statsmodels
OpenCV cv2
conda install -c conda-forge opencv (Works in Python 3.6)

Run the following command:

conda install -c https://conda.binstar.org/menpo opencv
I realized that opencv3 is also available now, run the following command:

conda install -c https://conda.binstar.org/menpo opencv3
Edit on Aug 18, 2016: You may like to add the "menpo" channel permanently by:

conda config --add channels menpo
And then opencv can be installed by:

conda install opencv(or opencv3)
Edit on Aug 14, 2017: "clinicalgraphics" channel provides relatively newer vtk version for very recent python3

conda install -c clinicalgraphics vtk

gym

pip install gym
pip install --no-index -f https://github.com/Kojoley/atari-py/releases atari_py

Works like charm on Windows

pip install moviepy
brew install ffmpeg


#Requirements

pip install -r requirements.txt

#Export Conda environment

Export to .yml file

conda env export > freeze.yml
To reproduce:

conda env create -f freeze.yml



# Extra reading
Sutton & Barto
http://incompleteideas.net/sutton/book/the-book-2nd.html


# Ipython shortkey

tab: 代码提示
shift+Enter: 运行,并将光标移动到下一行 control+Enter: 运行,不会将光标移动到下一行 shift+tab: 代码解释
shift+tab: 连按两次,显示更多注释信息
B: 插入cell
Y: 切换为code M: 切换为Markdown
L: 显示代码行数 D: 连按两次,删除cell
S: 保存文件 Shift + Control/Command + P: 选择命令

# Kind of funny for the reinforcment learning for Vm ubuntu
Do not have GPU, I still can use AMD one


# Additional Resources

###Official Resources:

 - [TensorFlow Python API](https://www.tensorflow.org/api_docs/python/)
 - [TensorFlow on Github](https://github.com/tensorflow/tensorflow)
 - [TensorFlow Tutorials](https://www.tensorflow.org/tutorials/)
 - [Udacity Deep Learning Class](https://www.udacity.com/course/deep-learning--ud730)
 - [TensorFlow Playground](http://playground.tensorflow.org/)

###Github Tutorials and Examples:

 - [Tutorials by pkmital](https://github.com/pkmital/tensorflow_tutorials)
 - [Tutorials by nlintz](https://github.com/nlintz/TensorFlow-Tutorials)
 - [Examples by americdamien](https://github.com/aymericdamien/TensorFlow-Examples)
 - [TensorFlow Workshop by amygdala](https://github.com/amygdala/tensorflow-workshop)

###Deep Learning Resources

 - [Efficient Back Prop by Yann LeCun, et. al.](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
 - [Online Deep Learning Book, MIT Press](http://www.deeplearningbook.org/)
 - [An Overview of Gradient Descent Algorithms by Sebastian Ruder](http://sebastianruder.com/optimizing-gradient-descent/)
 - [Stochastic Optimization by John Duchi, et. al.](http://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf)
 - [ADADELTA Method by Matthew Zeiler](http://arxiv.org/abs/1212.5701)
 - [A Friendly Introduction to Cross-Entropy Loss by Rob DiPietro](http://rdipietro.github.io/friendly-intro-to-cross-entropy-loss/)


###Additional Resources

 - [A Curated List of Dedicated TensorFlow Resources](https://github.com/jtoy/awesome-tensorflow/)

###Arxiv Papers

 - [TensorFlow: Large-Scale Machine Learning on Heterogeneous Distributed Systems](http://arxiv.org/abs/1603.04467)
 - [TensorFlow: A system for large-scale machine learning](http://arxiv.org/abs/1605.08695)
 - [Distributed TensorFlow with MPI](https://arxiv.org/abs/1603.02339)
 - [Comparative Study of Deep Learning Software Frameworks](https://arxiv.org/abs/1511.06435)
 - [Wide & Deep Learning for Recommender Systems](https://arxiv.org/abs/1606.07792)
