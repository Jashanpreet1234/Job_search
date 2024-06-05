import csv
import os

FILENAME = 'job_applications.csv'

def load_applications(filename):
    """Load job applications from a CSV file."""
    # Check if the file exists; if not, return an empty list
    if not os.path.exists(filename):
        return []

    # Open the file in read mode with UTF-8 encoding
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        # Use DictReader to read the CSV file into a list of dictionaries
        reader = csv.DictReader(file)
        return list(reader)

def save_applications(filename, applications):
    """Save job applications to a CSV file."""
    # Open the file in write mode with UTF-8 encoding
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        # Define the column headers for the CSV file
        fieldnames = ['Company', 'Job Title', 'Application Date', 'Status', 'Follow-Up']
        # Create a DictWriter object with the specified headers
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Write the header row to the CSV file
        writer.writeheader()
        # Write all application data to the CSV file
        writer.writerows(applications)

def add_application(applications):
    """Add a new job application."""
    # Prompt the user to enter details for the new job application
    company = input("Enter the company name: ")
    job_title = input("Enter the job title: ")
    application_date = input("Enter the application date (YYYY-MM-DD): ")
    status = input("Enter the application status: ")
    follow_up = input("Enter any follow-up actions: ")

    # Create a dictionary with the entered details
    application = {
        'Company': company,
        'Job Title': job_title,
        'Application Date': application_date,
        'Status': status,
        'Follow-Up': follow_up
    }

    # Add the new application to the list of applications
    applications.append(application)
    print("Job application added successfully!")

def view_applications(applications):
    """View all job applications."""
    # Check if there are any applications to display
    if not applications:
        print("No job applications found.")
        return

    # Print the header row
    print(f"{'Company':<20} {'Job Title':<20} {'Application Date':<15} {'Status':<15} {'Follow-Up':<20}")
    print("-" * 90)
    # Print each application in a formatted manner
    for app in applications:
        print(f"{app['Company']:<20} {app['Job Title']:<20} {app['Application Date']:<15} {app['Status']:<15} {app['Follow-Up']:<20}")

def update_application_status(applications):
    """Update the status of a job application."""
    # Prompt the user to enter the company name and job title of the application to update
    company = input("Enter the company name of the application to update: ")
    job_title = input("Enter the job title of the application to update: ")

    # Search for the application in the list
    for app in applications:
        if app['Company'] == company and app['Job Title'] == job_title:
            # Prompt the user to enter the new status
            new_status = input(f"Enter the new status (current: {app['Status']}): ")
            # Update the status of the application
            app['Status'] = new_status
            print("Job application status updated successfully!")
            return

    # If the application is not found, print a message
    print("Job application not found.")

def delete_application(applications):
    """Delete a job application."""
    # Prompt the user to enter the company name and job title of the application to delete
    company = input("Enter the company name of the application to delete: ")
    job_title = input("Enter the job title of the application to delete: ")

    # Search for the application in the list
    for i, app in enumerate(applications):
        if app['Company'] == company and app['Job Title'] == job_title:
            # Delete the application from the list
            del applications[i]
            print("Job application deleted successfully!")
            return

    # If the application is not found, print a message
    print("Job application not found.")

def main():
    """Main function to run the job search management tool."""
    # Load existing applications from the CSV file
    applications = load_applications(FILENAME)

    # Loop to display the menu and process user choices
    while True:
        print("\nJob Search Management Tool")
        print("1. Add a new job application")
        print("2. View all job applications")
        print("3. Update the status of a job application")
        print("4. Delete a job application")
        print("5. Save and exit")

        # Prompt the user to enter their choice
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Add a new job application
            add_application(applications)
        elif choice == '2':
            # View all job applications
            view_applications(applications)
        elif choice == '3':
            # Update the status of a job application
            update_application_status(applications)
        elif choice == '4':
            # Delete a job application
            delete_application(applications)
        elif choice == '5':
            # Save all applications to the CSV file and exit
            save_applications(FILENAME, applications)
            print("Job applications saved. Exiting...")
            break
        else:
            # Print an error message for invalid choices
            print("Invalid choice. Please enter a number between 1 and 5.")

# Entry point of the script
if __name__ == "__main__":
    main()
