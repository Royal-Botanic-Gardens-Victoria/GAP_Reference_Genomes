#PBS -N cp-ann-damp
#PBS -P dy44
#PBS -q normalsr
#PBS -l walltime=8:00:00
#PBS -l ncpus=8
#PBS -l mem=64GB
#PBS -l jobfs=4GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44




module load julia


for i in cp-split/*.fasta

do

outname=cp-gff-split/${i##*/}_chloe.gff3

julia --project=/g/data/nm31/bin/chloe /g/data/nm31/bin/chloe/chloe.jl annotate -s 0.5 --nofilter --short-gene-warning-threshold 0.75 --gff -r /g/data/nm31/bin/chloe/chloe_references/ -o $outname $i


done

#julia --project=/g/data/nm31/bin/chloe /g/data/nm31/bin/chloe/chloe.jl annotate -s 0.5 --nofilter --short-gene-warning-threshold 0.75 --gff -r /g/data/nm31/bin/chloe/chloe_references/ -o ./ r12.1_Doryanthes-merged-cp.fasta

#julia --project=/g/data/nm31/bin/chloe /g/data/nm31/bin/chloe/chloe.jl annotate -s 0.5 --nofilter --short-gene-warning-threshold 0.75 --gff -r /g/data/nm31/bin/chloe/chloe_references/ -o ./ /g/data/dy44/r12.36_organelle_annotation/fixed/r12.8_gastrolobium_cp_merged.fasta

