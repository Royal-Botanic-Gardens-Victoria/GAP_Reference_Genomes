#PBS -P dy44
#PBS -N compleasm
#PBS -q normal
#PBS -l walltime=4:00:00
#PBS -l ncpus=48
#PBS -l mem=190GB
#PBS -l jobfs=164GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44


module load hmmer


cd $PBS_JOBFS


compleasm.py run -a /g/data/dy44/r12.21_Eucryphia/hifiasm-herro/eucr_assembly.fasta -o compleasm/ -t 48 -l embryophyta -L /g/data/nm31/db/mb_downloads

rm -r compleasm/embryophyta_odb10

rsync -rut * $PBS_O_WORKDIR

