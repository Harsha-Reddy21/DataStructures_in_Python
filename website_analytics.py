
monday_visitors = {"user1","user2","user3","user4","user5"}
tuesday_visitors = {"user2","user4","user6","user7","user8"}
wednesday_visitors = {"user1","user3","user6","user9","user10"}



unique_visitors = monday_visitors | tuesday_visitors | wednesday_visitors
print("1. Unique Visitors Across All Days:")
print("Visitors:", unique_visitors)
print("Count:", len(unique_visitors))
print()



returning_tuesday = monday_visitors & tuesday_visitors
print("2. Returning Visitors on Monday and Tuesday:")
print("Visitors:", returning_tuesday)
print()


new_monday = monday_visitors
new_tuesday = tuesday_visitors - monday_visitors
new_wednesday = wednesday_visitors - (monday_visitors | tuesday_visitors)

print("3. New Visitors Each Day:")
print("New on Monday:", new_monday)
print("New on Tuesday:", new_tuesday)
print("New on Wednesday:", new_wednesday)
print()


loyal_visitors = monday_visitors & tuesday_visitors & wednesday_visitors
print("4. Loyal Visitors (all three days):")
print("Visitors:", loyal_visitors)
print()


monday_tuesday_overlap = monday_visitors & tuesday_visitors
tuesday_wednesday_overlap = tuesday_visitors & wednesday_visitors
monday_wednesday_overlap = monday_visitors & wednesday_visitors

print("5. Daily Visitor Overlap Analysis:")
print("Monday ∩ Tuesday:", monday_tuesday_overlap)
print("Tuesday ∩ Wednesday:", tuesday_wednesday_overlap)
print("Monday ∩ Wednesday:", monday_wednesday_overlap)
