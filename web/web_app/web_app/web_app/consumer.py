# from kafka import KafkaConsumer
# import json
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# consumer = KafkaConsumer(
#     'user-signups',
#     bootstrap_servers='broker:9092',
#     auto_offset_reset='earliest',
#     enable_auto_commit=True,
#     value_deserializer=lambda m: json.loads(m.decode('utf-8'))
# )

# def send_welcome_email(email, user_details):
#     sender_email = "your-email@example.com"
#     receiver_email = email
#     password = "your-email-password"
#     message = MIMEMultipart("alternative")
#     message["Subject"] = "Welcome to Our Service"
#     message["From"] = sender_email
#     message["To"] = receiver_email

#     text = f"Hi {user_details['name']},\nWelcome to our service!"
#     part = MIMEText(text, "plain")
#     message.attach(part)

#     with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message.as_string())

# def consume_signup_messages():
#     for message in consumer:
#         user_info = message.value
#         send_welcome_email(user_info['email'], user_info['details'])

# # Consume messages when the script is run
# if __name__ == "__main__":
#     consume_signup_messages()
