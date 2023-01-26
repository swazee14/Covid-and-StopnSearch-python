from cache import data
import requests
from tkinter import messagebox

def fetch_list_of_police_forces():
    list_of_police_forces = "list_of_police_forces"

    if list_of_police_forces in data:  #cache list of police forces
        return data[list_of_police_forces]
    else: #fetch list of police forces
        response = requests.get("https://data.police.uk/api/forces")
        if response.status_code == 200:
            result = response.json()
            list_of_police_force = {i["name"] : i["id"] for i in result}    #cache list of police forces by name and id
            data[list_of_police_forces] = list_of_police_force
        else:
            list_of_police_force = {}
            messagebox.showinfo("showinfo", "bad request, try again")
        return list_of_police_force
    
def fetch_all_stop_and_search_cases(police_force, date):
    list_of_police_forces = fetch_list_of_police_forces()
    
    stop_and_search_key = police_force + "-" + date     #cache key
    if stop_and_search_key in data:
        return data[stop_and_search_key]    #cache result from the api call
    else:
        response = requests.get( "https://data.police.uk/api/stops-force?force=" + list_of_police_forces[police_force] + "&date=" + date)
        if response.status_code == 200:
            result = response.json()
            data[stop_and_search_key] = {"length_of_result": len(result), "result": result}
            return {"length_of_result": len(result), "result": result}
        else:
            messagebox.showinfo("showinfo", "bad request, try again")
            return {}