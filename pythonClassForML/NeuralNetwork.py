import numpy as np

# Activation Functions
def sigmoid(x):
    return  1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))

def relu(x):
    return np.maximum(0,x)

def relu_derivative(x):
    return (x>0).astype(float)

class SimpleNeuralNetwork:
    def __init__(self,input_size=2,hidden_size=2,learning_rate=0.1,epochs=100):
        #initialize weights and biases
        self.w1=np.random.randn(input_size,hidden_size)
        self.b1=np.zeros((1,hidden_size))
        self.w2=np.random.randn(hidden_size,1)
        self.b2=np.zeros((1,1))
        self.lr=learning_rate
        self.epochs=epochs 

    def forward(self,X):
        # Forward pass
          self.z1=np.dot(X,self.w1)+self.b1
          self.a1=relu(self.z1) 
          self.z2=np.dot(self.a1,self.w2) +self.b2
          self.a2=sigmoid(self.z2)
          return self.a2
    def compute_loss(Self,y_true,y_pred):
        # Binary cross-entropy loss
        return -np.mean(y_true*np.log(y_pred+1e-8)+(1-y_true)*np.log(1-y_pred+1e-8))    
    
    def backward(self,X,y_true,y_pred):
        # Backward pass
        m=X.shape[0]

        dz2=y_pred-y_true
        dw2=np.dot(self.a1.T,dz2)/m
        db2=np.sum(dz2,axis=0,keepdims=True)/m

        dz1=np.dot(dz2,self.w2.T)*relu_derivative(self.z1)
        dw1=np.dot(X.T,dz1)/m
        db1=np.sum(dz1,axis=0,keepdims=True)/m

        #update weights and biases
        self.w2-=self.lr*dw2
        self.b2-=self.lr*db2
        self.w1-=self.lr*dw1
        self.b1-=self.lr*db1
    
    def fit(self,X,y):
        for i in range(self.epochs):
            y_pred=self.forward(X)
            loss=self.compute_loss(y,y_pred)
            self.backward(X,y,y_pred)
            if i%200==0:
                print(f"Epoch {i}, Loss: {loss:.4f}")

    def predict(self,X):
        probs=self.forward(X)
        return (probs>0.5).astype(int)   

# Create dataset
np.random.seed(0)
X=np.random.rand(100,2)
y=(X[:,1]>X[:,0]).astype(int).reshape(-1,1)

#initialize and train model
nn=SimpleNeuralNetwork(epochs=1000)
nn.fit(X,y)

# Predict on a few points
test_points=np.array([[0.2,0.8],[0.9,0.1],[0.4,0.5]])
predictions=nn.predict(test_points)
print("Predictions:",predictions)