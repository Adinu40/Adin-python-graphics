import pandas as pd
import matplotlib.pyplot as plt
adu= pd.Series([60,70,80,85], index=["bio", "phy", "chem","civ"])
print(adu)
mean=adu.mean()
print("mean =" ,mean)
median= adu.median()
print("median =", median)
print(adu["phy"])
adu["phy"]= 65
print(adu)
adu[2]=85
print(adu)
filt=adu>mean
print("Result above mean  ")
print(filt)
print("Result above 50")
print(adu>50)
for idx, value in adu.iteritems():
	print(idx, value)
for idx in adu.keys():
	print(idx)
print(adu.count())
print(adu.value_counts())
print(adu.duplicated())
print(adu.drop_duplicates)
print(adu)
print(adu.describe())
print(adu.min())
print(adu.idxmin())
print(adu.var())
print(adu.std())
print(adu.mad())

adu.plot(x="x",y="y")
plt.xlabel("index")
plt.ylabel("value")
plt.show()
adu.skew()
adu.kurt()
adu.cov(adu)
adu.corr(adu)
adu.diff()
adu.cumsum()