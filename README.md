<!-- 
    As part of the in-course assessment (ICA) for Software for Digital Innovation, EZEH JIDECHUKWU has submitted this project to the School of Computing, Engineering and Digital Technologies. This project was build with the help of python and it's frameworks. 
-->

Getting Started:

It is important to mention that this project supports **Python Version 3 upwards** running this on a lower version might result in certain problems. Ensure to only use **Python Version 3 upwards**



Installation

Step 1:

Installation of python version used (Python 3) - Python can be downloaded from the official python website which is https://www.python.org/downloads/. Ensure to download a python interpreter that suits your device. **For MacOs users** it is not advisable to work with the default python that comes with the system please upgrade.

Step 2:

Installation of Python packages and it's versions - The requirement.txt file in the project folder contains a list of the necessary packages and their related versions. Open the project folder in **Command Prompt** and type the following command `python -m pip install -r requirement.txt`. This will install all the packages and their versions used during the development of this project. **For MacOs users** use `python3 -m pip install -r requirement.txt`. 

Step 3:

Starting the GUI - To start the GUI application, Open the project folder in **Command Prompt** and type `python -m main_app`.**For MacOs users** use `python3 -m main_app`. This should start the application as seen in the image attached ![GUI app](images/tkinter-window.png)



The following visualisations are contained in the project:

Covid ![Covid button](images/covid-window.png) -  

⊛ Total cases per day over a given period ![Total cases per day over a given period](images/covid/total-cases-per-day-over-a-given-period.png)
⊛ Total cases per month over a given period ![Total cases per month over a given period](images/covid/total-cases-per-month-over-a-given-period.png)
⊛ Total cases on a given day ![Total cases on a given day](images/covid/total-cases-on-a-given-day.png)
⊛ Areas with highest percentage change in cases on a given day ![Areas with highest percentage change in cases on a given day](images/covid/Areas-with-highest-pecentage-change-in-daily-cases.png)
⊛ Comparison of cases in two areas per day ![Comparison of cases in two areas per day](images/covid/compairson-of-cases-in-two-areas-per-day.png)

Stop and Search ![Stop and Search button](images/stop-and-search-window.png) - 

⊛ Stop and search cases gender ![Stop and search cases gender](images/stop_and_search/stop-and-search-cases-by-gender.png)
⊛ Stop and search result by age range that resulted in arrest ![Stop and search result by age range that resulted in arrest](images/stop_and_search/stop-and-search-result-by-age-range-that-resulted-in-arrest.png)
⊛ Stop and search cases by officer defined ethnicity ![Stop and search cases by officer defined ethnicity](images/stop_and_search/stop-and-search-cases-by-officer-defined-ethnicity.png)
⊛ Stop and search cases by legislation ![Stop and search cases by legislation](images/stop_and_search/stop-and-search-cases-by-legislation.png)
⊛ Type of stop and search cases ![Type of stop and search cases](images/stop_and_search/type-of-stop-and-search-cases.png)
⊛ Outcome of stop and search cases ![Outcome of stop and search cases](images/stop_and_search/outcome-of-stop-and-search.png)



Unit testing

The unit tests used for this project are contained in the **test_app.py**. The procedures shown below describe how to run the unit tests used for this project and determine the test coverage for the application.

Step 1:

Open the project folder in **Command Prompt** and type `python -m test_app`. **For MacOs users** type `python3 -m test_app`, this executes each test present in the project. ![Unit test](images/test.png)

Step 2: To check for test coverage, Open the project folder in **Command Prompt** 

1. To perform coverage for all tests, enter the command `python -m coverage run -m unittest discover`.  **For MacOs users** use `python3 -m coverage run -m unittest discover`, This executes every test and determines the coverage. ![discover coverage for test](images/unit-test-discover.png)
    
2. Enter `python -m coverage report -m` to report the coverage in the command prompt. Use the command `python3 -m coverage report -m` on a **Mac** to find out how much test coverage was done.