# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)

data['Gender'].replace('-', 'Agender', inplace=True)

gender_count = data['Gender'].value_counts()

plt.hist(gender_count)
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()

plt.pie(alignment)
xlabel = 'Character Alignment'






# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']]

a = sc_df.cov()
print(a)
print('-'*20)
sc_covariance = a.iloc[0,1]
print(sc_covariance)
print('-'*20)
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()

sc_pearson = sc_covariance/(sc_combat*sc_strength)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']]

b = ic_df.cov()
print(b)

ic_covariance = b.iloc[0,1]
print(ic_covariance)

ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance/(ic_combat*ic_intelligence)
print(ic_pearson) 







# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)

super_best = data[data['Total']>total_high]
print(super_best)

super_best_names = list(super_best['Name'])

print(super_best_names)











# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1,figsize=(30,30))

ax_1=plt.boxplot(data.Intelligence)
#xtitle("Intelligence")

ax_2=plt.boxplot(data.Speed)
#xtitle("Speed")

ax_3=plt.boxplot(data.Power)
#xtitle("Power")








