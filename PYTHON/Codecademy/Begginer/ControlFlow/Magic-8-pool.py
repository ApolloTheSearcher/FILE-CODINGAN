# Berikut adalah ujian saya ketika belajar di codecademy. tentang control flow
# Membuat program Magic-8-pool 
import random
# Setting up
name = "Gentha"
question ="Apa bisa menang?"
answer = "Tidak kamu gk bakal menang."
random_number = random.randint(1,10)
if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "Insyaallah bisa."
else:
    answer = "Else"
# SEEING THE RESULT
if len(name) == 0:
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
elif len(question) == 0:
    print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)

