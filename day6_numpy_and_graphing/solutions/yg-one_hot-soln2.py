#yulia solution to DNA_to_one-hot_heatmap 

import numpy as np 
import matplotlib.pyplot as plt 

dna_seq = input("Please type in a DNA sequence: ")
print(f"Your DNA sequence is: {dna_seq}") #taking user input DNA sequence 

#define a dictionary of bases to numbers, corresponsing to position in vector 
base_to_index = {'A':0, 
                 'C':1, 
                 'G':2,
                 'T':3}

#intialize numpy array that is rows x columns 
one_hot = np.zeros((len(dna_seq), 4))


#for every position in the range (0,length_of_dna)
for position in range(len(dna_seq)):
    current_base = dna_seq[position] #find what DNA bp is at that position in the string
    if current_base in base_to_index: #look for current base in the dictionary 
        one_hot[position, base_to_index[current_base]] = 1 #at the position in the array, update the value to be 1 
    else: #handles if non-canonical base 
        print(f"Current base {current_base} is not A,C,G,T") 
print(one_hot)
plt.imshow(one_hot, cmap='Set3') #use imshow to map values to colors 
plt.colorbar() #add color legend 
plt.title(f'One hot encoded DNA sequence: {dna_seq}')
plt.show()