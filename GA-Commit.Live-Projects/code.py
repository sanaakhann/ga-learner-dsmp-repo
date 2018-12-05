# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)
print(loan_term)

big_loan_term = (loan_term >= 25).sum() 
print(big_loan_term)

# code ends here


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks,values='LoanAmount', index=['Gender','Married', 'Self_Employed'],                                     aggfunc=np.mean)



# code ends here



# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here

data = pd.read_csv(path)
bank = pd.DataFrame(data)

categorical_var = bank.select_dtypes(include=['object'])
print(categorical_var)


numerical_var = bank.select_dtypes(include=['number'])
print(numerical_var)





# code ends here


# --------------
# code ends here
loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']
print(loan_groupby)

mean_values = loan_groupby.mean()
print(mean_values)

# code ends here


# --------------
# code starts here
loan_approved_se = banks['Self_Employed'][(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].count().sum()
print(loan_approved_se)    

loan_approved_nse = banks['Self_Employed'][(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].count().sum()
print(loan_approved_nse)

percentage_se = (loan_approved_se/614)*100
print(percentage_se)
percentage_nse = (loan_approved_nse/614)*100
print(percentage_nse)
# code ends here






# --------------
# code starts here

banks = bank.drop(columns=['Loan_ID'], axis=1)

print(banks.isnull().sum())

bank_mode = banks.mode()

banks = banks.replace(np.NaN,bank_mode)

banks.notnull()

#code ends here


