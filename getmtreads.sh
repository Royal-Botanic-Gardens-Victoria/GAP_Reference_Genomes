#PBS -P dy44
#PBS -N getmtreads
#PBS -q normalsr
#PBS -l walltime=1:00:00
#PBS -l ncpus=104
#PBS -l mem=256GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44



cd $PBS_JOBFS

#input file must be called reads.fasta and seqs be on one line

INFOLDER=$PBS_O_WORKDIR

READFILE=reads.fasta

cp $PBS_O_WORKDIR/$READFILE ./

cp $INFOLDER/mt-bbmap-filt.sam ./

cut -f1 mt-bbmap-filt.sam > mt.list

del-split.py mt.list mt-d.list "_part"


rsync -rut mt-d.list $INFOLDER/

get-seqs-para.py mt-d.list $READFILE mt-reads-filt.fasta 104

rsync -rut mt-reads-filt.fasta $INFOLDER/




