# GAP_Reference_Genomes
This repository contains the scripts used to assemble and analyse the plant genomes generated for the paper: "Filling the Gaps in Australian Angiosperm Genomes." Allnutt et al., 2025.\
\
Pipeline:\
\
HiFi reads:\
reads > genoscope.sh [if coverage too low repeat sequencing]
cp_bbmap.sh\
mt_bbmap.sh\
getcpreads.sh > cphifiasm.sh > plastid genome > cp-ann.sh > plastid annotation\
getmtreads.sh > mthifiasm.sh > mitochondrial genome > mfannot-folder.sh > mitochondrial annotation\
Reads filtered of organelle genome reads:\
hifiasm.sh\
purge-hist.sh > set kmer freq. thresholds for purging\
purge.sh > purged assembly\
purged assembly > repeatmodeler.sh > repeatmasker.sh > repeat counts / table\
purged assembly > tidk.sh > count-telomeres.py > telomeres\
purged assembly > compleasm.sh > BUSCO scores.\
purged assembly > nquire-contigs.sh > ploidy estimates\
purged assembly > gemoma.sh > annotations\
\
ONT reads:\
raw_reads.fastq > chopper.sh > filtered reads > herro.sh > corrected reads\
\
Corrected reads combined with Hifi filtered reads where available then fed into the same pipeline as HiFi reads, except assembly done with hifiasm-herro.sh\
