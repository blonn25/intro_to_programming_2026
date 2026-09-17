# day6_numpy_and_graphing exercise solution: bl-one_hot.py

import numpy as np 
import matplotlib.pyplot as plt 

dna_seq = input("Please type in a DNA sequence: ")
print(f"Your DNA sequence is: {dna_seq}") # prints user's DNA sequence

#define a dictionary of bases to one hot vectors
base_to_one_hot = {'A': [1, 0, 0, 0],
                   'C': [0, 1, 0, 0],
                   'G': [0, 0, 1, 0],
                   'T': [0, 0, 0, 1]}

# init a list to store the full sequence encoding
seq_encoding = []

# iterate through the bases and update the sequence encoding
for base in dna_seq:
    one_hot = base_to_one_hot[base]
    seq_encoding.append(one_hot)

# convert sequence encoding to an array
seq_encoding_array = np.array(seq_encoding)

print(seq_encoding_array)
plt.imshow(seq_encoding_array, cmap='magmaß') #use imshow to map values to colors 
plt.colorbar() #add color legend 
plt.title(f'One hot encoded DNA sequence: {dna_seq}')
plt.show()