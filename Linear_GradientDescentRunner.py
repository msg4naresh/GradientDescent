from numpy import *
def costFunction(theta0,theta1,data):
   
    totalError=0
    for i in range(0, len(data)):
         y=data[i,1]
         x=data[i,0]
         totalError+=(y-(theta1*x+theta0))**2
    print(totalError/float(len(data)))
    
def gradientDescent(theta0,theta1,data,learningRate):
    derivativetheta0=0
    derivativetheta1=0
    for i in range(0,len(data)):
        y=data[i,1]
        x=data[i,0]
        derivativetheta0+=-(2*(y-(theta1*x+theta0)))/len(data)
        derivativetheta1+=-2*x*(y-(theta1*x+theta0))/len(data)
    theta0=theta0-(learningRate*derivativetheta0)
    theta1=theta1-(learningRate*derivativetheta1)
    return[theta0,theta1]

def gradientDescentConverger(theta0,theta1,data,leraningrate,iterations):
   
    for i in range(0,iterations):
     [theta0, theta1]=gradientDescent(theta0,theta1,data,leraningrate)
    
    return[theta0,theta1]
    
        
def run():
    data=genfromtxt("data.csv", delimiter=",")
    learningRate=0.0001
    theta0=24
    theta1=14
    iterations=200
    costFunction(theta0,theta1,data)
    [theta0, theta1]=gradientDescent(theta0,theta1,data,learningRate)
    [theta0, theta1]=gradientDescentConverger(theta0,theta1,data,learningRate,iterations)
    print(theta0)
    print(theta1)
    costFunction(theta0,theta1,data)
   
if __name__ == '__main__':
    run()