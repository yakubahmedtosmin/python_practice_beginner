import math
def pssm():
    n=int(input("Enter the no of sequence: "))
    s=[[""]for i in range (n)]
    for i in range(n):
        s[i]=input("Enter the sequene: ")
    print("Entered sequences are:")
    for i in range(n):
        print(s[i])

    p="ARNDCEQZGHILMFPSTWYV"
    s1=s[0]
    l=len(s1)
    sc=[[0.0 for i in range(l*4)] for j in range(len(p)*4)]
    print("The length of the sequence is :",l)
    for i in range(l):
        for j in range(len(p)):
            m=1
            for k in range(n):
                if(p[j]==s[k][i]):
                    m=m+1
            v=m/(20+n)
            sc[i][j]=(math.log(v/0.05))/math.log(10)

    print("The scoring matrix is: ")
    for i in range(len(p)):
        print("  ",p[i],end="    ")
    print("\n")
    for i in range(l):
        print(i+1,":",end="")
        for j in range (len(p)):
            print('%2.3f'%sc[i][j],end="  ")
        print("\n")
