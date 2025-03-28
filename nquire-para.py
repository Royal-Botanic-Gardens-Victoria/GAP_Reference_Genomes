#!/usr/bin/env python3

import sys
import concurrent.futures
import subprocess as sp
import glob
import re



def tokenize(filename):
	digits = re.compile(r'(\d+)')
	return tuple(int(token) if match else token for token, match in ((fragment, digits.search(fragment)) for fragment in digits.split(filename)))

def nquire(bam):

	print(bam)
	
	outfile=outfolder+"/"+bam.split("/")[-1]
	
	p0=sp.Popen(f"nQuire create -b {bam} -o {outfile} -x",shell=True).wait()
	
	p1=sp.Popen(f"nQuire histo {outfile}.bin > {outfile}.histo",shell=True).wait()
	
	p2=sp.Popen(f"nQuire denoise {outfile}.bin -o {outfile}.denoised",shell=True).wait()
	
	p3=sp.Popen(f"nQuire histo {outfile}.denoised.bin > {outfile}.denoised.histo",shell=True).wait()
	
	p4=sp.Popen(f"nQuire lrdmodel {outfile}.denoised.bin > {outfile}.model",shell=True).wait()
	
	p5=sp.Popen(f"nQuire histotest {outfile}.denoised.bin > {outfile}.test",shell=True).wait()
	
	
	
infolder=sys.argv[1]

filelist= glob.glob(infolder)

filelist.sort(key=tokenize)

print(filelist)

outfolder=sys.argv[2]

threads=int(sys.argv[3])

executor1 = concurrent.futures.ProcessPoolExecutor(threads)
futures1 = [executor1.submit(nquire,i) for i in filelist]
concurrent.futures.wait(futures1)

#for i in filelist:

	#nquire(i)