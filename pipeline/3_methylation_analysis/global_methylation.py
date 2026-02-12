import pandas as pd
import gzip
import sys

path = sys.argv[1] # bedMethyl file
size = int(sys.argv[2]) # genome size in bp
threshold = float(sys.argv[3]) # base methylation threshold (e.g. 50%)

# Parse the bedMethyl file
with gzip.open(path, 'rb') as handle:
    pileup = pd.read_table(handle, sep =  "\t", usecols = [1,2,3,10],
                           names = ['start', 'stop', 'type', 'perc_mod'])
    
# Filter out non-modified bases
pileup = pileup[pileup['perc_mod'] >= threshold]

# Global methylation level
nb_meth = pileup.shape[0]
frac_meth = nb_meth/size

# m6A methylation level
nb_6a_meth = pileup[pileup['type'] == 'a'].shape[0]
frac_6a_meth = nb_6a_meth/size

# m5C methylation level
nb_5c_meth = pileup[pileup['type'] == 'm'].shape[0]
frac_5c_meth = nb_5c_meth/size

# m4C methylation level
nb_4c_meth = pileup[pileup['type'] == '21839'].shape[0]
frac_4c_meth = nb_4c_meth/size

print(f"Methylation stats for file {path}")
print(f"Global methylation fraction: {frac_meth}")
print(f"4mC methylation fraction: {frac_4c_meth}")
print(f"5mC methylation fraction: {frac_5c_meth}")
print(f"6mA methylation fraction: {frac_6a_meth}")
