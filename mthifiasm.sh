#PBS -N mthifiasm
#PBS -P dy44 
#PBS -q normalsr 
#PBS -l walltime=2:00:00
#PBS -l ncpus=48
#PBS -l mem=190GB
#PBS -l jobfs=200GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


cd $PBS_JOBFS

hifiasm -o mt --n-hap 1 --lowQ 0 -t 48 $PBS_O_WORKDIR/mt-assembly/mtreads.fasta

rm *.bin *noseq*

awk '/^S/{print ">"$2;print $3}' mt.bp.p_ctg.gfa > mt-assembly.fasta

rsync -rut * $PBS_O_WORKDIR/mt-assembly
