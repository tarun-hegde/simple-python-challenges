import csv
import re

def is_valid_email(email):
    """Simple regex for validating an email"""
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def clean_csv(input_file, output_file):
    """
    Cleans a CSV file by removing duplicate user IDs and ensuring valid email addresses.
    This function reads the input CSV file, filters out rows with duplicate user IDs,
    and only includes rows with valid email addresses. 
    """

    seen_user_ids = set()
    cleaned_data = []

    with open(input_file, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            user_id = row['user_id']
            email = row['email']
            if user_id not in seen_user_ids and is_valid_email(email):
                seen_user_ids.add(user_id)
                cleaned_data.append(row)

    with open(output_file, mode='w', newline='') as outfile:
        fieldnames = cleaned_data[0].keys()
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)

if __name__ == "__main__":
    input_file = 'user_id.csv'
    output_file = 'output.csv'
    clean_csv(input_file, output_file)