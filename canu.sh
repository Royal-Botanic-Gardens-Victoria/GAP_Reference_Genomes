#PBS -P dy44
#PBS -N canu
#PBS -q normalsr
#PBS -l walltime=48:00:00
#PBS -l ncpus=104
#PBS -l mem=500GB
#PBS -l jobfs=400GB
#PBS -l wd
#PBS -l storage=gdata/nm31+scratch/nm31+gdata/if89+scratch/dy44+gdata/dy44

cd $PBS_JOBFS

label=gast
saveLocation=$PBS_O_WORKDIR/
reads=$PBS_O_WORKDIR/reads-filt.fasta
stageDirectory=/scratch/dy44/ta0341/
genomeSize=1.2g
correctCoverage=25
correctedErrorRate=0.03
corMaxEvidenceErate=0.05
minReadLength=10000
minOverlapLength=500


/g/data/nm31/bin/canu-2.2/bin/canu \
		-p $label \
		-d ${saveLocation}/canu_${label} \
		-nanopore $reads \
		-fast \
		genomeSize=${genomeSize} \
		stageDirectory=${stageDirectory} \
		corOutCoverage=${correctCoverage} \
		useGrid=false \
		correctedErrorRate=${correctedErrorRate} \
		corMaxEvidenceErate=${corMaxEvidenceErate} \
		minReadLength=${minReadLength} \
		minOverlapLength=${minOverlapLength} \
		"batOptions=-dg 3 -db 3 -dr 1 -ca 500 -cp 50" \
		cormhapMemory=60 \
		cormhapConcurrency=8 \
		cormhapThreads=13 \
		obtmhapMemory=60 \
		obtmhapConcurrency=8 \
		obtmhapThreads=13 \
		utgmhapMemory=60 \
		utgmhapConcurrency=8 \
		utgmhapThreads=13 
