import csv

username_list = []

with open('data.csv', 'r') as file:
    learner_data = csv.DictReader(file)
    for row in learner_data:
        user_id = row['user_id']
        first_name = row['first_name']
        last_name = row['last_name']
        year_of_birth = row['year_of_birth']
        centre = row['centre']
        gender = row['gender']
        grade = row['grade']

        username = first_name[0] + last_name[0:5] + year_of_birth[-2:] + centre[0:3] + gender[0]

        username_list.append(username)


with open('learner_usernames.csv', 'w') as output_file:
    fieldnames = ['user_id','first_name', 'last_name', 'year_of_birth', 'centre', 'gender', 'grade', 'username']
    output_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    output_writer.writeheader()

    with open('data.csv', 'r') as file:
        learner_data = csv.DictReader(file)
        for index, row in enumerate(learner_data):
            row['username'] = username_list[index]
            output_writer.writerow(row)
