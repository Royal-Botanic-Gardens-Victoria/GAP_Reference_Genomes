#!/usr/bin/env python3

import sys
import glob
import re
import os
import subprocess as sp
#on VM run mfannot.sif on folder of files and convert.

def tokenize(filename):
	digits = re.compile(r'(\d+)')
	return tuple(int(token) if match else token for token, match in ((fragment, digits.search(fragment)) for fragment in digits.split(filename)))

def runmfannot():
	cwd=os.getcwd()
	print(cwd)
	
	for i in filelist:
		#f=open(i,'r')
		
		#rename contigs
		filename=i.rstrip("\n").split("/")[-1].split(".")
		filename=filename[0]+"."+filename[1]
		'''
		print(filename)
		p1=sp.Popen("mkdir -p rename",shell=True).wait()
		
		g1=open("rename/"+filename+".fasta",'w')
		
		for x in f:
			if x[0]==">":
				#remove length info
				if "ptg" in x[1:]:
					k=x[1:].rstrip("\n").split("ptg")[1].split("_")[0]
					k="ptg"+k
				
				if "tig" in x[1:]:
					k=x[1:].rstrip("\n").split("tig")[1].split("_")[0]
					k="tig"+k
					
				if "ptg" not in x and "tig" not in x:
					print(i,"not valid contig name",x)
					
				g1.write(f">{filename}_{k}\n")
				
			else:
				g1.write(x)
		'''
		
		#annotate
		p2=sp.Popen(f"singularity exec --bind {cwd} ~/bin/mfannot_latest.sif mfannot --cleanenv -o {outfolder}/{filename}.mf {i}",shell=True).wait()
		
		p3=sp.Popen(f"singularity exec --bind {cwd} ~/bin/agat.sif agat_convert_mfannot2gff.pl -m {outfolder}/{filename}.mf -o {outfolder}/{filename}.gff3",shell=True).wait()
		
		#p4=sp.Popen(f"rm ./{filename}.mf",shell=True).wait()
		
		p5=sp.Popen(f"sed -i '/orf/d' {outfolder}/{filename}.gff3",shell=True).wait()
		p6=sp.Popen(f"sed -i 's/exon/CDS/g' {outfolder}/{filename}.gff3",shell=True).wait()
		p7=sp.Popen(f"sed -i 's/mRNA/gene/g' {outfolder}/{filename}.gff3",shell=True).wait()
		p8=sp.Popen(f"sed -i 's/clpP_/clpP1_/g' {outfolder}/{filename}.gff3",shell=True).wait()
		p9=sp.Popen(f"sed -i 's/cob_/cob1_/g' {outfolder}/{filename}.gff3",shell=True).wait()
		p10=sp.Popen(f"sed -i 's/rpoC_/rpoC1_/g' {outfolder}/{filename}.gff3",shell=True).wait()
		p11=sp.Popen(f"sed -i '/rRNA/d' {outfolder}/{filename}.gff3",shell=True).wait()
		p12=sp.Popen(f"sed -i '/rrn/d' {outfolder}/{filename}.gff3",shell=True).wait()
		p12=sp.Popen(f"sed -i '/rn1/d' {outfolder}/{filename}.gff3",shell=True).wait()
		p12=sp.Popen(f"sed -i '/\t\t/d' {outfolder}/{filename}.gff3",shell=True).wait()
		p12=sp.Popen(f"sed -i '/dpo/d' {outfolder}/{filename}.gff3",shell=True).wait()

		p13=sp.Popen(f"barrnap --kingdom mito --threads 12 {i} > {outfolder}/{filename}.rrn",shell=True).wait()
		p14=sp.Popen(f"barrnap --kingdom euk --threads 12 {i} >> {outfolder}/{filename}.rrn",shell=True).wait()
		p15=sp.Popen(f"cat {outfolder}/{filename}.gff3 {outfolder}/{filename}.rrn > ./{filename}.gff3",shell=True).wait()
		p16=sp.Popen(f"mv ./{filename}.gff3 {outfolder}/{filename}.gff3 ",shell=True).wait()
		p17=sp.Popen(f"rm {outfolder}/{filename}.rrn ",shell=True).wait()

infolder=sys.argv[1]

outfolder=sys.argv[2]

p1=sp.Popen(f"mkdir -p {outfolder}",shell=True).wait()

filelist=glob.glob(infolder)

filelist.sort(key=tokenize)

runmfannot()


