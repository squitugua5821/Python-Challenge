import pandas as pd

csv_path = "election_data.csv"

election_df = pd.read_csv(csv_path, encoding="utf-8")
total_votes = (election_df["Voter ID"].count())
percentage_won = (election_df["Candidate"].value_counts())
print(percentage_won / total_votes * 100, "The Winner is: Khan")



