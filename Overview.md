## Introduction
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
## Run
1. Install Python3 via the link above.
2. Clone the repository to your desired location via this command:
```
git clone https://github.com/ArnasSteponavicius00/graph_theory_project.git
```
3. Navigate to the project directory and 