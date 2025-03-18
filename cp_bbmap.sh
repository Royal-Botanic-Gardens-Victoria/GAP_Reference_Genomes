#PBS -N cpbbmap
#PBS -P dy44
#PBS -q normalsr
#PBS -l walltime=8:00:00
#PBS -l ncpus=104
#PBS -l mem=256GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


CPREF=/g/data/nm31/db/cp-refseq-nomt.fasta

reads=$PBS_O_WORKDIR/reads.fasta



cd $PBS_JOBFS 

#bbmap Version 39.01

mapPacBio.sh ref=$CPREF ambig=best nodisk=t nzo=t mappedonly=t minid=0.90 out=cp-bbmap.sam in=$reads fastareadlen=6000 threads=104 maxindel=100 k=15

sam-length.py cp-bbmap.sam cp-bbmap-filt.sam 1000 100

rsync -rut cp-bbmap-filt.sam $PBS_O_WORKDIR

