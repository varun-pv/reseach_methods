import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("edu9_n.csv",)
df.boxplot(column=['All Schools 2010-11', 'All Schools 2011-12', 'All Schools 2012-13'],figsize=(10,10))
df.plot.bar(x='State/UTs', y='All Schools 2012-13 (Functional Computers)', rot=90,figsize=(10,10))
d=pd.read_csv("gdp_data.csv",index_col=0)
gdp=d[['Gross Domestic Product (in Rs. Cr) at 2004-05 Prices','Agriculture (in Rs. Cr.) at 2004-05 Prices','Industry (in Rs. Cr.) at 2004-05 Prices','Mining and Quarrying (in Rs. Cr.) at 2004-05 Prices']]
gdp.plot.line(figsize=(14,14))
