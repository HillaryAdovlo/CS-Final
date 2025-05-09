import csv

class VoteCounter:
    def __init__(self, vote_filename: str, user_filename: str) -> None:
        self.vote_filename = vote_filename
        self.user_filename = user_filename
        self.candidates = {"1": "Bianca", "2": "Felicia", "3": "Edward"}
        self.votes = {"1": 0, "2": 0, "3": 0}
        self.total_votes = 0
        self.load_votes()

    def load_votes(self) -> None:
        try:
            with open(self.vote_filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.votes["1"] = int(row.get("Bianca", "0"))
                    self.votes["2"] = int(row.get("Felicia", "0"))
                    self.votes["3"] = int(row.get("Edward", "0"))
                self.total_votes = sum(self.votes.values())
        except FileNotFoundError:
            print("File not found")

    def save_votes(self) -> None:
        try:
            with open(self.vote_filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["Bianca", "Felicia", "Edward"])
                writer.writeheader()
                writer.writerow({"Bianca": self.votes["1"], "Felicia": self.votes["2"], "Edward": self.votes["3"]})
        except Exception as error:
            print(f"Error saving votes: {error}")

    def save_user_vote(self, user_id: str, user_name: str, candidate_number: str) -> None:
        try:
            with open(self.user_filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([user_id, user_name, self.candidates[candidate_number]])
        except Exception as error:
            print(f"Error saving user vote: {error}")

    def vote_for_candidate(self, candidate_number: str) -> None:
        if candidate_number in self.candidates:
            self.votes[candidate_number] += 1
            self.total_votes += 1
            self.save_votes()
        else:
            raise ValueError("Invalid candidate selected")
