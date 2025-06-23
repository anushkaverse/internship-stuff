import pandas as pd
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText

# Load AMC data
df = pd.read_csv("amc_data.csv")

# Today's date
today = datetime.today().date()
reminder_days = 7

# Filter AMC expiring within the next 'reminder_days' days
df['AMC Expiry Date'] = pd.to_datetime(df['AMC Expiry Date']).dt.date
upcoming = df[df['AMC Expiry Date'] <= (today + timedelta(days=reminder_days))]

# Email sending function (ye yha sirf print krta h- demo ke liye)
def send_email(to_email, client_name, asset_id, asset_type, expiry_date):
    subject = f"AMC Expiry Reminder for {asset_type} ({asset_id})"
    body = f"""Dear {client_name},

This is a reminder that the AMC for your {asset_type} with Asset ID - {asset_id} is expiring on {expiry_date}. 
Please contact us to renew it before the mentioned date.

Regards,
Trinity Infonet Solutions"""

    print(f"Sending email to {to_email}...")
    print("Subject:", subject)
    print("Body:\n", body)
    print("------")

# Loop through the filtered list
for index, row in upcoming.iterrows():
    send_email(row['Email'], row['Client Name'], row['Asset ID'], row['Asset Type'], row['AMC Expiry Date'])
