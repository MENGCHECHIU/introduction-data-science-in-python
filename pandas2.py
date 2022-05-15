#Let's explore the relationship between being fed breastmilk as a child and getting a 
#seasonal influenza vaccine from a healthcare provider. Return a tuple of the average 
#number of influenza vaccines for those children we know received breastmilk as a child 
#and those who know did not.

#This function should return a tuple in the form (use the correct numbers):(2.5, 0.1)

def average_influenza_doses():
    import pandas as pd
    import numpy as np
    data=pd.read_csv("assets/NISPUF17.csv",index_col=0)
    cbf_flu=data[['CBF_01','P_NUMFLU']]
    cbf_flu1=cbf_flu[cbf_flu['CBF_01'] ==1].dropna()
    cbf_flu2=cbf_flu[cbf_flu['CBF_01'] ==2].dropna()
    f1=cbf_flu1["P_NUMFLU"].sum()/len(cbf_flu1["P_NUMFLU"])
    f2=cbf_flu2["P_NUMFLU"].sum()/len(cbf_flu2["P_NUMFLU"])
    aid=(f1,f2)
    return aid
    # YOUR CODE HERE
#     raise NotImplementedError()
average_influenza_doses()