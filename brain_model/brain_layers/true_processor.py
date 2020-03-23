from brain_layers.automatic_functions import *
import tensorflow as tf
import keras as keras
class TrueProcessor:
    # List of pre-trained models loaded from .hdf5 files
    models = []
    def __init__(self):
        trained_models = 0
    
    def add_model(self, model):
        self.models.append(keras.models.load_model(model))
    
    def predict_input(self, data):
        return self.models[0].predict(data)

    def convert_data(self, data):
        # Convert incoming image/sound data into tensors
        return 0
