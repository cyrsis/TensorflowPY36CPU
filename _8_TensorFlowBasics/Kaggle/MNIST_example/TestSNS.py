import pandas as pd
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

from io import StringIO

datafile = StringIO("""\
IDNUM,S1Q2I
39191,1
39787,1
42909,1
43092,1
7,2
15,2
63,2
68,2
100,2
104,2
145,2
168,2
3787,9
6554,9
7616,9
29045,9
29731,9
""")

data = pd.read_csv(datafile, low_memory=False)

#setting a new dataset...
sub2 = data[(data["S1Q2I"]==1)].copy()

#setting the missing data 9 = unknown into NaN
sub2["S1Q2I"] = sub2["S1Q2I"].replace(9, numpy.nan)

#setting date to categorical type
sub2["S1Q2I"] = sub2["S1Q2I"].astype('category')

#plotting
sns.countplot(x="S1Q2I", data=sub2)