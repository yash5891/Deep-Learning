# -*- coding: utf-8 -*-
"""pytorch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J17bo5oEOz4xHVJqgrJE3IOo3c3Itz9X
"""

import torch

a = torch.rand(3,4)
a

a = torch.empty(3,4)
a

a = torch.zeros(3, 4)
a

a = torch.zeros(3, 4, dtype=torch.long)
a#.short=inttype=16 .long=inttype64

a = torch.tensor([[10, 20, 4],
                  [0, 0, 4]])
a

import numpy as np

a = np.ones(7)
b = torch.from_numpy(a)
a, b

import numpy as np

a = np.ones(7)
b = torch.from_numpy(a)
a, b

import numpy as np

a = np.ones(7)
x = np.ones(7)
b = torch.from_numpy(x)
a, b
b.numpy()

b *= 2
a,b

a = torch.rand(4,3)
b = torch.rand(4,3)
a+b

torch.add(a,b)

result = torch.empty(4, 3)
torch.add(a, b, out=result) # stored in tensor `result`.
result

a = torch.rand(3,4)
b = torch.rand(4,5)
c = torch.mm(a,b)
c

a@b

a.sum(), a.min(), a.max()

a[0, 0].item() # float data type

a = torch.rand(1,3,1,4)
b=a.shape, a.squeeze().shape
b

torch.cuda.is_available()

device_cpu = torch.device('cpu')  # CPU
device_gpu = torch.device('cuda') # GPU
device_cpu, device_gpu

# prompt: Import torch and print the version number.

import torch
print(torch.__version__)

# prompt:  Create a 1D tensor of numbers from 0 to 9

torch.arange(10)

# prompt:  Question: Create a 2D tensor of shape 5x3 to contain random decimal numbers between 5 and 10.

import torch

# Create a 2D tensor of shape 5x3 with random decimal numbers between 5 and 10
tensor = torch.randint(5,9,(5, 3))


# Print the tensor
print(tensor)

# prompt:  Create a 3×3 tensor of all True’s

a = torch.ones(3,3, dtype=torch.bool)
a

a=torch.arange(1,100,2)
a

# prompt: eplace all odd numbers in above arr with -1

a = torch.arange(1,100)
a[a % 2 != 0] = -1
a

arr = torch.arange(10)
arr.reshape()

# prompt: Convert a 1D tensor to a 2D tensor with 2 rows & 5 columns

import torch

# Create a 1D tensor
tensor = torch.arange(10)

# Convert the 1D tensor to a 2D tensor with 2 rows and 5 columns
tensor_2d = tensor.reshape(2, 5)

# Print the 2D tensor
print(tensor_2d)

