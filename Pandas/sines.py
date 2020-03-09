# Pandas module manipulate table
# Mar. 4, 2020
# Nan Hu

#############
# requirement
# 1. Use avan_rm.bed file in “/lustre/work/jenjense/python/Pandas”
# 2. Make sure it has proper column names
# 3. Determine what families are in there (SINE, etc)
# 4. Create new dataframe from that file using only elements in family “SINE” 
# 5. Drop columns “Strand” and “Score”
# 6. Create new column “Length”
# 7. Determine min, max, and mean for all SINEs
# 8. Determine min, max, and mean length for each sub-family of SINE (metulj and ZenoSINE)

import pandas as pd

# 2. Make sure it has proper column names
colnames = ["Scaffold","Start","Stop","Element","Score","Strand","Family","Sub-Family","Divergence"]
te = pd.read_csv("aVan_rm.bed", names = colnames, sep = "\t")

# 3. Determine what families are in there (SINE, etc)
fam_type = te.Family.unique()
print("Different families of TEs in this dataset are: ")
for fm in fam_type:
	print(fm,end =", ")
print("\n")

# 4. Create new dataframe from that file using only elements in family “SINE” 
SINE = te[te["Family"]=="SINE"]

# 5. Drop columns “Strand” and “Score”
SubSINE = SINE.drop(["Strand","Score"], axis=1)

# 6. Create new column “Length”
SubSINE["Length"] = SubSINE["Stop"]-SubSINE["Start"]+1

# 7. Determine min, max, and mean for all SINEs
SINEmin = SubSINE["Length"].min()
SINEmax = SubSINE["Length"].max()
SINEmean = SubSINE["Length"].mean()
print("The min of all SINEs length is: " + str(SINEmin))
print("The max of all SINEs length is: " + str(SINEmax))
print("The mean of all SINEs length is: " + str(SINEmean))

# 8. Determine min, max, and mean length for each sub-family of SINE (metulj and ZenoSINE)
GroupMin = SubSINE.groupby("Sub-Family")["Length"].mean()
print(GroupMin)
