import re
import csv

def find_emails(text):
    # Define the regular expression pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Use the findall() function from the re module to find all matches
    emails = re.findall(email_pattern, text)
    
    # Return the list of found email addresses
    return emails

def save_emails_to_csv(emails, filename):
    # Save the found email addresses to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        email_writer = csv.writer(csvfile)
        email_writer.writerow(["Email Addresses"])  # Header row
        for email in emails:
            email_writer.writerow([email])
    print(f"Email addresses saved to {filename}")

def main():
    # Take text input from the user
    print("Please enter the text in which you want to search for email addresses:")
    user_text = input()

    # Find email addresses in the user's text
    found_emails = find_emails(user_text)

    # Display the found email addresses or save them to a CSV file
    if found_emails:
        print("\nFound email addresses:")
        for email in found_emails:
            print(email)
        
        # Ask the user if they want to save the results to a CSV file
        save_option = input("\nWould you like to save these email addresses to a CSV file? (yes/no): ").strip().lower()
        
        if save_option == 'yes':
            filename = input("Please enter the filename (including .csv extension): ").strip()
            save_emails_to_csv(found_emails, filename)
        else:
            print("Email addresses will not be saved.")
    else:
        print("No email addresses found.")

if __name__ == "__main__":
    main()
