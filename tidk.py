#!/usr/bin/env python3

#Theo Allnutt 2023
#r12
#run tidk to find telomeres on single or multiple files.

import sys
import os
import re
import glob
import subprocess as sp
import concurrent.futures
from Bio import SeqIO

#alphanumeric human sort
def tokenize(filename):
	digits = re.compile(r'(\d+)')
	return tuple(int(token) if match else token for token, match in ((fragment, digits.search(fragment)) for fragment in digits.split(filename)))

def tidkrun(i):
	
	print(i)
	
	name1=i.split("/")[-1].split(".")[0]
	
	 

	
	
	p1=sp.Popen(f"tidk explore -d {oufolder} -o {name1} -m 5 -x 24 -t {threads} -e tsv --distance 100000 {i}",shell=True).wait()
	
	f1=open(f"{outfolder}/{name1}.txt","r")
	f1.readline()#header
	motif=f1.readline().split("\t")[0]
	f1.close()
	
	p2=sp.Popen(f"tidk search -s {motif} -d {outfolder} -e tsv -o {name1} -w 10000 {i}",shell=True).wait()

def get_telomeres(i):

	


#global
infolder=sys.argv[1]

outfolder=sys.argv[2]

threads =int(sys.argv[3])

reps = int(sys.argv[4])
	
filelist=glob.glob(infolder)
filelist.sort(key=tokenize)

print(filelist)

p0=sp.Popen(f{mkdir -p {outfolder},shell=True).wait()

if __name__ == '__main__':
	
	executor = concurrent.futures.ProcessPoolExecutor(reps)
	futures = [executor.submit(tidkrun, i) for i in filelist]
	concurrent.futures.wait(futures)
	
	filelist2=glob.glob(outfolder+"/*_repeat_windows.tsv")
	
	filelist2.sort(key=tokenize)
	
	print(filelist2)
	
	for i in filelist2:
	
		get_telomeres(i)

		