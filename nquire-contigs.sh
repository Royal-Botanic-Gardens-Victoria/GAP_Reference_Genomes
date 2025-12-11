#PBS -P dy44
#PBS -N nquire-contigs-damp
#PBS -q normalsr
#PBS -l walltime=48:00:00
#PBS -l ncpus=104
#PBS -l mem=300GB
#PBS -l jobfs=16GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44

infile=/g/data/dy44/r12.41_Dampiera_repeat/Dampiera_purged_1M.fasta
outfolder=/g/data/dy44/r12.41_Dampiera_repeat/nquire-contigs/
reads=/g/data/dy44/r12.41_Dampiera_repeat/reads-filt.fasta
prefix=Dampiera-purged

mkdir -p $outfolder

#fasta_split.py $infile $outfolder 40

module load samtools

for i in $outfolder/*.fasta
do
echo $i
name=${i##*/}
samtools faidx $infile


minimap2 -t 104 -a -x map-hifi $i $reads --sam-hit-only | samclip --max 30 --ref $i | samtools sort > $name.bam




mv $name.bam $outfolder
done


nquire-para.py "${outfolder}/*.bam" $outfolder/ 104
