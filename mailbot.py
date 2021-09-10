# import email package
import poplib

# import time package for waiting
import time

# import package that extracts urls from strings
# !!!!!!!!!!!IMPORTANT!!!!!!!!!!!!!
# type 'pip install urlextract' to install urlextract
from urlextract import URLExtract

# server, email, password, check frequency


def connectAndGetLinks(emailServer, emailUser, emailPassword, interval):

    # Connect to email server
    server = poplib.POP3(emailServer)
    server.user(emailUser)
    server.pass_(emailPassword)

    # Remember mail count before new email
    mail_count = server.stat()[0]

    server.quit()

    while True:
        print(".")

        # Wait certain amount of time to check new mail
        time.sleep(interval)

        # Connect to email server again
        server = poplib.POP3(emailServer)
        server.user(emailUser)
        server.pass_(emailPassword)

        # Get newest email count
        new_mail_count = server.stat()[0]

        # If new email is found, break out of loop
        if new_mail_count - mail_count >= 1:
            break

    # Saves the email as string into whole_email variable
    whole_email = ""
    for j in server.retr(new_mail_count)[1]:
        whole_email += str(j)

    # Extract all the urls found in the string
    extractor = URLExtract()
    urls = extractor.find_urls(whole_email)

    # Quit email server
    server.quit()

    # Return array of urls
    return urls
