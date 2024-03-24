#HOLY I DID IT!!!



import random
from matplotlib import pyplot as plt
#MWAHAHAHA I IMPORTED MATHS NOW PHYSICS DONT WORK ONLY MATHS!
import math
#dataSet
#please note that for this code runs on python and that pyplot is not nessacary for the ai to work but it is very helpful as it shows where the ai organizes the circles and lets you see its progress more clearly and interestingly than a percentage would


dataSet = []

amountOfData = 1000

tempCircle = []

tempCircleList = [ ]

colours = ["Yellow","Red","Green","Blue","Black"]
tempColourList = []

maxRadiiSize = (1,10)



for ListOfCircles in range(amountOfData):
    tempCircleList = []
    for Circle in range(50):
        #give it random x and y colour and radii
        tempCircle = []
        tempCircle.append(random.choice(colours))
        tempCircle.append(random.uniform(*maxRadiiSize))
        if tempCircle[0] == "Yellow":
            tempCircle.append(0)
        elif tempCircle[0] == "Red":
            tempCircle.append(1)
        elif tempCircle[0] == "Green":
            tempCircle.append(2)
        elif tempCircle[0] == "Blue":
            tempCircle.append(3)
        elif tempCircle[0] == "Black":
            tempCircle.append(4)
        #list of circles is the index the list of circles is, circle is the circle 0 is representing the input value while if it was the true correct value the ai should have put it in it would be 1
        tempCircleList.append(tempCircle)
        #creating the correct spot for each circle to be
    

    tempColourList = []
    #sort the list by alphabetical order !!!! :D im so happy i dont have to do this myself lmaooo
    tempColourList = sorted(tempCircleList,reverse = True)
    #b is weird dont question it
    #b is offset so it doesnt put the correct red pos in yellow bc it goes through all the circles in order and doesnt start at the right colors which is why b is neccesary, spaghetii code :D
    #i is essentialy if the Colour variable was a number instead of a colour
    b = 0
    i = 0
    for Colour in colours:
        i += 1
        for Circle in range(sum(1 for entry in tempColourList if entry[0] == Colour)):
            #put in the count the colour is so yellow would be 0 bc it goes in the first coloumn and red would be 1 bc it goes in the second colum dbasjhbdjhsambdh :D 
            tempColourList[Circle+b].append(i*25)
            tempColourList[Circle+b].append((Circle+1)*20)
        b += sum(1 for entry in tempColourList if entry[0] == Colour)
    tempCircleList = tempColourList

    






    
    dataSet.append(tempCircleList)


#shows the 696 data set on a pyplot graph

'''print(dataSet[696][5])
fig, ax = plt.subplots()
for ad in range(50):
    Circle = plt.Circle((dataSet[696][ad][2],dataSet[696][ad][3]),dataSet[696][ad][1],fill=True,color = dataSet[696][ad][0])
    ax.add_artist(Circle)
ax.set_aspect("equal")
#ax.set_xlim(0, 1)
#ax.set_ylim(0, 1)
plt.show()'''



def Relu(x):
    return(max(0,x))

def Sigmoid(x):
    return 1 / (1 + math.exp(-x))


#ai Class
class Neuron():
    def __init__(self,Weight,Bias):
        self.weights = Weight
        self.bias = Bias
        self.bestWeights = 0
        self.bestBias = 0
        self.output = []
        self.weightCount = len(self.weights)
        self.tempBestThing = 0
    def calc(self,Input):
        self.output = []
        for Weight in self.weights:
            self.output.append(Input*Weight)
       # print(self.output)
        return(self.output)
    def BecomeAnew(self,mutationValue):
        self.weights = []
        if self.bestWeights != 0 and mutationValue != 0:
            for index in range(self.weightCount):
                self.tempBestThing = random.uniform(-1,1)
                self.weights.append(self.tempBestThing + ((self.bestWeights[index] - self.tempBestThing) * (mutationValue/100)))
        else:
            
            for index in range(self.weightCount):
                self.weights.append(random.uniform(-1,1))
                #print("weight:")
                #print(self.weights)
        if self.bestBias != 0 and mutationValue != 0:
            self.tempBestThing = random.uniform(-1,1)
            self.bias = self.tempBestThing + ((self.bestBias - self.tempBestThing) * (mutationValue/100))
        else:
            self.bias = random.uniform(-1,1)
