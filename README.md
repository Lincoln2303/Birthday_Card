# Birthday_Card

A Python script that reads birthday data from a CSV file and sends personalized birthday cards via email.

## Features

- Automatically sends personalized birthday cards via email to individuals whose birthday matches the current date.
- Uses customizable letter templates for the birthday cards.
- Selects a random template for each recipient for added variety.

## Technologies Used

- Python
- pandas: A powerful data analysis and manipulation library for Python.
- smtplib: A Python library for sending emails using the Simple Mail Transfer Protocol (SMTP).

## Setup

1. Create a CSV file named birthday.csv with the following columns: name, email, year, month, day. Fill in the data for each person's name, email, and birthdate.
2. Create three text files letter_1.txt, letter_2.txt, letter_3.txt containing the letter templates for the birthday cards.
3. Replace the following placeholders in the script:
  - my_email: Replace with your email address.
  - app_password: Replace with your app password generated for SMTP access.
4. Verify that the correct template filenames are used in the script.
5. Install the required Python packages: pip install pandas smtplib

## Usage

1. The script reads the birthday data from the birthday.csv file.
2. It selects a random birthday card template from the available options.
3. For each person in the CSV file whose birthday matches the current date, the script replaces the [NAME] placeholder in the template with the person's name.
4. It sends a personalized birthday card via email to each person using the SMTP protocol.
5. The email subject is "Happy Birthday [Name]", and the content of the email is the personalized birthday card template.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
The project is part of the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" course on Udemy by Dr. Angela Yu.
