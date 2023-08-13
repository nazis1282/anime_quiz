import pandas as pd
import csv
import random

animedata = pd.read_csv("anime_data.csv")

subjects = ['year', 'episodes', 'studio']  # Add more subjects as needed

data = []

for i in range(25):
    anime_name = animedata.loc[i, 'TITLE']
    anime_id = animedata.loc[i, 'ID']

    for subject in subjects:
        if subject == 'year':
            correct_response = animedata.loc[i, 'YEAR']
            question = f"In which year did {anime_name} start streaming?"

            # Generate a list of random wrong responses from the 'YEAR' column
            wrong_responses = animedata['YEAR'].sample(n=3).tolist()

        elif subject == 'episodes':
            correct_response = animedata.loc[i, 'episodes']
            question = f"How many episodes does {anime_name} contain?"

            # Generate a list of random wrong responses from the 'episodes' column
            wrong_responses = animedata['episodes'].sample(n=3).tolist()

        elif subject == 'studio':
            correct_response = animedata.loc[i, 'Studio']
            question = f"Which studio produced {anime_name}?"

            # Generate a list of random wrong responses from the 'Studio' column
            wrong_responses = animedata['Studio'].sample(n=3).tolist()

        # Remove correct response from wrong responses, if present
        if correct_response in wrong_responses:
            wrong_responses.remove(correct_response)

        # Randomly shuffle the wrong responses
        random.shuffle(wrong_responses)

        data.append([anime_id, subject, question,
                    correct_response, wrong_responses])

csv_filename = "generated_questions.csv"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Anime ID", "Subject", "Question", "Correct Response"])
    writer.writerows(data)

print(f"CSV file '{csv_filename}' has been created.")
