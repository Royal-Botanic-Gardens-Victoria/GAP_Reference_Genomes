#!/usr/bin/env python3

#r12
# to get telomere peaks

import sys
import os
import re
import glob
import subprocess as sp
from scipy import signal as sig
import concurrent.futures

#tidk explore -d ./ -o Call-unfilt -m 5 -x 24 -t 48 -e tsv /g/data/dy44/pre-purge-assemblies/Callicoma_assembly.fasta
#tidk search -s TTTAGGG -d ./ -e tsv -o Callunfilt-TTTAGGG -w 50000 /g/data/dy44/pre-purge-assemblies/Callicoma_assembly.fasta
#count-telomeres.py "Call-TTTAGGG_telomeric_repeat_windows.tsv" Call-TTTAGGG.txt 50000 12

#alphanumeric human sort
def tokenize(filename):
	digits = re.compile(r'(\d+)')
	return tuple(int(token) if match else token for token, match in ((fragment, digits.search(fragment)) for fragment in digits.split(filename)))

def telo(i):
	print(i)
	f=open(i,'r')

	name1=i.split("/")[-1].split("_telo")[0]
	data={}
	contigs=[]
	
	for x in f:
	
		motifs=0
	
		if x[:2]!="id":#check no header in cat file of multiple telo motifs n.b. multiple motifs removed so this not really needed
			
			k=x.rstrip("\n").split("\t")
			rptcount=int(k[2])+int(k[3])
			contig=k[0]
			
			contigbin=int(k[1])
			
			if contig not in data.keys():
				
				data[contig]={}
				
				if contigbin not in data[contig].keys():
					data[contig][contigbin]=rptcount
				else:
					data[contig][contigbin]=data[contig][contigbin]+rptcount
				
			else:
				if contigbin not in data[contig].keys():
					data[contig][contigbin]=rptcount
				else:
					data[contig][contigbin]=data[contig][contigbin]+rptcount
		else:
		
			motifs=motifs+1

			
	contigs2=[]
	for x1 in data.keys():
		contigs2.append(x1)
		
	contigs2.sort(key=tokenize)
	
	#print(contigs)
	
	startpeaks=0
	endpeaks=0
	bothpeaks=0
	unkpeaks=0
	nopeaks=0
	midpeaks=0
	
	startpeak=[]
	endpeak=[]
	bothpeak=[]
	midpeak=[]
	
	summary=open(f"{name1}_all_telomere_peaks.txt",'w')
	
	for c in contigs2:
		midpeaks=0
		peakdata=[]
		
		contigbins=[]
		
		#print(c)
		
		for p in data[c].keys():
			contigbins.append(p)
			
		contigbins.sort()
		
		for y in contigbins:
			peakdata.append(data[c][y])
	
		
		m=min(peakdata)
		peakdata=[m]+peakdata+[m]
		
		#print(c,peakdata)
		
		peaks=sig.find_peaks(peakdata,prominence=100)
		
		print(c,peaks[0])
		
		if len(peaks[0])!=0:
			print(peakdata)
			peakslist=[]
			for z in peaks[0]:
				v=float((z-1)/(len(peakdata)-2))
				peakslist.append(v)#list of peaks' position as float
				print(name1,c,v) #give position of peak(s) in array...
				summary.write(name1+"\t"+c+"\t"+str(v)+"\n")
				if v>0.1 and v<0.9:
					print("midpeak",v)
					midpeaks=midpeaks+1
			
			if midpeaks>0:
				midpeak.append(c)
			
			summary.write(f"{c}\tmidpeaks\t{str(midpeaks)}\n")
			
			if max(peakslist)>=0.9 and min(peakslist)<=0.1:
				bothpeaks=bothpeaks+1
				summary.write(f"{c}\tboth telo\n")
				bothpeak.append(c)
				
			else:
				
				if max(peakslist)>=0.9:
					endpeaks=endpeaks+1
					summary.write(f"{c}\tend telo\n")
					endpeak.append(c)
				if min(peakslist)<=0.1:
					startpeaks=startpeaks+1
					summary.write(f"{c}\tstart telo\n")
					startpeak.append(c)
		else:
			#print(name1, c, "no peaks")
			nopeaks=nopeaks+1
			summary.write(f"{c}\tno telo\n")
	
		
	summary.close()
	
	m=",".join(str(p) for p in midpeak)
	s=",".join(str(p) for p in startpeak)
	e=",".join(str(p) for p in endpeak)
	b=",".join(str(p) for p in bothpeak)
	
	
	outfile.write(name1+"\t"+str(nopeaks)+"\t"+str(len(midpeak))+"\t"+str(startpeaks)+"\t"+str(endpeaks)+"\t"+str(bothpeaks)+"\t"+m+"\t"+s+"\t"+e+"\t"+b+"\n")
	
	
infolder=sys.argv[1]

filelist= glob.glob(infolder)

filelist.sort(key=tokenize)

#print(filelist)

outfile=open(sys.argv[2],'w')

outfile.write("Genome\tNone\tMid\tStart\tEnd\tboth\tmid\tstart\tend\tboth\n")

binsize=int(sys.argv[3])

threads=int(sys.argv[4])

#executor1 = concurrent.futures.ProcessPoolExecutor(threads)
#futures1 = [executor1.submit(telo,i) for i in filelist]
#concurrent.futures.wait(futures1)

for i in filelist:

	telo(i)