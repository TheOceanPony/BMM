import pandas as pd
import numpy as np
from PIL import Image


def get_random_probs(ds_size, clusters_amount):
    rand_matrix = np.random.randint(
      low=0,
      high=5000,
      size=(ds_size, clusters_amount))
    
    sum_along_row = np.repeat(
      rand_matrix.sum(axis=1).reshape((-1, 1)),
      repeats=2,
      axis=1)
    
    prob_matrix = rand_matrix/sum_along_row
    return prob_matrix
  
  

# Loading the data
df = pd.read_csv("dataset/ds81.csv")
N = df.shape[0]

# Creating an "album"
album = np.zeros((N, 28, 28))
for i in range(0, N):
  temp = np.reshape( df[i:i+1].to_numpy(), (-1, 28))
  temp = (temp>127).astype(np.uint8)
  album[i] = temp
  
  
  
im = Image.fromarray(np.uint8(p[1] * 255) , 'L')
im.show()

im = Image.fromarray(np.uint8(p[0] * 255) , 'L')
im.show()
