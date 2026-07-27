student_data = {"id1": { "name": "Ali", "class": "9", "subject": "Math" },
"id2": {"name": "Sara","class": "9","subject": "Science" },
"id3": {"name": "Ali","class": "9","subject": "Math"},
"id4": {"name": "Ahmed","class": "10","subject": "English" }}

# Step 2: Display original records
print("Original Records:")
print(student_data)

# Step 3: Access values safely
print("\nSearching id1:")
print(student_data.get("id1", "Not Found"))

print("\nSearching id5:")
print(student_data.get("id5", "Not Found"))

# Step 4: Add a new student
student_data["id5"] = {"name": "Zara","class": "8","subject": "Computer"}

print("\nAfter adding id5:")
print(student_data)

# Step 5: Update an existing record
student_data["id2"]["subject"] = "Biology"

print("\nAfter updating id2:")
print(student_data)

# Step 6: Remove duplicate records
cleaned_data = {}
seen_records = []

for student_id, details in student_data.items():
    record = (details["name"], details["class"], details["subject"])

    if record not in seen_records:
        seen_records.append(record)
        cleaned_data[student_id] = details

student_data = cleaned_data

print("\nAfter removing duplicates:")
print(student_data)

# Step 7: Remove one record and check length
student_data.pop("id4")

print("\nAfter removing id4:")
print(student_data)

print("\nTotal Records:", len(student_data))

# Step 8: Print final records
print("\nFinal Records:")

for student_id, details in student_data.items():
    print(student_id, ":", details)