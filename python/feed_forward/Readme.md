# Feed-Forward Neural Network written in Python 
The neural network is build up using a single perceptron receiving three binary input values (+weights)

1
--w1-->   |---------------|
1         | SUM(wi*xi)    |
--w2-->   |         relU->|--------> y^----|
0         |               |                |
--w3-->   |               |                | error = expected_output - y^ (actual_output)
  /\       ---------------                 |
  --------------<-------------<-------------
              readjust (backpropagation)



Two activation functions are implemented (relU and sigmoid) and can be used.


The input features look like this:
input (4x1 vector)        expected output (label)

0 0 0                     0

0 1 1                     0

1 0 0                     1

1 1 1                     1



test with the input: 

1 0 1  ---> output should be a 1 since the output depends on the first value of the input vector 
–



The class is "losely" programmed. No explicit method extracation or good isolation / pep8 style.