class Layer():
    def __init__(self,neurons,futureNeurons):
        self.neurons = []
        self.ScaledTempOutput = 0
        self.calcOutput = []
        self.OutputCalcOutput = []
        self.tempOutput = 0
        for neuron in range(neurons):
            self.tempNeuron = Neuron([random.uniform(-1,1) for i in range(futureNeurons)],random.uniform(-1,1))
            self.neurons.append(self.tempNeuron)

    def layercalc(self, Input):
        #print(len(self.neurons))
        self.calcOutput = []
        neuronOutput = 0
        self.tempOutput = 0
        for PrevLayerOutput in Input:
            neuronOutputs = []
            for indexedNeuronInList in self.neurons:
                neuronOutput = indexedNeuronInList.calc(PrevLayerOutput)
                neuronOutputs.append(neuronOutput)
        for index, output in enumerate(neuronOutputs):
            self.tempOutput = 0
             
            for value in range(len(neuronOutputs[0])):
                self.tempOutput += output[value]
            self.calcOutput.append(Sigmoid(self.tempOutput+self.neurons[index].bias))
        return(self.calcOutput)
    def Reset(self,mutationValue):
        for Neuron in self.neurons:
            Neuron.BecomeAnew(mutationValue)
    def outputLayerCalc(self,minOutput,maxOutput,newMax,newMin,Input):
        scaledOutput = []
        self.tempOutput = 0
        self.OutputCalcOutput = []
        scaledOutput = self.layercalc(Input)
        #print(scaledOutput)
        for val in scaledOutput:
            self.tempOutput = (val - minOutput) * (newMax - newMin) / (maxOutput - minOutput) + newMin
            self.OutputCalcOutput.append(self.tempOutput)
        return(self.OutputCalcOutput)


        

class NeurelNetwork():
    def __init__(self,hiddenLayersPlusNeuronsForLayers,possibleOutputs,learningRate):
        self.layers = []
        self.tempLayer = Layer
        self.mutationValue = 0
        for iteration, layer in enumerate(hiddenLayersPlusNeuronsForLayers):
            self.tempLayer = Layer(layer,hiddenLayersPlusNeuronsForLayers[iteration+1])
            self.layers.append(self.tempLayer)
            if iteration == len(hiddenLayersPlusNeuronsForLayers)-2:
                break
        self.tempLayer = Layer(hiddenLayersPlusNeuronsForLayers[-1],possibleOutputs)
        self.layers.append(self.tempLayer)
        self.minOutput = 0
        self.maxOutput = 600
        self.tempLearningOutput = 0
        self.layerOutput = 0
        self.tempLayerOutput = 0
        self.tempPercentageDeviation = 0
        self.tempPercentageAvrgCount = 0
        self.percentageDeviation = 0
        self.BestPercentageDeviation = float('inf')
        self.time = 0
    def UseBrain(self,Input):
        self.tempLayerOutput = self.layers[0].layercalc(Input)
        for layer in self.layers[1:-1]:
            self.tempLayerOutput = layer.layercalc(self.tempLayerOutput)
        self.layerOutput = self.layers[-1].outputLayerCalc(0,1,self.maxOutput,self.minOutput,self.tempLayerOutput)
        #print(self.layerOutput)
        return(self.layerOutput)
    def Spanking(self,mutationValue):
        for layer in self.layers:
            layer.Reset(mutationValue)
    def GoToSchool(self,InputDataSet,YearsOfLearning):
        for Year in range(YearsOfLearning):
            self.time += 1
            if self.time >= YearsOfLearning/100:
                print("It is now", round(Year/YearsOfLearning*100), "% through the learning procces")
                self.time = 0
            if Year == round(YearsOfLearning * 0.25):
                print("mutationValue is now 75%")
                self.mutationValue = 75
            elif Year == round(YearsOfLearning * 0.5):
                print("mutationValue is now 50%") 
                self.mutationValue = 50
            elif Year == round(YearsOfLearning * 0.75):
                print("mutationValue is now 25%")
                self.mutationValue = 25 
            elif Year == round(YearsOfLearning * 0.9):
                print("mutationValue is now 5%")
                self.mutationValue = 5
            self.tempLearningOutput = 0
            self.tempPercentageAvrgCount = 0
            self.tempPercentageDeviation = 0
            self.percentageDeviation = 0
            for circle in random.choice(InputDataSet):
                self.tempLearningOutput = self.UseBrain([circle[2],circle[1]])
                for index, output in enumerate(self.tempLearningOutput):
                    self.tempPercentageDeviation += abs((circle[index+3] - output) / circle[index+3]) * 100
                    self.tempPercentageAvrgCount += 1
            self.percentageDeviation = self.tempPercentageDeviation / self.tempPercentageAvrgCount
            if self.percentageDeviation < self.BestPercentageDeviation:
                for layer in self.layers:
                    for neuron in layer.neurons:
                        neuron.bestWeights = neuron.weights
                        neuron.bestBias = neuron.bias
                print(f"The New Best Percentage Deviation is : {round(self.percentageDeviation)}%")
                self.BestPercentageDeviation = self.percentageDeviation
            self.Spanking(self.mutationValue)
            




brain = NeurelNetwork([2,10,2],2,1)
#brain.UseBrain([1,1])
brain.GoToSchool(dataSet,4320000)




