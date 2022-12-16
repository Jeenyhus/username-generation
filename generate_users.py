# uses csv module to read the file and create the username_list
import csv

username_list = []

# opens a csv file and reads data, then assigns the data from each row to variables
with open('inb.csv', 'r') as file:
    learner_data = csv.DictReader(file)
    for row in learner_data:
        user_id = row['user_id']
        first_name = row['first_name']
        last_name = row['last_name']
        year_of_birth = row['year_of_birth']
        centre = row['centre']
        gender = row['gender']
        grade = row['grade']
        
# create usernames taking the 1st letter of their first name, first 5 letters of their last name, last 2 digits of their year of birth,
# first 3 letters of their centre and 1st letter of their gender, adding it to the username_list.
        username = first_name[0] + last_name[0:5] + year_of_birth[-2:] + centre[0:3] + gender[0]

        username_list.append(username.lower())

# opens csv file, set the fieldnames, and write the header row. This allows the data to be stored in a structured way.
with open('learner_usernames.csv', 'w') as output_file:
    fieldnames = ['user_id', 'full_name', 'first_name', 'last_name', 'year_of_birth', 'centre', 'gender', 'grade', 'username']
    output_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    output_writer.writeheader()

# opens the csv file and iterating through the rows of data to assign each row a username from the username_list. Finally, it is writing the rows to an output file.
    with open('inb.csv', 'r') as file:
        learner_data = csv.DictReader(file)
        for index, row in enumerate(learner_data):
            row['username'] = username_list[index]
            full_name = row['first_name'] + ' ' + row['last_name']
            full_name = ' '.join(full_name.split())
            row['full_name'] = full_name
            output_writer.writerow(row)

# removes the empty rows
with open('learner_usernames.csv', 'r') as file:
  reader = csv.reader(file)
  lines = list(reader)
  with open('learner_usernames.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for line in lines:
      if line:
        writer.writerow(line)

# prints out the message that the file has been created
print("Successfully created learner_usernames.csv file")