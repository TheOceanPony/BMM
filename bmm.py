import pandas as pd
import numpy as np
from PIL import Image

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
