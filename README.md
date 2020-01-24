Unit testing/TDD tutorial

#Intro
Clone this repository to your local machine and check out the master branch
The goal of this exercise is to practice a small end-to-end development example. We will implement a simple virtual wallet ads described in src/wallet.py. 
In this file a setup is created of the class and functions that should be implemented.

##Step-by-step guide
1) Since our wallet should be interpreted as a physical wallet, there is a situation that might occur using the two defined functions. Create a custom exception for this to avoid this situation and give it an appropriate name.
2) Add static typing wherever necessary.
3) Write tests for the class to be implemented. Be torough: you want to make sure that you can rely on the fact that now anyone who implements the wallet and passes your tests did so correctly.
4) Implement the wallet.
5) Run tests and refactor wherever necessary
When you reached this point, both the tests and the actual implementation of the wallet should be working, now only a final check remains.
6) Check your code coverage.
7) compare your work to the example answer on the example_answer branch.


