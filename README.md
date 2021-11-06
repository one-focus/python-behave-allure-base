## Simple project using Page Object model and selenium
### Installation:
+ Install HomeBrew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python@3.10
brew install chromedriver
pip install git+https://github.com/behave/behave
pip install -r requirements.txt
```
### Run 
```
behave
behave --tags=regression,search
```
```
python behave-parallel.py --tags=regression,search
```
### Report
```
behave -f allure_behave.formatter:AllureFormatter -o allure-results --tags=regression,search  
allure generate --clean "allure-results" -o "allure-report"
allure serve allure-results
```