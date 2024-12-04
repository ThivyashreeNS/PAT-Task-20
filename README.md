## Overview:
This project demonstrates the use of Selenium WebDriver for automating web interactions with two government websites: CoWIN and Labour. It includes automation for navigating through various web pages, interacting with elements, and downloading files or images.

The project contains three main scripts:

- Task_20_Cowin.py - Automates navigation on the CoWIN website.
- Task_20_Labour.py - Automates interactions with the Labour Ministry website.
- test_Cowin.py and test_Labour.py - Test scripts to verify the functionality of the web automation scripts.

## Table of Contents:
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Code Explanation](#Code-Explanation)
- [Running the Tests](#running-the-tests)

## Features:
- Navigate to the FAQ and Partners sections on the CoWIN website.

- Handle multiple browser windows and perform actions like opening, switching, and closing windows.

- Download PDF files and images from the Labour Ministry website.

- Manage window handles for multiple browser tabs.

- Automated testing using pytest to ensure the correctness of the scripts.

## Prerequisites
- Python 3.x
- Required libraries:
  - `selenium`
  - `pytest`
  - `webdriver-manager`
  - `Requests`

## Installation:
To successfully set up and run the Selenium Automation Testing Project, follow these steps:

1. Ensure that you have Python 3.x installed on your machine. You can download it from  [python.org](https://www.python.org/).

2. Familiarity with command-line interface (CLI) tools is recommended for executing commands.

3. Set Up a Virtual Environment (Optional but Recommended):
   - It's best practice to create a virtual environment to manage dependencies for your project:
     
     - Verify Python Virtual Environment: `Virtualenv --version`
       
     - Create Virtual Environment:  `virtualenv cd`
       
     - Activate Virtual Environment:  `Scripts\Activate`
       
     - Deactivate Virtual Environment: `Scripts\Deactivate`
       
4.  Install Required Libraries:
    - Install the necessary Python libraries using pip. The required libraries for this project include:
      - __Selenium :__ For web browser automation.
        Install Python Selenium Module: `pip install selenium`
        
      - __Pytest :__ For running test cases and managing test execution.
        `pip install pytest`
         Pytest Report: `pip install pytest-html`
        
      - __requests :__ Used for downloading images from the Labour website.
         `pip install requests`
        
      - __Webdriver-manager :__ To automatically manage browser drivers.
          Install WebDriver Manager Module: `pip install webdriver-manager`

## Project Structure
```
PAT Task 20/
│
├── Task_20_Cowin.py                # CoWIN website automation script
├── Task_20_Labour.py               # Labour Ministry website automation script
├── test_Cowin.py                   # Test file for CoWIN automation
├── test_Labour.py                  # Test file for Labour automation
├── downloaded_photos               # Downloaded photos from the Labour website
└── README.md                       # Project description and usage
```

## Code Explanation
### CoWIN Automation (Task_20_Cowin.py)

- __WindowsAutomation:__ This class automates the browser actions on the CoWIN website. It clicks the FAQ and Partners links, handles multiple windows, and prints the window IDs.
- __Test:__ The test verifies that three windows are opened (main window, FAQ, and Partners).

### Labour Automation (Task_20_Labour.py)

- __WindowsAutomation:__  This class interacts with the Labour website, closes an ad banner, downloads a PDF report, and downloads up to 10 photos from the media gallery.
- __Test:__ The test verifies that exactly 10 photos have been downloaded.





