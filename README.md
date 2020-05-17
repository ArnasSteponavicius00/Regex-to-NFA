# Graph Theory Project 3rd Year Sem 2

## Introduction
A program that builds an NFA (Non deterministic Finite Automaton) from a regular expression

## Setup Instructions
* Have Python 3.8 installed on your machine
```
git clone https://github.com/ArnasSteponavicius00/graph_theory_project.git
```
* Open cmd inside the cloned directory
```
cd project
```
* Run the following command - 1st way
```
python run.py
```
* OR via command line arguments - 2nd way
```
python run.py -r <regex string> -s <string>
```

## How to use:
- 1st way
1. Enter regular expression
2. Enter string you wish to compare
3. Result will return either ```True``` or ```False```
4. Choose between [y/n] | y - continue , n - exit.

- 2nd way
1. python run.py -r "regex string" -s [string]
2. Note: the regex string must be encased in quotation marks i.e 
3. ```python run.py -r "a.b|c*" -s cccccc```

## Author:
* Arnas Steponavicius

## References:
* [Ian McLoughlin](https://github.com/ianmcloughlin)
* [Articles Used](https://github.com/ArnasSteponavicius00/graph_theory_project/blob/master/study_research/RESEARCH.md)

