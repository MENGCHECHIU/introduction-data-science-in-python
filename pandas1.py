#For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this 
#assignment is in assets/NISPUF17.csv. A data users guide for this, which you'll need to map the variables 
#in the data to the questions being asked, is available at assets/NIS-PUF17-DUG.pdf. Note: you may have to 
#go to your Jupyter tree (click on the Coursera image) and navigate to the assignment 2 assets folderto see 
#this PDF file).

#Write a function called proportion_of_education which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

#This function should return a dictionary in the form of (use the correct numbers, do not round numbers):

#    {"less than high school":0.2,
#    "high school":0.4,
#    "more than high school but not college":0.2,
#    "college":0.2}

def proportion_of_education():
    import pandas as pd
    import numpy as np
    data=pd.read_csv("assets/NISPUF17.csv",index_col=0)
    edu=data["EDUC1"]
    poe={"less than high school":0,
        "high school":0,
        "more than high school but not college":0,
        "college":0}
    poe["less than high school"]=(data["EDUC1"]==1).sum()/edu.shape[0]
    poe["high school"]=(data["EDUC1"]==2).sum()/edu.shape[0]
    poe["more than high school but not college"]=(data["EDUC1"]==3).sum()/edu.shape[0]
    poe["college"]=(data["EDUC1"]==4).sum()/edu.shape[0]
    return poe
    print(edu.sort_values(ascending=False))
    # your code goes here
    # YOUR CODE HERE
    # raise NotImplementedError()
print(proportion_of_education())