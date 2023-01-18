# LSTMS
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

class lstm:
    
    def __init__(self, X_train, y_train):

        self.x = X_train
        self.y = y_train
        
        self.model = Sequential()
        self.model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
        self.model.add(Dropout(rate=0.2))

        self.model.add(LSTM(units=50, return_sequences=True))
        self.model.add(Dropout(rate=0.2))

        self.model.add(LSTM(units=50, return_sequences=True))
        self.model.add(Dropout(rate=0.2))

        self.model.add(LSTM(units=50, return_sequences=False))
        self.model.add(Dropout(rate=0.2))

        self.model.add(Dense(units=1))
        self.model.compile(optimizer='adam', loss='mean_squared_error')

        print("Architecture of the Multi Stack LSTM Layer is ready!")

    def train_it(self):
        self.model.fit(self.x, self.y, batch_size=32, epochs=20)

        return self.model

    def predict_it(self, data):
        lst = self.model.predict(data)

        return lst


