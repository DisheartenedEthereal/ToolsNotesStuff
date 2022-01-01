#imports
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
#import
genres = pd.read_csv("/home/disheartenedethereal/Projects/Machine_learning/Spotify-analysis/genres.csv")
genres
os.system("ls")
#split data


#joblib to save memory
