# day3_python exercise solution: bl-transcriber.py

print("Here are the RNA sequences:")    # little message to print for users

# open the dna fasta file
with open("my_seq.fa", 'r') as f_in:

    # open a new file for the rna sequences
    with open("output_RNA_seq.fa", 'w') as f_out:

        # look through all the lines in the dna fasta file
        for line in f_in:

            # if it starts with '>', print it to the rna file (seq name)
            if line[0] == '>':
                f_out.write(line)   # write line to rna file

            # otherwise, it could be a sequence
            else:
                dna_seq = line.strip().upper()  # remove white spaces and put in upper case

                # look at each base in the dna sequence
                is_dna = True
                for base in dna_seq:

                    # if it's not a valid base, skip it 
                    if base not in ['A', 'G', 'C', 'T']:
                        is_dna = False

                # convert to rna and write/print the result
                if is_dna:
                    rna_seq = dna_seq.replace('T', 'U')
                    f_out.write(rna_seq + '\n')
                    print(rna_seq)

                # if invalid, say so
                else:
                    invalid_dna = dna_seq
                    f_out.write(f"INVALID ({dna_seq})")
                    print(f"INVALID ({dna_seq})")
