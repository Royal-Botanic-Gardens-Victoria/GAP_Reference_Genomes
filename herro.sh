#!/bin/bash 
#PBS -P dy44
#PBS -N dorado-herro
#PBS -q gpuvolta
#PBS -l ncpus=48
#PBS -l ngpus=4
#PBS -l walltime=48:00:00
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44
#PBS -l mem=382G
#PBS -l jobfs=400G
#PBS -l wd

module load cuda


cd $PBS_JOBFS

cp $PBS_O_WORKDIR/ont-filt.fastq ./

cp -r /g/data/nm31/bin/dorado-0.7.2-linux-x64/herro-v1/ ./herro-v1

dorado correct -t 48 --infer-threads 6 -m herro-v1 ont-filt.fastq  > $PBS_O_WORKDIR/herro.fasta



