#!/usr/bin/python


def collect():
    pass

def pop():

    import numpy as np
    import pandas as pd


    cities = ['Berlin', 'Frankfurt', 'Hamburg',
            'Nuremberg', 'Munich', 'Stuttgart',
             'Hanover', 'Saarbruecken', 'Cologne',
              'Constance', 'Freiburg', 'Karlsruhe'
             ]

    n= len(cities)
    data ={'Temperature': np.random.normal(24, 3, n),
            'Humidity': np.random.normal(78, 2.5, n),
            'Wind': np.random.normal(15, 4, n)
           }
    df = pd.DataFrame(data=data, index=cities)
    df.to_csv("../assets/stats.csv")


pop()

