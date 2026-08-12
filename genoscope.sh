#PBS -P dy44
#PBS -N erem-genoscope
#PBS -q normalsr
#PBS -l walltime=4:00:00
#PBS -l ncpus=48
#PBS -l mem=190GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44

cd $PBS_JOBFS

#input file must be called reads.fasta and seqs be on one line

INFOLDER=$PBS_O_WORKDIR

READLEN=19244

GENOMESIZE=800000000

jellyfish count -C -m 21 -s $GENOMESIZE	 -t 48 $INFOLDER/hifi-filt.fasta -o reads.jf &>jflog.txt 

jellyfish histo -t 48 reads.jf > reads.histo

rsync -rut reads.histo  $INFOLDER/

mkdir genomescope

Rscript ~/bin/genomescope/genomescope.R reads.histo 21 $READLEN genomescope/ 500


rsync -rut genomescope $INFOLDER/

