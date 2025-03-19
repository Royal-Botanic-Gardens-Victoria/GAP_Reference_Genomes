#PBS -P dy44
#PBS -N genome-hifiasm
#PBS -q normalsr
#PBS -l walltime=48:00:00
#PBS -l ncpus=104
#PBS -l mem=500GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


mkdir -p hifiasm-herro

cd $PBS_JOBFS

#hifiasm

OUTNAME=genome_name

cp $PBS_O_WORKDIR/herro.fasta ./

hifiasm --lowQ 0 -o $OUTNAME -t 104 reads.fasta

awk '/^S/{print ">"$2;print $3}' $OUTNAME.bp.p_ctg.gfa > $OUTNAME'_assembly.fasta'

rm *noseq* *.bin

rsync -rut * $PBS_O_WORKDIR/hifiasm-herro/


