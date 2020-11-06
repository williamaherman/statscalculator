[![Build Status](https://travis-ci.com/williamaherman/statscalculator.svg?branch=main)](https://travis-ci.com/williamaherman/statscalculator)


Overview
For this project you need to work in a team of 2-3 people to create a statistical calculator.  

You need to create a project plan that includes:

1.  A diagram or outline showing how each of the statistical and calculator functions relate to each other.  This should help you plan the order of the tasks.  You should show your instance class, static method class that "Wraps" calls the static functions, and the individual class and function for each operation.

For example

Calculator Object
Properties
Result 
Methods
Addition -> Calls addition static method from math operations
Subtraction -> Call subtraction static method from Math operations
Math Operations Static Class
Methods
Addition -> Calls addition class method of sum
Subtraction->Calls subtraction class method of difference
Operations class(s)
Addition
Methods 
Sum 1 numbers
Sum List of numbers
Subtraction
Methods
Subtract 2 numbers
2.  A list of task that break each development task down to the function level.  Each task requires a description, formula, and an example of the formula with data and the result of the calculation.  

3.  A Gitub Repository and a Project that has a 4 column chart: Todo, In progress, Review, Done.  

ToDo Shows your Tasks List
In progress needs to show the task assigned to a developer
Review needs to be for pull requests to review and who did the review
Done is for complete tasks
Program Requirements
Demonstrate inheritance by extending the calculator
Demonstrate encapsulation by having the calculator have methods and a result property
Demonstrate abstraction by layering your code and using static methods.  Object methods should call static methods to perform the operation.
Check values for being valid numbers and not strings
Throw an exception for divide by zero 
Throw exception for empty list
Use random data for tests and be able to increase the number of calculations required i.e. be able to increase the list of numbers that the mean calculation is done on.  You can actually use built in libraries or 3rd party libraries to check your calculations that you complete yourself.  i.e. you can use the standard deviation function from a stats library to compute the correct value for your list of random numbers and then use that to test that your own calculation is correct for that list.
Random Generator function

Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
Select a random item from a list
Set a seed and randomly.select the same value from a list
Select N number of items from a list without a seed
Select N number of items from a list with a seed
Population Sampling functions

Simple random sampling
Confidence Interval For a Sample
Margin of Error
Cochran’s Sample Size Formula
How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
Descriptive Statistics functions

Mean
Median
Mode
Variance
Standard Deviation
Z-Score
Additional Modules

Helper Functions (Functions you use for checking types or performing repeated operations)
Random Number Generator
Submission Instructions
For this project you need to submit a link to the repository on GitHub that has a build icon from Travis that shows passing.  On your Readme file, you should include your project task list and program diagram or outline.  Your readme should show the partners that worked on the project and what they did.  You can use more than one page by making additional text files and linking to them.  

Grading
1.  25 Points - Team Work i.e. task completion and usage of the project management tools on GitHub

2.  25 Points - Documentation i.e. are your documents accurate to the code and tasks

3.  50 Points - Code i.e. Meeting project requirements and having a working program with the correct structure.