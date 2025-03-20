#PBS -N purge
#PBS -P dy44
#PBS -q normalsr
#PBS -l walltime=2:00:00
#PBS -l ncpus=48
#PBS -l mem=190GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44




ASSEMBLY=/g/data/dy44/r12.34_Elaeocarpus/hifiasm/elae_assembly.fasta
outfolder=purge
bamfile=aligned.bam

mkdir -p $outfolder

cd $PBS_JOBFS

. /home/554/ta0341/.bashrc 
conda activate /g/data/nm31/bin/purge_haplotigs

#purge_haplotigs hist -t 48 -b $PBS_O_WORKDIR/aligned.bam -g $ASSEMBLY -d 800

cp $PBS_O_WORKDIR/$outfolder/$bamfile.gencov ./

purge_haplotigs cov -i $bamfile.gencov -l 30 -m 65 -h 140

purge_haplotigs purge -g $ASSEMBLY -c coverage_stats.csv -r $PBS_O_WORKDIR/elae-rpt.bed -t 48

rsync -rut * $PBS_O_WORKDIR/$outfolder


