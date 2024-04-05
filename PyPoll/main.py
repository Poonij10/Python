import csv

csv_file_path = r"C:\Users\jaspe\OneDrive\Desktop\Classwork\Python\PyPoll\Resources\election_data.csv"


total_votes = 0

candidates = {}

winner = None

max_votes = 0



with open(csv_file_path, "r") as file:

    csv_reader = csv.reader(file)

    

   

    next(csv_reader)

    

    

    for row in csv_reader:

        

        total_votes += 1

    

        candidate_name = row[2]

        

        

        candidates[candidate_name] = candidates.get(candidate_name, 0) + 1

        

        

        if candidates[candidate_name] > max_votes:

            winner = candidate_name

            max_votes = candidates[candidate_name]



print("Election Results")

print("-------------------------")

print(f"Total Votes: {total_votes}")

print("-------------------------")

for candidate, votes in candidates.items():

    percentage = (votes / total_votes) * 100

    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")

print(f"Winner: {winner}")

print("-------------------------")

