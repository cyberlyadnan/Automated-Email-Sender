\\

---

# Automated Email Sender

This project is designed to automate the process of sending emails to a list of contacts using Python and SMTP. It utilizes random quotes from the Hadith collection and includes news updates from a CSV file.

## Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/cyberlyadnan/Automated-Email-Sender.git
    ```

2. Install the required dependencies:

    ```bash
    pip install pandas
    ```

3. Update the following variables in the `main.py` file:

    ```python
    MY_MAIL = "your_email@gmail.com"
    MY_PASSWORD = "your_email_password"
    ```

4. Ensure you have a CSV file named `news.csv` containing a list of contacts with their names and email addresses.

5. Run the script to send automated emails:

    ```bash
    python main.py
    ```

## Usage

- The script reads random quotes from the Hadith collection in the `hadis.py` file.
- It selects news updates from the `news.csv` file to include in the email content.
- Modify the email template as per your requirements in the `main.py` file.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

---

Feel free to customize the README further based on your specific project details, usage instructions, and contribution guidelines.
