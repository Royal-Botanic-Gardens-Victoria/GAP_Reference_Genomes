#!/usr/bin/env python3

#theo allnutt 2024

#r12.24 get kmer counts along contig lengths

#kmer-by-length.py ../themeda_scaf_norpts.fasta 21 1024 10000

#kmer-by-length.py infile kmerlen window_length_for_measurement length_to_bin

import sys
import os
import re
import glob
from Bio import SeqIO
import gzip
import math
import collections
import statistics as stats


def tokenize(filename):
	digits = re.compile(r'(\d+)')
	return tuple(int(token) if match else token for token, match in ((fragment, digits.search(fragment)) for fragment in digits.split(filename)))



def kmercount(dna_sequence,wordsize):
	
	wordsizeint=int(wordsize)
	kmers=[]
	seqlen=float(len(dna_sequence))
	wordsize=float(wordsize)
	
	dna_sequence=dna_sequence.replace("\n","")
	
	#n.b. this posscount is modelled for shorter sequences where b^len count is not true
	posscount=float((4**wordsize)*(1-math.exp(-(1/(4**wordsize))*seqlen)))
	
	#use infinate len seq posscount
	#posscount=4**wordsize
	
	#print(posscount)
	for x in range(len(dna_sequence)-wordsizeint):
		
		kbit=dna_sequence[x:x+wordsizeint]
		if "N" not in kbit:
			
		#if kbit not in kmers:
			#print(x,kbit)
			kmers.append(kbit) #also try if to test before set see which is faster: 
		
		#if len(kmers)>=posscount:
			#break
	kmers=set(kmers)
	
	kratio=float(len(kmers)/posscount)
	#kratio is ratio of kmer count to maximum possilbe count for the sequence length
	return (len(kmers),kratio)
		

def kmerbylength(i):

	g.write("contig\tbp\tkmer_count\tkmer_ratio\n")
	
	
	for x in SeqIO.parse(i,'fasta'):
	
		print(x.id)
		c=0
		
		seqlen=len(x.seq)
		

			
		for y in range(0,seqlen,binlength):
			
			binkc=[]
			binkr=[]
			
			if y+binlength > seqlen:
				seqbin=x.seq[y:]
				
			else:
				seqbin=x.seq[y:y+binlength]
			
			binlen=len(seqbin)
			
			#print(y,y+binlength)
			
			for z in range(0,binlen,sample):
				
				if z+sample>binlen:
					kseq=seqbin[z:]
				else:
					kseq=seqbin[z:z+sample]
					
				binkr.append(1-kmercount(kseq,wordn)[1])
				binkc.append(kmercount(kseq,wordn)[0])
			
				#print(binkc)
				
				#input()
			
			mkr=stats.mean(binkr)
			
			if mkr > 0.9:
				g2.write(">"+i.id+"_"+str(mkr))+"_"+str(y)+"-"+str(y+binlen)+"\n"+str(kseq)+"\n")
				
				
			g.write(str(x.id)+"\t"+str(y)+"\t"+str(stats.mean(binkc))+"\t"+str(mkr)+"\n")
			
			
			
			#print(len(binkr),len(kseq),str(x.id)+"\t"+str(y)+"\t"+str(stats.mean(binkc))+"\t"+str(stats.mean(binkr)))
		
		




#global

f=open(sys.argv[1],'r')

g = open(sys.argv[1].split("/")[-1]+".kmers",'w')

g2=open("very_rpt.fasta",'w')

wordn=int(sys.argv[2])
sample=int(sys.argv[3])
binlength=int(sys.argv[4])

kmerbylength(f)




