#!/usr/bin/env python3
from Bio import SeqIO
import os
import re
import glob
import sys
import numpy

#get n50 etc. details on all seqs in a folder (with specified extension).
#n50folder.py "folder/*.fasta"
#n50folder.py "assembly.fasta"



digits = re.compile(r'(\d+)')
def tokenize(filename):
    return tuple(int(token) if match else token
                 for token, match in
                 ((fragment, digits.search(fragment))
                  for fragment in digits.split(filename)))
				  


folder = sys.argv[1] #working folder

fmt = "fasta"

filelist=glob.glob(folder)

filelist.sort(key=tokenize)
print(filelist)
print("")
ml=max(len(w.split("/")[-1]) for w in filelist)

g=open("n50.txt",'a')

print("File"+(" "*(ml-4))+"\tCount\tTotal_bp\tMax\tMin\tN50\tL50\tN95\tL95\tMean")
g.write("File\tCount\tTotal_bp\tMax\tMin\tN50\tL50\tN95\tL95\tMean\n")

for f in filelist:

	seqs = SeqIO.index(f,fmt)
	if len(seqs)!=0:
		#get lengths and names
		data={}
		total=0
		t=0
		for i in seqs:
			t=t+1
			l1=len(seqs[i])
			
			total=total+l1
			data[i]=l1


		keylist=sorted(data,key=data.__getitem__)
		sizes=[]
		for p in keylist:
			sizes.append(data[p])
		
		min1= int(min(sizes))
		max1= int(max(sizes))
		ave=int(numpy.mean(sizes))
		
		c=0
		l2=0
		
		for k in reversed(keylist):
			c=c+1
			#print(data[k])
			l2=l2+int(data[k])
			
			if l2>=int(total)/2:
				
				n50=int(data[k])
				L50=c
				break
		
		c=0
		l2=0
		
		for k in reversed(keylist):
			c=c+1
			
			l2=l2+int(data[k])
			
			#print(data[k],l2)
			
			if l2>=int(total)*0.95:
				
				n95=int(data[k])
				L95=c
				break
		
	else:
		t=0
		total=0
		max1=0
		min1=0
		n50=0
		ave=0
	
	
	print(f.split("/")[-1]+"\t"+str(t)+"\t"+str(total)+"\t"+str(max1)+"\t"+str(min1)+"\t"+str(n50)+"\t"+str(L50)+"\t"+str(n95)+"\t"+str(L95)+"\t"+str(ave))
	
	g.write(f.split("/")[-1]+"\t"+str(t)+"\t"+str(total)+"\t"+str(max1)+"\t"+str(min1)+"\t"+str(n50)+"\t"+str(L50)+"\t"+str(n95)+"\t"+str(L95)+"\t"+str(ave)+"\n")



