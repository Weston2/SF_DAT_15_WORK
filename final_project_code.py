# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:38:32 2015

@author: westonbuck
"""

import numpy as np
import pandas as pd
import glob
import geopy as geo

all_data = pd.DataFrame()
for f in glob.glob("/Users/westonbuck/Desktop/Permit*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)

print all_data.head()

all_data.info()

from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("185 Channel street, San Francisco")
print(location.address)
print((location.latitude, location.longitude))

