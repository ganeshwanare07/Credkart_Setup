#!/bin/bash

cd "$WORKSPACE"

# Activate virtual environment
source "/Users/ganeshwanare/Desktop/Ganesh/new test data/Testing Notes Credence/Assignments/.venv/bin/activate"

# Check Python and pytest
python --version
which python
which pytest

# Run test
pytest -v -s --browser chrome \
--alluredir=Reports \
--html=Html_Report/my_report.html

#All Browsers with specific test case
#pytest -v -s -n=auto --html=Html_reports\my_headless_report_31st_jan_2026.html --browser headless -k "test_verify_Credkart_url_001" --alluredir=AllureReports
#pytest -n=auto --html=Html_reports\my_chromereport_31st_jan_2026.html --browser chrome -k "test_verify_Credkart_url_001" --alluredir=AllureReports
#pytest -n=auto --html=Html_reports\my_firefoxreport_31st_jan_2026.html --browser firefox -k "test_verify_Credkart_url_001" --alluredir=AllureReports
#pytest -n=auto --html=Html_reports\my_safarireport_31st_jan_2026.html --browser safari -k "test_verify_Credkart_url_001" --alluredir=AllureReports

#pytest -n=auto --html=Html_reports\my_edgereport_31st_jan_2026.html --browser edge -k "test_verify_Credkart_url_001" --alluredir=AllureReports


#headless sh
#pytest -v -s -n=auto --html=Html_reports\my_headless_report_31st_jan_2026.html --browser headless -k "test_verify_Credkart_url_001" "--alluredir=AllureReports" "--disable-warnings"


#Persmission first
#chmod +x run.sh

#Then
#./run.sh

#Run in one time
#chmod +x run.sh
#./run.sh

#pytest -v -s --alluredir=Reports
#allure serve Reports


#Jenkins command
#brew services list
#brew services start jenkins-lts
#brew services start jenkins-lts
#brew services stop jenkins-lts
#brew services restart jenkins-lts
#brew services list
#jenkins-lts started