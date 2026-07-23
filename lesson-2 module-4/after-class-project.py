# Create a tuple with different data types
habit_info=("Reading",True,7,20.5)
print(habit_info)

# Create a tuple of daily habit completion
# 1 means completed, 0 means missed
weekly_habits=(1,0,1,1,0,1,1)
print(weekly_habits)

# Find the length of the tuple
print("length:",len(weekly_habits))

# Access items using indexing
print("first day:",weekly_habits[0])
print("fourth day:",weekly_habits[3])
# Access items using slicing
print("first three days:",weekly_habits[0:3])
print("last two days:",weekly_habits[5:7])
# Create a new tuple (tuples are immutable)
new_weekly_habits=weekly_habits=weekly_habits=(1,)
print("update tuple:",new_weekly_habits)
# Count completed and missed days
completed=weekly_habits.count(1)
missed=weekly_habits.count(0)

print("completed days:",completed)
print("Missed days:",missed)
# Print progress message
print("\nWeekly habit tracker summary")
if completed>missed:
    print("Good job! keep it up!")
else:
    print("Try to improve next week")
# Final summary
print("\nWeekly Habit Tracker Summary")
print("Habit:", habit_info[0])
print("Status:", habit_info[1])
print("Total Days:", habit_info[2])
print("Average Time:", habit_info[3], "minutes")
print("Completed:", completed)
print("Missed:", missed) 