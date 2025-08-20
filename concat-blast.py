#!/usr/bin/env python3

#from R02.4 concatenate tandem numpts - can be used for any tandem or overlappiing blast hits


import sys
import subprocess as sp

def concat_hits(f2):

	print("Reading blast")
	for i in f2: 
		
		k=i.rstrip("\n").split("\t")
		
		id1=k[-1]
		contig=k[contigpos]
		x=int(k[startpos])
		y=int(k[endpos])
		if x<y:
			start=x
			end=y
		else:
			start=y
			end=x
			
		pid=float(k[2])
		
		internalsw=0
		
		if contig not in contigs.keys():
			
			k3=i.rstrip("\n").split("\t")
			k3[startpos]=start
			k3[endpos]=end
			newi="\t".join(str(p) for p in k3)+"\n"
			
			contigs[contig]=[(start,end,pid,newi)]
			
		else:
			#check if identical
			if start==contigs[contig][-1][0] and end==contigs[contig][-1][1]:
				newpid=(contigs[contig][-1][2]+pid)/2

				k2=contigs[contig][-1][3].split("\t")
			
				k2[2]=newpid
				k2[-1]=k2[-1].rstrip("\n")+";"+id1+"_identical"
				
				newi="\t".join(str(p) for p in k2)+"\n"
				
				contigs[contig][-1]=(start,end,newpid,newi)
			#not identical
			else:
				if start< contigs[contig][-1][1]+overlap:#catenate
					
					newstart=contigs[contig][-1][0] #file sorted by start so cannot be less than current start
					
					if end>contigs[contig][-1][1]: #if internal numpt, use existing end
						newend=end
						internalsw=0
					else:
						newend=contigs[contig][-1][1] # internal
						internalsw=1
					#weight pid by lengths
					len1=float((contigs[contig][-1][1])-(contigs[contig][-1][0]))
					len2=float(end-start)
					
					newpid=((contigs[contig][-1][2]*len1)+(pid*len2))/(len1 + len2)
					
					#print(contigs[contig][-1][1],contigs[contig][-1][0],start,end,contigs[contig][-1][2],len1,pid,len2)
					
					k2=contigs[contig][-1][3].split("\t")
						
					k2[startpos]=newstart
					k2[endpos]=newend
					
					k2[3]=len1 + len2
					k2[2]=newpid
					k2[-1]=k2[-1].rstrip("\n")+";"+id1
					if internalsw==1:
						k2[-1]=k2[-1]+"_internal"
					
					newi="\t".join(str(p) for p in k2)+"\n"
					
					contigs[contig][-1]=(newstart,newend,newpid,newi)
				else:#don't catenate
					contigs[contig].append((start,end,pid,i))

def sort_blast(f):

	name1=f+".sorted"
	ck=contigpos+1
	ck=str(ck)
	p0=sp.Popen(f"sort -t$'\t' -k{ck},{ck} -k{startpos+1},{startpos+1}n {infile}>{infile}.sorted",shell=True).wait()
	
#global

infile = sys.argv[1] #input blast
g = open(sys.argv[2],'w') #out blast

overlap = int(sys.argv[3]) #allowed bp of space between hits before being merged

contigpos=int(sys.argv[4]) #blast contig column - zero numbered
startpos=int(sys.argv[5]) 
endpos=int(sys.argv[6])


contigs={}
concats={}

sort_blast(infile)

f2=open(infile+".sorted",'r')

concat_hits(f2)


#write data
for x in contigs.keys():

	for y in contigs[x]:
	
		g.write(y[3])
		
g.close()

print("done")	
		
		
		
		