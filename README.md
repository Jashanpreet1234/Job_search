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
def load_applications(filename):
    """Load job applications from a CSV file."""
    if not os.path.exists(filename):
        return []

    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

Purpose: Load job applications from a CSV file into a list of dictionaries.
Logic:
  Checks if the file exists.
  Opens the file in read mode and uses csv.DictReader to read the data.
  Returns a list of dictionaries representing the job applications, or an empty list if the file 
  does not exist.
