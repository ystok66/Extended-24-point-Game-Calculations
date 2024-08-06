# Extended-24-point-Game-Calculations
Extended 24-point Game Calculations（24 puzzle） for Any Target with Square Roots, Factorials, and Exponentiation in Under 100 Lines



# Introduction

Standard 24-point game rules: The game is an arithmetical puzzle in which the objective is to find a way to manipulate four int so that the end result is 24. For example, for the numbers 4, 7, 8, 8, a possible solution is $$(7-(8/8))/*4$$.

This extended version supports square roots, factorials, and exponentiation operations. It is no longer limited to only four numbers; any target number can be specified. An iterative method has been designed to keep the code under 100 lines.

## Input Requirements
- **Element list:** Contains the numbers to be processed.
- **Operations list:** Allowed combinations of addition, subtraction, multiplication, division, exponentiation, and allowed independent operations like square roots and factorials.
- **Integer:** The target number.

## Note
Due to the iterative method and brute-force approach, adding an allowed computation method (square root, factorial, exponentiation) causes the computational cost to grow exponentially. Therefore, computing with multiple numbers might cause memory limitation (if someone finds issues when verifying with many numbers, please provide feedback). Additionally, there is currently a flaw where equivalent expressions are output, which should be easy to solve, but I have not had the time yet.

## Something Interesting
This project was inspired while watching my younger brother play the 24-point game. I thought, why not write a program? With the spirit of making something fun, I spent three hours one evening developing an extended version of the 24-point game. It turned out quite well, although I'm not sure about the thinking of my computer's memory, haha!
