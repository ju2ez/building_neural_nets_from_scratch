"""
example of a Feed Forward Neural Network    



"""

import numpy as np

from time import sleep



class neuralNetwork(): 
        def sigmoid(x):
                return 1 /(1+ np.exp(-x))


        def sigmoid_derivative(x):
                return x * (1-x)


        def relU(x):
               return np.maximum(0,x)

        def relU_derivative(x):
                x[x<=0] = 0
                x[x>0] = 1 
                return x


        training_inputs = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
        more_training_inputs = np.array ([[1,1,0],[0,1,0],[1,1,0]])
        training_outputs= np.array([0,1,1,0]).T
        more_training_outputs = np.array([1,0,1]).T


        training_inputs=np.concatenate((training_inputs,more_training_inputs))
        training_outputs=np.concatenate ((training_outputs,more_training_outputs))

        print ('training_outputs:\n',training_outputs)

        np.random.seed(1)
 
        synaptic_weights= 2* np.random.random((3,1))
            
        print ("training input:")
        print (training_inputs)

        print("random synaptic weights are")
        print (synaptic_weights)

        for iteration in range (200000):
                input_layer = training_inputs
                outputs = sigmoid(np.dot(input_layer, synaptic_weights))
                #outputs = relU(np.dot(input_layer, synaptic_weights))
                error = training_outputs - outputs.T
               # print ('error:',error)
                #print ('weights:',synaptic_weights)
                adjustments = np.dot(training_inputs.T, error.T * sigmoid_derivative(outputs))
              #  adjustments = np.dot(training_inputs.T, 0.0000005*error.T * relU_derivative(outputs))
                synaptic_weights+=adjustments
                #print ('expected outputs:',training_outputs)
                #print ('outputs: ',np.round(outputs.T,decimals=3))
                #sleep(.4)
        print ("synaptic weights after training:")
        print ( synaptic_weights)
        print ("expected outputs",training_outputs)
        print ("outputs after training: ")
        print (np.round(outputs.T,decimals=3))
        print ("now test the function...")
        test_vector= np.array([1,0,0])
        output = relU_derivative(relU(np.dot(test_vector, synaptic_weights)))
        print ('prediction:',output)
