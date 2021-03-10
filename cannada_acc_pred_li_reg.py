from sklearn import linear_model
import pandas as pd 
import matplotlib.pyplot as plt 
password='shsnsnnssn'
df=pd.read_csv("cannada_acc.csv")
plt.scatter(df['Acc'],df['Year'])
#plt.show()
reg=linear_model.LinearRegression()
reg.fit(df[['Acc']],df.Year)
df1=pd.read_csv("can_acc_cal.csv")
p=reg.predict(df1[['Year']])
df1['Acc']=p
df1.to_csv('can_acc_cal.csv')
print(reg.predict([[2020]]))
plt.plot(df1['Acc'],df1['Year'],color='blue')
plt.show()