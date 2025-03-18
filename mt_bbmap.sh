#PBS -N \mtbbmap
#PBS -P dy44
#PBS -q normalsr
#PBS -l walltime=12:00:00
#PBS -l ncpus=104
#PBS -l mem=256GB
#PBS -l jobfs=256GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


MTREF=/g/data/nm31/db/mt-ref.fasta

reads=/g/data/dy44/r12.15_Gastrolobium/herro-dedup.fasta



cd $PBS_JOBFS 

#bbmap Version 39.01

mapPacBio.sh ref=$MTREF ambig=best nodisk=t nzo=t mappedonly=t minid=0.90 out=mt-bbmap.sam in=$reads fastareadlen=6000 threads=104 maxindel=100 k=15

sam-length.py mt-bbmap.sam mt-bbmap-filt.sam 1000 100

rsync -rut mt-bbmap-filt.sam $PBS_O_WORKDIR

