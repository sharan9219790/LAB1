import csv
import os

class CSVHandler:
    @staticmethod
    def save_to_csv(filename, data):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def load_from_csv(filename):
        abs_path = os.path.abspath(filename)
        print(f"🔎 Looking for file at: {abs_path}")

        if not os.path.exists(filename):
            print(f"⚠️ Warning: {filename} not found! Creating an empty file.")
            CSVHandler.save_to_csv(filename, [])

        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            return [row for row in reader if row]
