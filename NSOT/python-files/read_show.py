import os
import csv


class ShowCommandsReader:
    def __init__(self, base_dir):
        """Initialize the ShowCommandsReader with the base directory."""
        self.base_dir = base_dir
        self.commands_csv_path = os.path.join(
            self.base_dir, "..", "..", "MISC", "show_commands.csv"
        )

    def load_show_commands(self):
        """Loads show commands from a CSV file and categorizes them."""
        commands = {}
        try:
            with open(self.commands_csv_path, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    category = row["Category"]
                    command = row["Command"]
                    if category not in commands:
                        commands[category] = []
                    commands[category].append(command)
        except Exception as e:
            print(f"Error reading show commands CSV: {e}")
        return commands
