#PBS -P dy44
#PBS -N chopper
#PBS -q normalsr
#PBS -l walltime=4:00:00
#PBS -l ncpus=48
#PBS -l mem=300GB
#PBS -l jobfs=4GB
#PBS -l wd
#PBS -l storage=gdata/if89+gdata/nm31+scratch/nm31+gdata/dy44+scratch/dy44


mkdir -p ont-filt

chopper.py "$PBS_O_WORKDIR/ont-dorado.fastq" $PBS_O_WORKDIR/ont-filt/ 5000 12 48

mv ont-filt/ont-dorado.fastq ont-filt.fastq

