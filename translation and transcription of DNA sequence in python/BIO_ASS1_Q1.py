from itertools import permutations 
flag=0

f = open('/home/talha/Documents/tarfile.txt')
for W in f:
    seq=W
    
f.close() 


def translate_dna(sequence):
    gencode = { 'ATA':'I',
    'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T',
    'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S',
    'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L',
    'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R',
    'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A',
    'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E',
    'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S',
    'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'', 'TGC':'C',
    'TGT':'C', 'TGA':'S', 'TGG':'T', }
    #print sequence
    proteinseq = ''

    for n in range(0,len(sequence),3):
        if gencode.has_key(sequence[n:n+3]) == True:
            proteinseq += gencode[sequence[n:n+3]]
    print 'PROTEIN SEQUENCE:',proteinseq    




def delete_intron(intrn,seq_list):
    LIST=[]
    global flag
    global seq
    if flag==0:
        j=seq.split(intrn)
        flag=flag+1
        return j
    #print "j: ", j
    for i in seq_list:
        K=i.split(intrn)
        LIST.append(K)

    lsst = []
    #print "LIST: ", LIST


    for i in LIST:
        for r in i:
            lsst.append(r)
    #print 'lst: ', lsst
    return lsst
  
   
    
t = ''
lst=[]
list_full=[]
while t!="STOP":
    t = raw_input("enter intron sequences :for stop enter (STOP)")
    if t!="STOP":
        lst.append(t)
for s in lst:
    list_full=delete_intron(s,list_full)

    
    
leng=len(list_full)
original = list_full[leng-1]
strr=""
for i in range(0,len(original)-1):
    strr=strr+original[i]
del list_full[leng-1]
list_full.append(strr)
print 'LISTAA IS HERE :',list_full
mRNA=[]    



perm=permutations(list_full)
final_seq_list=[]
temp=''
for p in perm:
    #print p
    for o in range(0,len(p)):
        temp=temp+p[o]
    mRNA.append(temp)
    temp=""
    
for s in range(0,len(mRNA)):
    translate_dna(mRNA[s])

