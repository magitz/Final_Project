#another idea for incorporating if statement

from Bio import Entrez, SeqIO
Entrez.email = 'mcullen1@ufl.edu'

#prompt user for organism and number of results desired 
query= input('Enter organism name')
usermax=input('Enter maximum number of results ')

#send query to Entrez nucleotide database 
handle = Entrez.esearch(db='nucleotide', term = query, field='organism', retmax=usermax)
record = Entrez.read(handle) 
handle.close()

#get the 'IDList' field from the results 
ids=(record["IdList"]) 
print(ids) #optional

#function to get sequences from the genbank IDs returned from the search and write to 'query_fastas.txt' 
def get_sequences():
    open('query_fastas.txt','w') 
    for seq_id in ids:
        handle = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text",retmax=1) 
        local_file=open('query_fastas.txt','a')
        local_file.write(handle.read())
get_sequences() 
handle.close()

####attempt to incorporate if statement

fhand = open('query_fastas.txt')

print(fhand)

gene = input("Enter gene of interest: ")

for line in fhand:
    line = line.rstrip()
    fields = line.split(" ")
    if fields[0] == gene:
        print(fields[30])
    else:
        print("Gene not found :(")
