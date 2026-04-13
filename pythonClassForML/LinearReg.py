import numpy as np

# linaerRegression class
class LinearRegression:
    def __init__(self,learning_rate=0.01,epochs=100):
        self.learning_rate=learning_rate
        self.epochs=epochs
        self.weight=0
        self.bias=0

    def predict(self,X):
        return self.weight*X +self.bias

    def compute_loss(self,y_true,y_pred):
        return np.mean((y_pred-y_true)**2)    
    
    def fit(self,X,y):
        n=len(X)
        for i in range(self.epochs):
            y_pred=self.predict(X)
            dw=(-2/n)*np.sum(X*(y-y_pred))
            db=(-2/n)*np.sum(y-y_pred)

            self.weight-=self.learning_rate*dw
            self.bias-=self.learning_rate*db

            if i%10==0:
                loss=self.compute_loss(y,y_pred)
                print(f"Epoch {i}, Loss: {loss:.4f},weight:{self.weight:.4f},{self.bias:.4f}")

    def evaluate(self,X,y):
        y_pred=self.predict(X)
        loss=self.compute_loss(y,y_pred)
        print(f"Final Loss: {loss:.4f}")

# creating some sample data
X=np.array([1,2,3,4,5], dtype=np.float32)     
y=np.array([2,4,6,8,10], dtype=np.float32)     

#creating an object of our class
model=LinearRegression(learning_rate=0.01,epochs=100)

# Train the model
model.fit(X,y)

#Evaluate the model
model.evaluate(X,y)

#Mark a prediction 
print("Predicted price for size 7",model.predict(7))