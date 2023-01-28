import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt
import tkinter as tk 
from tkinter import messagebox
from matplotlib_charts import grouped_bar_chart_visual, tree_map_visual, diverging_text_visuals, area_chart, population_pyramid
from helpers.format_date import format_date
# from datetime import date
import calendar

# Importing the CSV file 
covid_df=pd.read_csv('data/specimenDate_ageDemographic-unstacked.csv', low_memory=False)

# Creating a new dataframe with only relevant columns
covid_df=covid_df[['areaType','areaCode','areaName','date','newCasesBySpecimenDate-0_59','newCasesBySpecimenDate-60+']]

# Deleting all rows with empty columns
covid_df1=covid_df.dropna(inplace=False)

#creating a new column which contains the total number of new cases by specimen date
covid_df1["newCasesBySpecimenDate-Sum"] = (covid_df1["newCasesBySpecimenDate-0_59"] + covid_df1["newCasesBySpecimenDate-60+"])

#Creating new columns to show the percentage change in new cases by specimen date
covid_df1['PercentageChange-cases-0_59']=covid_df1["newCasesBySpecimenDate-0_59"].pct_change() * 100
covid_df1['PercentageChange-cases-60+']=covid_df1["newCasesBySpecimenDate-60+"].pct_change() * 100
covid_df1['PercentageChange-cases_Sum']=covid_df1["newCasesBySpecimenDate-Sum"].pct_change() * 100

# Replacing infs with NaN and filling NaNs  with 0
covid_df1.replace([np.inf, -np.inf], np.nan, inplace=True)
covid_df1.fillna(0, inplace=True)

def cases_per_day_over_a_period(date_one, date_two):
    title =  "Percentage change in Daily covid cases from " + date_one + " to " + date_two
    covid_data = covid_df1.loc[((covid_df1["date"] >= format_date(date_one)) & (covid_df1["date"] <= format_date(date_two)))]
    covid_data = covid_data.groupby(["date"], as_index=False)[[ "PercentageChange-cases_Sum" ]].sum()
    max_row = covid_data[covid_data['PercentageChange-cases_Sum']==covid_data['PercentageChange-cases_Sum'].max()]
    
    if len(covid_data) > 1:
        area_chart(title, max_row["date"].tolist()[0], max_row["PercentageChange-cases_Sum"].tolist()[0], covid_data )
    else:
        return messagebox.showinfo("showinfo", "No data available, select again")
    
def cases_per_month_over_a_period(date_one, date_two):
    if date_one == date_two:
        return messagebox.showinfo("showinfo", "cannot compare same month")
    
    covid_data_new = covid_df1.loc[(covid_df1["date"] >= format_date(date_one)) & (covid_df1["date"] <= format_date(date_two))]
    covid_data_new['months'] = pd.DatetimeIndex(covid_data_new['date']).month_name()
    covid_data_new = covid_data_new.groupby('months')['newCasesBySpecimenDate-Sum'].sum()
    covid_data_new = covid_data_new.reset_index()
    
    if len(covid_data_new) > 1:
        title =  "Covid cases by month from " + date_one + " to " + date_two 
        labels = covid_data_new.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
        return tree_map_visual(title, covid_data_new["newCasesBySpecimenDate-Sum"], labels )
    else:
        return messagebox.showinfo("showinfo", "No data available, select again")
    
def cases_on_a_given_day(date):
    title =  "Total Covid cases on " + date
    covid_data = covid_df1.loc[((covid_df1["date"] == format_date(date)))]
    covid_data = covid_data.groupby(["areaName"], as_index=False)[[ "newCasesBySpecimenDate-Sum", "newCasesBySpecimenDate-60+" ]].sum()
    
    if len(covid_data) > 1:
        covid_data_df = covid_data.sort_values([ "newCasesBySpecimenDate-Sum", "newCasesBySpecimenDate-60+" ],ascending=False)[:20] 
        return population_pyramid(title, covid_data_df, covid_data_df["newCasesBySpecimenDate-Sum"], covid_data_df["newCasesBySpecimenDate-60+"], covid_data_df["areaName"], x_label = "Cases count", y_label ="Age group")
    else:
        return messagebox.showinfo("showinfo", "No data available, select again")

def areas_with_highest_cases_on_a_given_day(date_selected):  
    title =  "Areas with the highest percentage change in covid cases on " + date_selected
    covid_data = covid_df1.loc[ (covid_df1["date"] == format_date(date_selected)) ]
    
    covid_data = covid_data.groupby(["areaName"], as_index=False)[[ "PercentageChange-cases_Sum" ]].sum()
    covid_data = covid_data.sort_values([ "PercentageChange-cases_Sum" ],ascending=False)[:30]
    
    if len(covid_data) > 1:
        return diverging_text_visuals(title, covid_data, "PercentageChange-cases_Sum" )
    else:
        return messagebox.showinfo("showinfo", "No data available, select again")

def compare_two_areas_per_day(region_one, region_two, date_selected):
    if region_one == region_two:
        return messagebox.showinfo("showinfo", "Regions cannot be the same")
    
    title =  "Covid cases between " + region_one + " and " + region_two + " on " + date_selected
    covid_data = covid_df1.loc[ (covid_df1["date"] == format_date(date_selected)) ]
    covid_data = covid_data.loc[(covid_data['areaName'] == region_one) | (covid_data['areaName'] == region_two)]
    
    covid_data = covid_data.groupby(["areaName"], as_index=False)[[ "newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+", "newCasesBySpecimenDate-Sum"]].sum()
    covid_data = covid_data.sort_values([ "newCasesBySpecimenDate-0_59", "newCasesBySpecimenDate-60+", "newCasesBySpecimenDate-Sum"],ascending=False)
    
    if len(covid_data) > 1:
        return grouped_bar_chart_visual(title, covid_data, "areaName", "Covid cases", ["Age Group 0-59", "Age Group 60+", "Age Group Sum"])
    else:
        return messagebox.showinfo("showinfo", "No data available, select again")
