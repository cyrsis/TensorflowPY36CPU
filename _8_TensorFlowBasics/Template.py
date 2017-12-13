# Dataset split: Training (70%), validation (20%), testing (10%)
# Model: Convolutional neural network.
# Layers: Kernels of size 2x2 with stride of 2
# Optimizer: RMSProp.
# Activation function: ELU (Exponential Linear Unit), because of the performance it has shown when compared to ReLUs
# Initialization: Xavier for the weights matrices in all layers.
# Regularization: Dropout with probability 0.5


#1.voting system
#  --A Create Mono
#  --B Create Spectrogram
#  --C Slice
#  --D Classify
#  --E Vote (Softmax -> output the probablity of each genre (Classification Confidence))

