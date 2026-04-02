# This Python script was designed to illustrate the lecture of the BIO504
# module at UGA - L3 Biology
# It asks the user for the 2 sequences to compare
# Then displays the consensus sequence between them
# T. GAUTIER ®2020

# import required package
import re
print('This script displays the consensus motif between\ntwo character chains of similar sizes\nsimply aligned one under the other\nTG@2020-22')
def main():

    # Ask the user to enter the first sequence

    seq1 = input("What is the first sequence? (just hit return for default value: ADFGHYOP) ")
    # Ask the user to enter the second sequence
    seq2 = input("What is the second sequence? (just hit return for default value: ADEGHILP) ")
    # Prepare the memory space to store the consensus sequence
    consensus = []
    if seq1 =='':
        seq1 = 'ADFGHYOP'
    if seq2 =='':
        seq2 = 'ADEGHILP'
    # Test on the sequence length
    if len(seq1) <= len(seq2):
        length = len(seq1)
    else:
        length = len(seq2)
    # Ask the user the type of sequence to analyse
    letteru = input('Are your sequences proteic (just hit return for default value) or nucleotidic (type n)? ')
    letter = 'x'
    letteru = letteru.lower()
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    if letteru != '':
        letter = 'n'   
    # Beginning of the loop
    for i in range(length):
        #Test the equality of the letter at a specific position
        if seq1[i] == seq2[i]:
            consensus.append(seq1[i])
        else:
            consensus.append(letter)

    # Displaying the helping text
    print("The consensus sequence between",seq1,"and", seq2,"is :")
    # Formating the consensus sequence and displaying it
    print(''.join(consensus))

    # Asking the user for its choice
    choice = input('\nWould you like to perform another comparison? (y/n) ')
    print('\n')
    if choice == 'y':
        main()
    else:
        print('Ok, bye\n')
        quit()



# Part of code necessary to make the script fully python compliant

if __name__ == '__main__':
    main()
