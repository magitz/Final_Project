#where code I am working on will go

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

gene = input("enter gene of interest")

def get_gene(): 
    open('query_fastas.txt','w') 
    for name in ids:
        if(name == gene):
            print(name) 
        else: print('could not find gene')


