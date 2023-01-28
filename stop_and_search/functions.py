from tkinter import messagebox
import pandas as pd
from stop_and_search.api_request import fetch_all_stop_and_search_cases
from helpers.format_date import format_date_to_year_month
from matplotlib_charts import  scatter_plot, donut_chart, pie_chart, simple_bar_chart, tree_map_visual

def fetch_all_cases(date, police_force):
    result = fetch_all_stop_and_search_cases(police_force, date)["result"]
    if result == []:
        return messagebox.showinfo("showinfo", "There is no data for this  month selected")
    else: 
        return result
    
def search_by_gender(date, police_force):
    df = pd.DataFrame.from_dict(fetch_all_cases(format_date_to_year_month(date), police_force))
    gender = df.groupby(['gender'], as_index=False)[ ["involved_person"] ].count()
    graph_title = "Breakdown of stop and search cases by gender for " + police_force + " in " + date
    explode = [0.05, 0.05]
    return pie_chart(graph_title, gender["involved_person"], gender["gender"], explode, label_title="label")

def search_by_age_range_that_resulted_in_arrest(date, police_force):
    df = pd.DataFrame.from_dict(fetch_all_cases(format_date_to_year_month(date), police_force))
    df = df.loc[df['outcome'] == "Arrest"]
    df = df.reset_index()
    age_range = df.groupby(["age_range"], as_index=False)[["involved_person"]].count()
    graph_title = "Breakdown of stop and search cases by age range for " + police_force + " on " + date
    return donut_chart(graph_title, age_range["involved_person"], age_range["age_range"])

def search_by_officer_defined_ethnicity(date, police_force):
    df = pd.DataFrame.from_dict(fetch_all_cases(format_date_to_year_month(date), police_force))
    officer_defined_ethnicity = df.groupby(['officer_defined_ethnicity'], as_index=False)[ ["involved_person"] ].count()
    graph_title = "Breakdown of stop and search cases by officer defined ethnicity " + police_force + " on " + date
    return tree_map_visual(graph_title, officer_defined_ethnicity["involved_person"], officer_defined_ethnicity["officer_defined_ethnicity"])
    
def search_by_legislation(date, police_force):
    df = pd.DataFrame.from_dict(fetch_all_cases(format_date_to_year_month(date), police_force))
    legislation = df.groupby(['legislation'], as_index=False)[ ["involved_person"] ].count()
    graph_title = "Breakdown of stop and search cases by legislation for " + police_force + " in " + date
    if len(legislation["involved_person"]) == 3:
        colors = ["#94D2BD","gold", "#FFB703"]
    elif len(legislation["involved_person"]) == 2:
        colors = ["#94D2BD", "#E6CCB2"]
    return scatter_plot(graph_title, legislation["legislation"], legislation["involved_person"], colors)
    
def search_by_type(date, police_force):
    df = pd.DataFrame.from_dict(fetch_all_cases(format_date_to_year_month(date), police_force))
    type = df.groupby(['type'], as_index=False)[ ["involved_person"] ].count()
    graph_title = "Type of stop and search cases for " + police_force + " on " + date
    return simple_bar_chart(graph_title, type["involved_person"], type["type"])
    
def search_outcome(date, police_force):
    df = pd.DataFrame.from_dict(fetch_all_cases(format_date_to_year_month(date), police_force))
    outcome = df.groupby(['outcome'], as_index=False)[ ["involved_person"] ].count()
    graph_title = "Outcome of stop and search cases for " + police_force + " on " + date
    return donut_chart(graph_title, outcome["involved_person"], outcome["outcome"])