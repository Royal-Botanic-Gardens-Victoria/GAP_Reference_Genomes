#PBS -P dy44
#PBS -N bell-hifiasm
#PBS -q normalsr
#PBS -l walltime=48:00:00
#PBS -l ncpus=104
#PBS -l mem=392GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


outfolder=hifiasm-ont
OUTNAME=bell

mkdir -p $outfolder



cd $PBS_JOBFS


hifiasm --lowQ 0 -o $OUTNAME -t 104 --ul-rate 0.06 --ul /g/data/dy44/r12.23_Bellendena/ont.fasta /g/data/dy44/r12.23_Bellendena/hifi2good.fasta

awk '/^S/{print ">"$2;print $3}' $OUTNAME.bp.p_ctg.gfa > $OUTNAME'_assembly.fasta'

rm *noseq*

rsync -rut *_assembly.fasta *.gfa $PBS_O_WORKDIR/$outfolder/
