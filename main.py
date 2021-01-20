# Creating a multiple choice quiz using the import of a class, lists, a function, a for loop, an if statement and a print statement:

#from Questions import Questions

from Questions import Question
question_prompts = [ # Here we are creating a list of questions and naming it question_prompts.
    "What is port 443?\n(a) HTTPS\n(b) TFTP\n(c) SNMP\n(d) HTTP\n\n",
    "What IP class is 172.12.5.0?\n(a) Class A\n(b) Class B\n(c) Class C \n(d) Class D\n\n",
    "What do you use to connect a PC to a switch?\n(a) Console cable\n(b) Rollover cable\n(c) Crossover cable \n(d) Straight-Through cable\n\n",
    "What is layer 3 or the OSI model?\n(a) Application layer\n(b) Network layer\n(c) Physical layer\n\n",
    "How many available hosts are on a /29 subnet?\n(a) 8\n(b) 123\n(c) 16\n(d) 32\n\n",
    "What tool would you use to locate a particular cable on a rack?\n(a) ODTR\n(b) Multimeter\n(c) Toner and Probe\n(d) Voltage Reader\n\n",
    "Switches are responsible for routing information across networks. True or False?\n(a) True\n(b) False\n\n",
    "The TCP/IP model is also know as the: \n(a) Bus model\n(b) DoD model\n(c) Spine and leaf model\n\n",
    "List the 4th cable in the TIA/EIA B wiring standard. \n(a) Blue-white\n(b) Brown\n(c) Orange\n(d) Blue\n\n",
    "Which of these best describes a MAC address? \n(a) A dynamically changing logical address used at layer 2 of the OSI model.\n(b) A logical address used to route data from network to network\n(c) A pyhsical address burned into the NIC of a device.\n\n",

]

# Here we are creating another list (this time called questions) and adding the Question class and passing in values to the attributes of the Question class. We are first passing in our question prompts and call out which index position they are in within our question_prompts list, then we are giving the correct answer to the question using a string value
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "d"),
    Question(question_prompts[9], "c"),
]


# Now we are defining our run_test function and passing the questions variable (which is a list of question using the question class and question_prompts variable) into it and we are also giving a starting point for our score (which is 0), then we are iterating or looping through each question in the questions variable/list and stating that if the answer that the user inputs within the question prompt attribute (inside of the Question class) is equal to the answer attribute that we have defined within our Question class, then increment their score up by one. Finally, print a statement telling the user how many questions they got correct and then finally run the function to make this program work.
def run_test(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

# Here we define what message to print based on the score.
    if score >= 7:
        print("You're a networking superstar!")
    if score == 6:
        print("Good attempt, but it looks like you still have more to review.")
    if score == 5:
        print("Good attempt, but it looks like you still have more to review.")
    if score <= 4:
        print("You need to keep studying.")


# Import random.shuffle and run quiz
import random
random.shuffle(questions)

run_test(questions)

