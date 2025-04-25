import smtplib
import schedule
import time
from plyer import notification

# Function to send email
def send_email(subject, message, to_email):
    from_email = "your_email@example.com"  # Replace with your email
    password = "your_password"  # Replace with your email password

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, password)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(from_email, to_email, email_message)
            print(f"Email sent to {to_email}!")
    except Exception as e:
        print(f"Error: {e}")

# Function to show desktop notification
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Automated Reminder System",
        timeout=10
    )

# Function to add a reminder
def add_reminder(reminder_time, message, to_email):
    schedule.every().day.at(reminder_time).do(send_email, "Reminder", message, to_email)
    schedule.every().day.at(reminder_time).do(show_notification, "Reminder", message)

# Main function
def main():
    print("Automated Reminder System")
    to_email = input("Enter your email address: ")

    while True:
        reminder_time = input("Enter reminder time (HH:MM format, 24-hour): ")
        message = input("Enter reminder message: ")
        add_reminder(reminder_time, message, to_email)
        print(f"Reminder set for {reminder_time} with message: '{message}'")

        # Run the scheduler
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()