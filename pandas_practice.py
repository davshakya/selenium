import pandas as pd
import numpy as np

# country=["India","China", "USA", "Srilanka"]
# run=[34,789,223,123]
# sr=pd.Series(country)
# print(sr)

# sr1=pd.Series(run,index=country,name='Total runs country wise')
# print(sr1)

d={"dev":78,"manan":98,"ranjana":76,"manav":99}
sr3=pd.Series(d,name="family marks")
print(sr3)
print(sr3.size)
print(sr3.name)
print(sr3.is_unique)
print(sr3.index)
print(sr3.values)
print(sr3.dtype)






