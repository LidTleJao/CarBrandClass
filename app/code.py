import pickle
import numpy as np

class_brand = {0:'Audi', 1:'Hyundai Creta', 2:'Mahindra Scorpio', 3:'Rolls Royce',
               4:'Swift', 5:'Tata Safari', 6:'Toyota Innova'}


def predict_brand(model,hog):
    brand = model.predict(np.array(hog).reshape(1,-1))
    return {'brand':class_brand[brand[0]]}