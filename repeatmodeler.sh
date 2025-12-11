#PBS -N elae-repeatmodeler
#PBS -P dy44
#PBS -q normalsr
#PBS -l walltime=48:00:00
#PBS -l ncpus=48
#PBS -l mem=300GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


#example for Elaeocarpus

mkdir -p repeats

cd $PBS_JOBFS

module load RepeatModeler


BuildDatabase -name repeats/Elae_rpts /g/data/dy44/r12.42_Elaeocarpus_repeat/purge/Elaeocarpus_purged_rpt.fasta

RepeatModeler -threads 48 -database /g/data/dy44/r12.42_Elaeocarpus_repeat/repeats/Elae_rpts 

rsync -rut * /g/data/dy44/r12.42_Elaeocarpus_repeat/repeats/