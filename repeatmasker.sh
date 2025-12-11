#PBS -N repeatmasker-elae
#PBS -P dy44
#PBS -q normalsr
#PBS -l walltime=24:00:00
#PBS -l ncpus=48
#PBS -l mem=300GB
#PBS -l jobfs=14GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44

#Example for Elaeocarpus

RepeatMasker -pa 12 -dir repeats -lib /g/data/dy44/r12.42_Elaeocarpus_repeat/repeats/Elae_rpts-families.fa /g/data/dy44/r12.42_Elaeocarpus_repeat/purge/Elaeocarpus_purged_rpt.fasta
