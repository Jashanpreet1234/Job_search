# Job Search Management Tool

This is a command-line tool for managing your job applications. It allows you to keep track of job applications by adding new applications, viewing all applications, updating the status of an application, and deleting an application. The data is stored in a CSV file.

## Features

1.) Add a new job application: Input details such as company name, job title, application date, status, and follow-up actions.

2.) View all job applications: Display all stored job applications in a formatted table.

3.) Update the status of a job application: Modify the status of an existing job application.

4.) Delete a job application: Remove a job application from the list.

5.) Save and load applications from a CSV file: Persist the data across sessions.

## Prerequisites

Python 3.x

## Installation
1.) Clone the repository:

git clone https://github.com/yourusername/job-search-management-tool.git
cd job-search-management-tool

2.) (Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.) Install dependencies( if any) 

pip install -r requirements.txt  # No requirements for this simple script

## Usage
1.) Run the script: 
python job_search_tool.py

2.) Follow the on-screen prompts to manage your job applications

## Code Explanation 
Importing Libraries

csv: This module is used for reading from and writing to CSV files.

import csv

os: This module provides a way of using operating system-dependent functionality like checking if a file exists.

import os

## Constants
FILENAME = 'job_applications.csv'

## Functions 
`load_applications`
def load_applications(filename):
    """Load job applications from a CSV file."""
    if not os.path.exists(filename):
        return []

    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

![image](https://github.com/Jashanpreet1234/Job_search/assets/105735825/4fd0cfb2-408e-4925-8b69-2ea36ab388a1)


Purpose: Load job applications from a CSV file into a list of dictionaries.
Logic:
  Checks if the file exists.
  Opens the file in read mode and uses csv.DictReader to read the data.
  Returns a list of dictionaries representing the job applications, or an empty list if the file 
  does not exist.

`save_applications`
def save_applications(filename, applications):
    """Save job applications to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Company', 'Job Title', 'Application Date', 'Status', 'Follow-Up']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(applications)

![image](https://github.com/Jashanpreet1234/Job_search/assets/105735825/1b4e65df-fb8c-4478-8c0f-cfd90e9c84d1)

Purpose: Save the current list of job applications to a CSV file.
Logic:
    Opens the file in write mode.
    Uses csv.DictWriter to write the application data to the file.
    Writes the header and then writes each application as a row in the CSV file.

    
`add_application`
def add_application(applications):
    """Add a new job application."""
    company = input("Enter the company name: ")
    job_title = input("Enter the job title: ")
    application_date = input("Enter the application date (YYYY-MM-DD): ")
    status = input("Enter the application status: ")
    follow_up = input("Enter any follow-up actions: ")

    application = {
        'Company': company,
        'Job Title': job_title,
        'Application Date': application_date,
        'Status': status,
        'Follow-Up': follow_up
    }

    applications.append(application)
    print("Job application added successfully!")
