#PBS -P nm31
#PBS -N getcpreads
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

cp $INFOLDER/cp-bbmap-filt.sam ./

cut -f1 cp-bbmap-filt.sam > cp.list

del-split.py cp.list cp-d.list "_part"


rsync -rut cp-d.list $INFOLDER/

get-seqs-para.py cp-d.list $READFILE cp-reads-filt.fasta 104

rsync -rut cp-reads-filt.fasta $INFOLDER/




