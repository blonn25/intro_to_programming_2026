#yulia solution to translator.py 

genetic_code = {
    'AUG': 'M', 
    'UUU': 'F', 'UUC': 'F',
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'UAU': 'Y', 'UAC': 'Y',
    'CAU': 'H', 'CAC': 'H',
    'CAA': 'Q', 'CAG': 'Q',
    'AAU': 'N', 'AAC': 'N',
    'AAA': 'K', 'AAG': 'K',
    'GAU': 'D', 'GAC': 'D',
    'GAA': 'E', 'GAG': 'E',
    'UGU': 'C', 'UGC': 'C',
    'UGG': 'W',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
}

def get_sequence(path:str): 
    """
    Gets DNA sequence from a FASTA file. 
    
    Args: 
    path (str): defines where the fasta file with sequence is located 
    
    Returns:
    sequence (str): DNA sequence from FASTA file
    
    """
    
    with open(path, 'r') as file: 
        content = file.readlines()
        seq = content[1]
        return seq
    
    #alternatively - if you have a list of fasta sequences - you can select all of the lines that don't start with > and add them to a list of sequences. 
    # list_of_seq = []
    # with open(path, 'r') as file: 
    #     content = file.readlines()
    #     for line in content: 
    #         if not line.startswith('>'): 
    #             list_of_seq.append(line)
    # return list_of_seq[0]

def DNA_to_RNA(dna_sequence): 
    """
    Transcribes DNA sequence into RNA. Replaces T with U.  
    
    Args: 
    dna_sequence (str): DNA sequence  
    
    Returns:
    rna_seq (str): RNA sequence 
    
    """
    rna_seq = dna_sequence.replace('T', 'U')
    return rna_seq

def RNA_to_AA(rna_seq): 
    """
    Translates RNA sequence into amino acid sequence. 
    
    Args: 
    rna_seq (str): RNA sequence 
    
    Returns: 
    aa_seq (str): Amino acid sequence 
    """
    aa_seq=''
    start_position = 0
    while start_position < len(rna_seq):
        working_codon = rna_seq[start_position:start_position+3]
        aa_to_add = genetic_code[working_codon]
        aa_seq+=aa_to_add
        start_position += 3
    return aa_seq  
            
input_path = input("Where is the path to the DNA seuqence file? " ) #get path from terminal prompt
dna_seq = get_sequence(input_path) #get dna sequence from input_path using get_sequence 
rna_seq = DNA_to_RNA(dna_seq) #get rna sequence from dna_seq using DNA_to_RNA
aa_seq = RNA_to_AA(rna_seq) #get aa sequence from rna_seq using RNA_to_AA 
print(aa_seq) #print aa_seq to the terminal 


