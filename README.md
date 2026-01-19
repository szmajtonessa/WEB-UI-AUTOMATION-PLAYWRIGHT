WEB UI TEST AUTOMATION PROJECT USING PYTEST AND PLAYWRIGHT  
  
#Overview  
This project is an end-to-end test automation framework built to test the SauceDemo web application.  

#Tech Stack  
-Python 3.10+  
-Playwright (Python)  
-pytest  
-pytest-html  
  
#Project Structure  
\---pages/# Page Object Models  
\---tests/# Test cases  
\---utils/# Test data and helpers  
\---reports/# Test reports (generated)  
\---conftest.py # pytest fixtures and hooks  
\---requirements.txt  
\---README.md  

#How to Run Tests

1. Install dependencies
'''bash
pip install -r requirements.txt

2. Install Playwright browsers
playwright install

3. Run tests
pytest

#Test reports  
  
-HTML report  
  pytest --html=reports/report.html --self-contained-html  
  
-Screenshots on Failure  
  Screenshots are automatically captured when a test fails and saved to: reports/screenshots/  
  
-Video recordings  
  Videos of test execution are saved to: reports/videos/  
  
-Playwright Trace Viewer  
  Traces are recorded for failed tests and can be viewed using: playwright show-trace reports/traces/<test_name>.zip  
