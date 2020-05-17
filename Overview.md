# Introduction
This is a program written in the Python programming language that is able to build **Non-deterministic Finite Automaton (NFA)** when given an input of a **regular expression (regex)**, and uses the **NFA** to determine whether the given **regex** matches any given string.

### Terminology:
1. Automata - Construct made of states that determines whether the input should be **accepted** or **rejected**. i.e. when the machine receives an input it looks at the *states* and picks a state to transition to based on the input it was given. Once there are no more inputs the automaton stops on a state and checks whether it will *accept* or *reject* the current set of inputs.
2. Regular Expressions (Regex) - A string and certain characters contain a special meaning. i.e * = Kleene Star, | = alternation, ? = Zero or One etc.
 - Example of a regex would be:
 - a.b|c* =  **a** followed by a **b** *OR* any number of **c's**, so a valid string would be either **ab** *or* **ccccccccc**, an invalid string could be **acb**, **ccccssss** etc.
3. Non-deterministic Finite Automaton (NFA) - an automaton is a self operating machine designed to follow a sequence of instructions. It takes in a string of inputs and for each symbol(character) it transitions to a new **State**.

### Useful Articles:
* [Basics of Automata Theory - Stanford.edu](https://cs.stanford.edu/people/eroberts/courses/soco/projects/2004-05/automata-theory/basics.html)
* [Automata Theory Wikipedia](https://en.wikipedia.org/wiki/Automata_theory#Very_informal_description)
* [NFA's Wikipedia](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton#Informal_introduction)



### Repository:
- Separated into 2 folders:
- study_research - contains links to useful articles I found while writing the program that explain the core concepts of the program.
- project - contains a sub-directory with all the main components of the program called *utils* and a run.py script which is used to run the program.

### Requirements:
 - [Python3](https://www.python.org/downloads/)
 
# Running the program
1. Install Python3 via the link above.
2. Clone the repository to your desired location via this command:
```
git clone https://github.com/ArnasSteponavicius00/graph_theory_project.git
```
3. Navigate to the project directory and run the program via one of these 2 ways:
```
1. python run.py
```
**OR**
```
2. python run.py -r "[regex]" -s [string]
```
*example of the 2nd method: **python run.py -r "(a.b)|c\*" -s ccccccc***
- The quotation marks for the regex string are very important as command line shells usually have the special characters used in a regex reserved for other actions, which when run without the quotes will cause errors in some scenarios.

# Tests
The utils folder also holds a test.py file, you can run the test file via the following command:  
```
python test.py
```
If all your test cases match the regex then the it will run without issue, if a string does not match a regex then an error message will be displayed showing which strings should match but don't.

### How it works:
```python
if __name__ == "__main__":
    tests = [
            ["a.b|b*", "bbbbbbb", True],
            ["a.b|b*", "bbbn", False],
    ]

    for test in tests:
        assert match(test[0], test[1]) == test[2], test[0] + \
        (" should match " if test[2] else " should not match ") + test[1]
```
The first thing we do is create an array, and the elements of the array will be a list that holds 3 items. As you can guess those 3 things will be the: 
- ["*regex*", "*string to match*", True/False], the True or False is to indicate whether the string should match or not.

The for loop just loops over the elements in the **tests** array, using the **assert** keyword we put the elements into a match() function, which will be covered further down and we check to see whether our match function returned the expected value we put it in our **tests** array.

# Main Algorithms
### state.py
This is the file that defines what a state is. Every state has 0, 1 or 2 *edges*. The class defines *edges* and a *label* for the edges. **Edges** can interpreted as arrows or transitions and the **Labels** are the values given to the edges. So if an edge has the value of "None (epsilon)" it will allow any character to transition along the edge to the next state.

### fragment.py
Uses **state.py** to define the start and accept states of the NFA fragment.

### shunting.py
Used to convert regular infix notation to postfix notation. The way we as people write numbers is in infix notation i.e "3 + 4 or 5 x 2 - (2 - 1)". For a computer this is hard to compute so we convert it to postfix notation. In postfix "3 + 4" now becomes "3 4 +" and "5 x 2 - (2 - 1)" becomes "5 2 2 1 - - x". The way it converts from infix to postfix is by using a stack and constantly pushing and popping symbols to and from the stack.
1. The first step is to take in a string in infix notation, add the symbols (characters) to a list and reverse it.

```python
def shunt(infix):
    """Convert an expression in infix notation to postfix notation
    :param infix: regular expression
    :type infix: string
    :return: infix converted to postfix
    """

    infix = list(infix)[::-1]
```

We then create 2 empty lists that will hold an operator stack and the newly converted postfix expression. We also give the operators that will be used a precedence by assigning them a value, this will determine where the operator will be in the stack once we start the conversion.
```python
 opstack, postfix = [], []
    
    # Operator precedence.
    precedence = {'*': 100, '?': 99,'+': 98, '.': 80, '|': 60, ')': 40, '(': 20}
```

2. The next thing that we do is we create a while loop that loops through the reversed infix list until there are no more characters left. We pop each character as we go along the list and decide what to do with the character based on what it is. If it is an operator character we append it to the **opstack** list and if it is a regular character we append it to the **postfix** list. Once there are no more characters left we then append operators to the **postfix** list and convert it to a string.

```python
    while infix:
        # Pop a character from the input
        print(f"STACK: {infix}")
        cChar = infix.pop()

        # Decide what to do based on the character
        if cChar == '(':
            # Push and open to the opstack stack
            opstack.append(cChar)

        elif cChar == ')':
            # Pop the operator stack until you find an opening bracket
            while opstack[-1] != '(':
                postfix.append(opstack.pop())
            # Get rid of the opening bracket
            opstack.pop()

        elif cChar in precedence:
            # Push any operators on the opstack with higher precedence to the output
            while opstack and precedence[cChar] < precedence[opstack [-1]]:
                postfix.append(opstack.pop())
            # Push cChar to the operator stack
            opstack.append(cChar)

        else:
            # Generally just push the character to the output.
            postfix.append(cChar)

    # Pop all operators to the output
    while opstack:
        postfix.append(opstack.pop())


    # Convert output list to String
    return ''.join(postfix)
```