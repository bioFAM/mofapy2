from mofapy2.run.entry_point import entry_point
import pandas as pd
import numpy as np
import argparse

#####################
## Parse arguments ##
#####################

parser = argparse.ArgumentParser()
parser.add_argument('--gpu', action='store_true')

args, _ = parser.parse_known_args()

################################
## Load data in matrix format ##
################################

# views = ["0"]
# sample_groups = ["0"]

# data = [None]*len(views)
# for m in range(len(views)):
#     data[m] = [None]*len(sample_groups)
#     for g in range(len(sample_groups)):
#         datafile = "%s/%s_%s.txt.gz" % (datadir, views[m], sample_groups[g])
#         data[m][g] = pd.read_csv(datafile, header=None, sep='\t')

####################################
## Load data in data.frame format ##
####################################

data = pd.read_csv("ftp://ftp.ebi.ac.uk/pub/databases/mofa/getting_started/data.txt.gz", sep="\t")

##########
## MOFA ##
##########

# initialise
ent = entry_point()

# Set data options
ent.set_data_options()

# Set data
ent.set_data_df(data)

# Set model options
ent.set_model_options(factors=15)

# Set training options
ent.set_train_options(iter=50, freqELBO=1, dropR2=None, startELBO=1, verbose=False, seed=42, convergence_mode="fast", gpu_mode=args.gpu)

# Build the model
ent.build()

# Train the model
ent.run()

# Save the model
# ent.save(outfile)
