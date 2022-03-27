last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subject = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics",98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Your code below: 
print(gradebook)

# Add more subjects
gradebook.append(["computer science",100])
gradebook.append(["visual arts", 93])
print(gradebook)

# Modify the gradebook
gradebook[-1][-1] = 95
gradebook[2].remove(85)
gradebook[2].append("Pass")

# ONE BIG GRADEBOOK!
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
