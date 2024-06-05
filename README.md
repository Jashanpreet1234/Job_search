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
![image](https://github.com/Jashanpreet1234/Job_search/assets/105735825/be8f71b4-4c10-46d1-9733-54bd474a1ac0)

Purpose: Collects details for a new job application and adds it to the list.
Logic:
    Prompts the user for details about the job application.
    Creates a dictionary with the provided details.
    Appends this dictionary to the list of applications.
    Prints a success message.

`view_applications`

def view_applications(applications):
    """View all job applications."""
    if not applications:
        print("No job applications found.")
        return

    print(f"{'Company':<20} {'Job Title':<20} {'Application Date':<15} {'Status':<15} {'Follow-Up':<20}")
    print("-" * 90)
    for app in applications:
        print(f"{app['Company']:<20} {app['Job Title']:<20} {app['Application Date']:<15} {app['Status']:<15} {app['Follow-Up']:<20}")

![image](https://github.com/Jashanpreet1234/Job_search/assets/105735825/7fda1133-51d8-461b-8899-8542fd0e12b8)

Purpose: Display all stored job applications in a formatted table.
Logic:
    Checks if there are any applications in the list.
    Prints a header row.
    Iterates through the list and prints each application's details in a formatted manner.

`update_application_status`  

def update_application_status(applications):
    """Update the status of a job application."""
    company = input("Enter the company name of the application to update: ")
    job_title = input("Enter the job title of the application to update: ")

    for app in applications:
        if app['Company'] == company and app['Job Title'] == job_title:
            new_status = input(f"Enter the new status (current: {app['Status']}): ")
            app['Status'] = new_status
            print("Job application status updated successfully!")
            return

    print("Job application not found.")
    
![image](https://github.com/Jashanpreet1234/Job_search/assets/105735825/37e279e6-87d0-4cb4-97a5-fe5f719b43a3)

Purpose: Updates the status of a specified job application.
Logic:
    Prompts the user for the company name and job title of the application to update.
    Searches the list for a matching application.
    If found, prompts the user for the new status and updates the application.
    Prints a success message or an error message if the application is not found.

`delete_application`

def delete_application(applications):
    """Delete a job application."""
    company = input("Enter the company name of the application to delete: ")
    job_title = input("Enter the job title of the application to delete: ")

    for i, app in enumerate(applications):
        if app['Company'] == company and app['Job Title'] == job_title:
            del applications[i]
            print("Job application deleted successfully!")
            return

    print("Job application not found.")

![image](https://github.com/Jashanpreet1234/Job_search/assets/105735825/27f111bc-a013-4f27-97de-e1534e00833b)

## Main Function

def main():
    """Main function to run the job search management tool."""
    applications = load_applications(FILENAME)

    while True:
        print("\nJob Search Management Tool")
        print("1. Add a new job application")
        print("2. View all job applications")
        print("3. Update the status of a job application")
        print("4. Delete a job application")
        print("5. Save and exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_application(applications)
        elif choice == '2':
            view_applications(applications)
        elif choice == '3':
            update_application_status(applications)
        elif choice == '4':
            delete_application(applications)
        elif choice == '5':
            save_applications(FILENAME, applications)
            print("Job applications saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

![image](https://github.com/Jashanpreet1234/Job_search/assets/105735825/7abe0a17-6262-4666-b2fc-97330ef56291)

Purpose: Runs the job search management tool, displaying a menu and handling user input.
Logic:
    Loads existing applications from the CSV file.
    Displays a menu with options to add, view, update, or delete applications, or to save and 
    exit.
    Calls the appropriate function based on the user's choice.
    Saves the applications to the CSV file and exits when the user chooses to save and exit.
    Prints an error message for invalid choices.
    
Purpose: Ensures the main function runs only if the script is executed directly, not if it is imported as a module in another script

## Output 
![image](https://github.com/Jashanpreet1234/Job_search/assets/105735825/b5adc8a4-d07f-4d8b-867e-ee5ed20ccbf9)
