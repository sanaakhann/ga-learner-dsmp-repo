# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
#df.head()
fico_grt_700=df['fico']>700
#print(fico_grt_700.value_counts())
#x=df.loc[fico_grt_700,'fico']
fico_grt_700=len(df.loc[fico_grt_700,'fico'])
#print(fico_grt_700)
len_df=len(df)
#print(len_df)
p_a=fico_grt_700/len_df
print(p_a)
df1=df['purpose']== 'debt_consolidation'
#y=df.loc[df1,'purpose']
df1=len(df[df1])
p_b=df1/len_df
print(p_b)
p_both=p_a*p_b
# Probability of A given B is equal to P(B,A) / P(A)
p_a_b=p_both/p_a
print(p_a_b)
result=(p_a_b==p_a)
print(result)
# code ends here


# --------------
# code starts here

prob_lp=len(df.loc[df['paid.back.loan']=='Yes','paid.back.loan'])/len_df
print(prob_lp)
prob_cs=len(df.loc[df['credit.policy']=='Yes','credit.policy'])/len_df
print(prob_cs)
new_df=df.loc[df['paid.back.loan']=='Yes',:]
prob_pd_cs=new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]
print(prob_pd_cs)
bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
import numpy as np
import matplotlib.pyplot as plt
name=df['purpose'].unique()
counts=np.array(df['purpose'].value_counts())
plt.bar(name,counts)
plt.xlabel('Purpose')
plt.ylabel('Counts Of all Purpose')
plt.xticks(rotation=90)
plt.show()

df1=df.loc[df['paid.back.loan']=='No',:]
df1.purpose.value_counts(normalize=True).plot(kind='bar')
df1.shape
# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()
inst_mean=df['installment'].mean()
plt.hist(df.installment)
a=df['log.annual.inc']
plt.hist(a)
# code ends here


