# Check 1
# Check 2
# Check 3
# Check 4

blanks = ["__1__", "__2__", "__3__", "__4__"]
easy_level = """What manipulates __1__. It
 does  __2__. So as __3__. If __4__ actions.\n"""
easy_correct_answers = ["information", "program", "output", "executing"]
medium_level = """Iteration can also be called a __1__ mechanism. Like a conditional\n
 statement, a LOOP begins with a test. If the test evaluates to __2__,\n the computer
  program executes the LOOP body once and then goes\n back to re-evaluate the test.
   The syntax of a __3__ LOOP in\n Python programming language is - WHILE expression:
    statement(s). Another\n conditional language mechanism, the __4__ LOOP, is used more\n
     often in Python to simplify programs that contain iteration.\n"""
medium_correct_answers = ["loop", "true", "while", "for"]
hard_level = """When you're trying to solve some coding problem, often you'll\n find an
 existing __1__ that creates objects that do ALMOST\n what you need. What can you do?
  You could modify this old\n CLASS, but you'll make it more complicated. The solution
   is\n __2__, creating a new CLASS from an existing one, but with\n some additions or
    changes. With INHERITANCE, you define only what\n you need to add or change. The
     original is called the __3__,\n the new one the __4__.\n"""
hard_correct_answers = ["class", "inheritance", "parent", "child"]

# This function checks for the exact match (no punctuation) of the blank and its place in the level paragraph.
def match_blanks(match, blanks):
    for same in blanks:
        if same in match:
            return same
    return None


# function_one prompts user to input a level selection -- easy/medium/hard.
# It checks that those words have actually been input.
# Then it passes the correct level string, and answers, to Function_two


def function_one():
    level_selection = raw_input("Choose a game difficulty (lower case) by typing in easy, medium, or hard: \n")
    if level_selection == "easy":
        print "You chose an easy quiz. 4 guesses. Let's go! \n \n"
        print "The paragraph now reads: \n"
        print easy_level
        return easy_level, easy_correct_answers
        # function_two()
    elif level_selection == "medium":
        print "You chose a medium quiz. 3 guesses. Let's go! \n \n"
        print "The paragraph now reads: \n"
        print medium_level
        return medium_level, medium_correct_answers
    elif level_selection == "hard":
        print "You chose a hard quiz. Only 2 guesses. Let's go! \n \n"
        print "The paragraph now reads: \n"
        print hard_level
        return hard_level, hard_correct_answers
    else:
        return "Not valid input. You'll need to relaunch the quiz."


def function_two():
    level, answers = function_one()
    # guess, correct_answer = function_three(str, str)
    level = level.split()
    for match in level:
        switch = match_blanks(match, blanks)
        if switch != None:
            answer_input = raw_input("What should be substituted in " + switch + " ?")
            # if answer_input == guess:
            #    print "Good!"
            return function_three(str, str)


def function_three(answer_input, answers):
    #answer_input, answers = function_two()
    for i in range(len(answers)):
        guess = answers[i]
        if answer_input == guess:
            print "OKAY!"
            return guess, answers
        #elif answer_input != guess:
        #    print "NOOOO!"
        return function_two()

# TRY TO REWRITE REDO_CodeAQuiz.py PUTTING IN THE ELIF STATEMENT OF FUNCTION_THREE A COUNTER THAT SAYS: "ELSE, PRINT # OUT WRONG AND RETURN DEMAND ANSWER_INPUT AGAIN."
# PROBLEM WITH THIS FILE V. IT IS THAT WITHOUT RETURNING FUNCTION_THREE WITH PARAMETERS AS REDO_ DOES, FUNCTION_THREE DOESN'T EXECUTE HERE AS IT DOES THERE:

function_two()
