import pandas as pd 

#Extracting Unique areas from the covid dataframe and sorting the areas alphabet
covid_dfl=pd. read_csv('data/specimenDate_ageDemographic-unstacked.csv', low_memory=False)
areas = sorted(covid_dfl.areaName.unique().tolist())

    