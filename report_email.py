#!/usr/bin/env python3
import os
import datetime
import reports
import emails

data = []
def process_data(fpath):
    for file in os.listdir(fpath):
        if file.endswith(".txt"):
            with open((fpath + file), "r") as f:
                WORDS = f.readlines()
    data.append({"name":WORDS[0].strip("\n"),"weight":WORDS[1].strip("\n")})
    results = ""
    for item in data:
        result += "name: {} <br/> weigh: {} <br/> <br/>".format(item["name"], item["weight"])
    return results


if __name__ == "__main__":
    fpath_data = os.getcwd() + "/supplier-data/descriptions/"

    date_today = datetime.date.today().strftime("%B %d, %Y")
    title = 'Processed Update on ' + date_today
    attachment = "/tmp/processed.pdf"
    paragraph = process_data(fpath_data)

    # How to generate the pdf
    reports.generate_report(attachment, title, paragraph)

    sender = "automation@example.com"
    receiver = "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
