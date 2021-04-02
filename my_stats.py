from tabulate import tabulate
from datetime import datetime

class Statistics:

    def __init__(self, headers):
        self.headers = headers
        self.headers.insert(0, "Time")

    def print(self, accuracy_percents):
        self.add_time_to_list(accuracy_percents)
        print(tabulate([accuracy_percents], headers=self.headers, floatfmt=".5f", tablefmt = "grid"))

    def add_time_to_list(self, list):
        list.insert(0, self.get_time())

    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")