# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.
medical_cause=input("did you have a medical cause Y or N ").strip().upper()
# (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':
if medical_cause=="Y":
    print("student is allowed to take the exam")
# - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):
else:
    atten=int(input("what is your attendance percentage? "))
# a) Ask for the student’s attendance percentage and store it in `atten`.

# b) If `atten` is 75 or more:
    if atten >= 75:
        print("you are allowed to take exam")
    else:
        print("you are not allowed to take exam")
# - Print "Allowed"

# c) Else:
# - Print "Not allowed"