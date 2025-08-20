#!/usr/bin/env python3

import sys
from Bio import SeqIO
import re

#get proportion of stuff in contig from bed file r12

digits = re.compile(r'(\d+)')
def tokenize(filename):
    return tuple(int(token) if match else token
                 for token, match in
                 ((fragment, digits.search(fragment))
                  for fragment in digits.split(filename)))


def sizes(infile):
	data={}

	f=open(infile,'r')

	for x in SeqIO.parse(f,'fasta'):
		
		data[x.id]=len(x.seq)

	return data

def propstuff(bedfile,contigs):

	bedcontigs={}
	
	
	for x in bedfile:
	
		contig=x.split("\t")[0]
		
		st=int(x.split("\t")[1])
		en=int(x.split("\t")[2])
		z=int(0)
		
		if st>en:
			z=st
			st=en
			en=z
		c=en-st
		
		if contig not in bedcontigs.keys():
			
			bedcontigs[contig]=[c]
			
		else:
			bedcontigs[contig].append(c)
			
	
	
	print(contigs)
	print(bedcontigs)
	
	g.write("contig\tfeature_propn\tfeature_len\tfeature_num\tcontig_len\n")
	
	for x in contigs:
		
		if x in bedcontigs.keys():
			hitlen=sum(bedcontigs[x])
			hitnum=len(bedcontigs[x])
			print(x,bedcontigs[x],contigs[x])
			p=float(hitlen/contigs[x])
			
			g.write(x+"\t"+str(p)+"\t"+str(hitlen)+"\t"+str(hitnum)+"\t"+str(contigs[x])+"\n")
		else:
			g.write(x+"\t0\t0\t0\t"+str(contigs[x])+"\n")
			

contigfile=sys.argv[1]

bedfile=open(sys.argv[2],'r')

g=open(sys.argv[3],'w')

contigs=sizes(contigfile)

propstuff(bedfile,contigs)
