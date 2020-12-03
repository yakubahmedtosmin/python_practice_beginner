# needleman-wunsch algorithm:
import numpy as np

seq1 = "ATGCTGTACAGCTGCATG"
seq2 = "AGCTGATCACTAGCTAGC"

#matrices
main =np.zeros((len(seq1)+1, len(seq2)+1))
matching = np.zeros((len(seq1), len(seq2)))

#score
match_s = 1
mismatch = -1
gap = -2

# fill thae macthing matrix
for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq1[i] == seq2[j]:
            matching[i][j] = match_s
        else:
            matching[i][j] = mismatch
#print(matching)
#fill the main matrix
for i in range(len(seq1)+1):
    main[i][0] = i*gap
for j in range(len(seq2)+1):
    main[0][j] =j*gap
#print(main)
#matrix filling
for i in range(1, len(seq1)+1):
    for j in range(1, len(seq2)+1):
        main[i][j] = max(main[i-1][j-1]+matching[i-1][j-1],
                         main[i-1][j]+gap,
                         main[i][j-1]+gap)
# traceback
alin1 = ""
alin2 = ""

n1 = len(seq1)
n2 = len(seq2)

while (n1>0 and n2>0):
    if (n1>0 and n2>0 and main[n1][n2]==main[n1-1][n2-1]+matching[n1-1][n2-1]):
        alin1 = seq1[n1-1]+alin1
        alin2 = seq2[n2-1]+alin2
        
        n1 = n1-1
        n2=  n2-1
    
    elif (n1>0 and main[n1][n2] == main[n1-1][n2]+gap):
        alin1 = seq1[n1-1]+alin1
        alin2 = "-" +alin2
        
        n1 = n1-1
    
    else:
        alin1 = "-"+alin1
        alin2 = seq2[n2-1]+alin2
        
        n2 = n2-1
print(alin1)
print(alin2)
