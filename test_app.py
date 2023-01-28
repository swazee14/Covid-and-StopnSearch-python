import pandas as pd
import pytest
import warnings
import unittest
import requests
from main_app import index
from stop_and_search.api_request import fetch_list_of_police_forces, fetch_all_stop_and_search_cases
from functions.widgets import text_label, button, date_entry, combo_box
from helpers.format_date import format_date, format_date_to_year_month

class testModules(unittest.TestCase):

    @pytest.mark.asyncio
    # To start the tkinter window without actually launching it
    async def _start_app(self):
        self.app.mainloop()

    def setUp(self):
        warnings.filterwarnings("ignore")
        self.app = index()
        self._start_app()

    def tearDown(self):
        self.app.destroy()
    
    #This tests checks that a Label from tkinter is rendered
    def test_text_label(self):
        Label = text_label(self.app, "Test label", 0, 0).winfo_class()
        self.assertEqual(Label, "Label")
    
    #This tests checks that a Button from tkinter is rendered
    def test_button(self):
        render_button = button(self.app,'SUBMIT', 0, 0).winfo_class()
        self.assertEqual(render_button, "Button")
        
    #This tests checks that a TEntry from tkinter is rendered
    def test_date_entry(self):
        date = date_entry(self.app, 0, 0).winfo_class()
        self.assertEqual(date, "TEntry")
        
    #This tests checks that a TCombobox from tkinter is rendered
    def test_combo_box(self):
        render_combo_box = combo_box(self.app, ["1", "2", "3", "4"],30, 0, 0).winfo_class()
        self.assertEqual(render_combo_box, "TCombobox")
        
    #This test checks that the fetch_list_of_police_forces functions returns a dictionary
    def test_list_of_police_forces(self):
        list_of_police_forces = fetch_list_of_police_forces()
        self.assertIsInstance(list_of_police_forces, dict)
        
    #This test checks that the stop and search api returns a 200
    def test_return_stop_and_search_cases(self):
        result = requests.get("https://data.police.uk/api/stops-force?force=essex&date=2021-06")
        self.assertEqual(result.status_code, 200)
        
    #This test checks that fetch_all_stop_and_search_cases returns a tuple 
    def test_format_date(self):
        result = format_date("05-12-2022")
        self.assertIsInstance(result, str)
        
    #This test checks that format_date_to_year_month returns a string 
    def test_format_date_to_year_month(self):
        result = format_date_to_year_month("05-12-2022")
        self.assertIsInstance(result, str)
        
    #This test checks that fetch_all_stop_and_search_cases returns a string 
    def test_fetch_all_stop_and_search_cases(self):
        result = fetch_all_stop_and_search_cases("Dorset Police", "2021-05")
        self.assertIsInstance(result, dict)

if __name__ == "__main__":
    unittest.main(verbosity=2)