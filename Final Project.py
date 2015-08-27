"""
Created on Mon Aug  3 20:46:09 2015
@author: westonbuck
"""


#-------------------------------------------------------------------
#import needed modules
import numpy as np
import pandas as pd
import geopy as geo
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.cross_validation import cross_val_score

#takes an address and converts it to a lat / long for KNN grouping
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("185 Channel street, San Francisco")
print(location.address)
print((location.latitude, location.longitude))

# Loads crime data - From SF open data. 190MB
crime_data = pd.read_csv("CrimeData.csv") 
crime_data.info()    
crime_data.head()
crime_data
#Truncates the data to a manageable size
recent_crimes = crime_data[crime_data.Date.str.contains('2015')]
recent_crimes.info()

#breaks down a single day into 4 divisions and creates a new feature
recent_crimes.Time = pd.to_datetime(recent_crimes.Time)

def dtConvert(dt):
    if dt.hour < 6:
        return 'late night'
    elif dt.hour < 12:
        return 'morning'
    elif dt.hour < 18:
        return 'afternoon'
    else:
        return 'evening'

#selects distinct columns
selected = recent_crimes.loc[:, ['Category','X', 'Y', 'DayOfWeek', 'PdDistrict', 'Time']]
selected.info()

#Defines 4 features, weekday, time, and lat/long
recent_crimes['Time'] = recent_crimes.Time.apply(dtConvert)

#creates integers and ignores the x and y
x = pd.get_dummies(recent_crimes[['DayOfWeek', 'Time','X','Y']])
y = recent_crimes['Category']

#Feature = Category››
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.cross_validation import train_test_split

# Scaling Values to de-mean to 0 and std dev 1
#scalar = StandardScaler()
#X_scaled = scalar.fit_transform(X)

knn_model = KNeighborsClassifier(n_neighbors=20)
x_train, x_test, y_train, y_test = train_test_split(x, y)
knn_model.fit(x_train, y_train)  

#predict accuracy
y_train_preds = knn_model.predict(x_train)
y_test_preds = knn_model.predict(x_test)

#Accuracy for training set 50% @n=3
float((y_train_preds == y_train).sum()) / len(y_train)

#Accuracy for testing set 25% @n=3
float((y_test_preds == y_test).sum()) / len(y_test)

#Find the most accurate N (1=starting N, 30=ending N, 2=skips every other)
k_range = range(1, 30, 2)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores.append(np.mean(cross_val_score(knn, x, y, cv=5, scoring='accuracy')))
scores

#list features
x_test.columns
#Dictionary
#1) Lat, 2) Long, 3) Fri, 4) Mon, 5) Sat, 6) Sun, 7) Thurs
#8) Tues 9) Wed 10) Afternoon 11) Evening 12) Night 13) Morning

#Runs Model
knn_model.predict([37.77408, -122.390142437182, 0,0,0,0,0,0,1,0,1,0,0])  

# Try Decision tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
tree_model = DecisionTreeClassifier(max_depth=5)
tree_model.fit(x_train, y_train)  
y_preds = tree_model.predict(X_test)
float((y_preds == y_test).sum()) / len(y_preds)

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, max_depth=20)
rf_model.fit(x_train, y_train)  
y_preds = rf_model.predict(x_train)

float((y_preds == y_test).sum()) / len(y_preds)
 
pd.DataFrame(zip(X.columns, rf_model.feature_importances_)).sort_index(by=1, ascending=False)







