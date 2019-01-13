""" this class creates a simple "artificial neuron". 
the neuron can get some inputs (values and weight).
Also it contains the summation function for the inputs and
the activation function to forward the output"""

import math as math

class Neuron:
        

       

        #sigmoid activation function
        def activation_function_sigmoid(self,x):
                output= float ( 1. / (1+ math.pow(math.e,-x)))
                return output
        
        #RelU activation function
        def activation_function_relu(self,x):
                return max(0,x)

       
       #input function of the neuron (our neuron can receive three values as input)
        def input(self, feature_1, feature_2, feature_3):
                weighted_feature_1 = feature_1 * weight_1 
                weighted_feature_2 = feature_2 * weight_2 
                weighted_feature_3 = feature_3 * weight_3 
                return true

        
        #sum up the input values def summation(self,x):
                return true

        #forward the value (the neurons output)
        def output(self,x):
                return true

        def set_weigths (self, weight_1, weight_2, weight_3):
                self.weight_1 = weight_1
                self.weight_2 = weight_2  
                self.weight_3 = weight_3 
                return true




if __name__ == "__main__":
    print ("testing my class")
    neuron = Neuron()
    print ("the output of the sigmoid function for value 2 is:",neuron.activation_function_sigmoid(2))
    print ("the output of the relu function for value -1 is :",neuron.activation_function_relu(-1))

