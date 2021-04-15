from tensorflow.keras.models import load_model
import os

def load():

    dirname = os.path.dirname(__file__)
    modelpath = os.path.join(dirname, 'lstm2')
    return load_model(modelpath)
    #return load_model('/home/paredes/IdeaProjects/store0/src/store0/lstm2')