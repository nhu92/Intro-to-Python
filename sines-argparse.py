# Argparse bedfile to csv
# Practising using argparse
# Apr. 22, 2020
# Nan Hu

# import pandas and argparse
import pandas as pd
import argparse

# Argparse claims
Argparse = argparse.ArgumentParser()
Argparse.add_argument("-f", "--FILE", required = True, help = "Input bed file containing TE information")
Argparse.add_argument("-t", "--FAMILY", required = True, help = "Selecting TE family.")
Argparse.add_argument("-s", "--GENOME", required = True, type = int, help = "Selecting genome size.")
argv = vars(Argparse.parse_args())

# read .bed file
colnames = ["Scaffold","Start","Stop","Element","Score","Strand","Family","Sub-Family","Divergence"]
te = pd.read_csv(argv["FILE"], names = colnames, sep = "\t")

# Determine what families are in there (SINE, etc)
fam_type = te.Family.unique()
print("Different families of TEs in this dataset are: ")
for fm in fam_type:
	print(fm,end =", ")
print("\n")

# Create new dataframe from that file using only elements in selected family  
selected_fam = te[te["Family"]==argv["FAMILY"]]

# Drop columns “Strand” and “Score”
Sub_selected_fam = selected_fam.drop(["Strand","Score"], axis=1)

# Create new column “Length”
Sub_selected_fam["Length"] = Sub_selected_fam["Stop"]-Sub_selected_fam["Start"]+1

# Determine min, max, and mean for all TEs in selected family
selected_fam_min = Sub_selected_fam["Length"].min()
selected_fam_max = Sub_selected_fam["Length"].max()
selected_fam_mean = Sub_selected_fam["Length"].mean()
print("The min of all SINEs length is: " + str(selected_fam_min))
print("The max of all SINEs length is: " + str(selected_fam_max))
print("The mean of all SINEs length is: " + str(selected_fam_mean))

# Determine min, max, and mean length for each sub-family in selected family
GroupMin = Sub_selected_fam.groupby("Sub-Family")["Length"].mean()
for items in GroupMin:
	print(items,end =", ")
print("\n")

# Create new column “Proportion” which is Length/genome size 
Sub_selected_fam["Proportion"] = Sub_selected_fam["Length"]/argv["GENOME"]

# Output a csv
Sub_selected_fam.to_csv("aVan.csv")
