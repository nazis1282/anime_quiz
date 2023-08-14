import csv
import pandas as pd
import random

animedata = pd.read_csv("anime_data.csv")

subjects = ['year', 'episodes', 'studio']  # Add more subjects as needed
wrong_answer_count = 3

data = []
question_id = 1  # Initialize the question ID counter

for i in range(25):
    anime_name = animedata.loc[i, 'TITLE']
    anime_id = animedata.loc[i, 'ID']

    for subject in subjects:
        if subject == 'year':
            correct_response = animedata.loc[i, 'YEAR']
            question = f"In which year did {anime_name} start streaming?"

            # Fetch wrong answers from the 'YEAR' column
            wrong_answers = animedata['YEAR'].sample(
                n=wrong_answer_count).tolist()
            wrong_answers = [str(answer) for answer in wrong_answers if str(
                answer) != str(correct_response)]

        elif subject == 'episodes':
            correct_response = animedata.loc[i, 'episodes']
            question = f"How many episodes does {anime_name} contain?"

            # Fetch wrong answers from the 'episodes' column
            wrong_answers = animedata['episodes'].sample(
                n=wrong_answer_count).tolist()
            wrong_answers = [str(answer) for answer in wrong_answers if str(
                answer) != str(correct_response)]

        elif subject == 'studio':
            correct_response = animedata.loc[i, 'Studio']
            question = f"Which studio produced {anime_name}?"

            # Fetch wrong answers from the 'Studio' column
            wrong_answers = animedata['Studio'].sample(
                n=wrong_answer_count).tolist()
            wrong_answers = [
                answer for answer in wrong_answers if answer != correct_response]

        # Shuffle wrong answers
        random.shuffle(wrong_answers)

        data.append([question_id, anime_id, subject, question,
                    correct_response, *wrong_answers])
        question_id += 1  # Increment the question ID

# Write data to a CSV file
csv_filename = "questions"

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Question ID", "Anime ID", "Subject", "Question",
                    "Correct Response", "Wrong Response 1", "Wrong Response 2", "Wrong Response 3"])
    writer.writerows(data)

print(f"CSV file '{csv_filename}' has been created.")
