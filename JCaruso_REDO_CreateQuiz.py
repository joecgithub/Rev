# for final submission; based directly on 23-Charm.py, committed to GitHub.
import textwrap

easy_tries = 4
med_tries = 3
hard_tries = 2

# The three _level strings below are the quizzes to be completed by user. The _blanks and _answers lists
# are the quiz questions to be filled in and the correct answers, respectively, for each level.

easy_level = """What is a computer? How does it do so many things? A computer\n has been defined as essentially a
machine that stores and manipulates __1__. It does this under the control of a computer\n __2__. So the __1__
  goes into a computer and is changed by a __2__\n as __1__ in new forms; it is then displayed as __3__. If the __2__\n
  changes, the computer performs different actions, different tasks.\n Computers are basically machines for carrying
   out -- or __4__ --\n different tasks through varying sequences of actions.\n"""

easy_blanks = ["__1__", "__2__", "__3__", "__4__"]
easy_answers = ["information", "program", "output", "executing"]

medium_level = """Iteration can also be called a __1__ mechanism. Like a conditional\n statement, a __1__ begins with a
 test. If the test evaluates to __2__,\n the computer program executes the __1__ body once and then goes\n back to
  re-evaluate the test. The syntax of a __3__ __1__ in\n Python programming language is - __3__ expression: statement
  (s). Another\n conditional language mechanism, the __4__ __1__, is used more\n often in Python to simplify programs
   that contain iteration.\n"""

medium_blanks = ["__1__", "__2__", "__3__", "__4__"]
medium_answers = ["loop", "true", "while", "for"]

hard_level = """When you're trying to solve some coding problem, often you'll\n find an existing __1__ that creates
 objects that do ALMOST\n what you need. What can you do? You could modify this old\n __1__, but you'll make it more
  complicated. The solution is\n __2__, creating a new __1__ from an existing one, but with\n some additions or
   changes. With __2__, you define only what\n you need to add or change. The original is called the __3__,\n the new
    one the __4__.\n"""

hard_blanks = ["__1__", "__2__", "__3__", "__4__"]
hard_answers = ["class", "inheritance", "parent", "child"]

# This function checks for the exact match (no punctuation) of the blank and its place in the level paragraph.


def match_blanks(match, blanks):
    for same in blanks:
        if same in match:
            return same
    return None


def failure():
    print "Sorry! No more tries!"
    print "Type 'exit' to quit."
    exit = raw_input(" ")
    if exit == "exit":
        quit()
    else:
        print "Not valid input"
        failure()


def check_easy_tries():
    if easy_tries == 0:
        failure()
    else:
        print "Incorrect! You have:", easy_tries, "more chances!\n"


# def choose_difficulty returns (which it 'passes to,' 'are passed to,' 'are picked up by,' 'are called by' another
# function) arguments of the quiz level string (easy, medium, or hard difficulty), the list of quiz level questions
#  to fill in the blanks, and the quiz level answers that are expected.
# In this program, they will be called by ask_questions as quiz, question, answer.


def choose_difficulty():
    level_selection = raw_input("Choose a game difficulty (lower case) by typing in easy, medium, or hard: \n")
    if level_selection == "easy":
        # ? print "You chose an easy quiz. 4 guesses. Let's go! \n \n"
        # print "The paragraph now reads: \n"
        # print easy_level
        return ask_questions(easy_level, easy_blanks, easy_answers)
        # function_two()
    elif level_selection == "medium":
        # ? print "You chose a medium quiz. 3 guesses. Let's go! \n \n"
        # print "The paragraph now reads: \n"
        # print medium_level
        return ask_questions(medium_level, medium_blanks, medium_answers)
    elif level_selection == "hard":
        # ? print "You chose a hard quiz. Only 2 guesses. Let's go! \n \n"
        # ? print "The paragraph now reads: \n"
        # ? print hard_level
        return ask_questions(hard_level, hard_blanks, hard_answers)
    else:
        print " "
        print "Not valid input: type only easy, medium, or hard to choose a quiz type."
        return choose_difficulty()


def ask_questions(level, level_blanks, level_answers):
    print "Here's how the quiz paragraph reads now:"
    print " "
    print level
    guess = 0
    while guess < len(level_blanks):
        if level_blanks[guess] in level:
            answer_input = raw_input("What goes in " + level_blanks[guess] + "?")
            if check_answers(answer_input, level_answers[guess]) == True:
                level = level.replace(level_blanks[guess], answer_input)
                print level
            else:
                guess -= 1
        guess += 1
    print " "
    print "You got it! All complete."
    print " "
    return go_again()


def check_answers(answer_input, level_answers):
    global easy_tries
    if answer_input == level_answers:
            print " "
            print "Right!"
            print "Here's how the quiz paragraph reads now:"
            print " "
            return True
    else:
        print "Sorry, that's wrong! Try again."
        easy_tries -= 1
        check_easy_tries()
        return False


def go_again():
        user_choice = raw_input("Play again? Type either (lower case) yes or no:")
        if user_choice == "yes":
            return choose_difficulty()
        elif user_choice == "no":
            print " "
            print "Ok. Thanks for playing. Bye!"
        else:
            print "Not valid input: type only yes or no in lower case."
            return go_again()

choose_difficulty()
