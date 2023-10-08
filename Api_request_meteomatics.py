import datetime as dt
import meteomatics.api as api
import pandas as pd

username = 'username_example'
password = 'password_example'

# cordinates of the city of Interest
coordinates = [(37.3886303,-5.9953403)]
# Parameters of interest
parameters = ['t_2m:C', 'precip_1h:mm', 'wind_speed_10m:ms']
model = 'mix'
startdate = dt.datetime(2020, 1, 1, 0, 0)  # Fecha de inicio para el año 2020
enddate = dt.datetime(2020, 12, 31, 23, 59)  # Fecha de fin para el año 2020
interval = dt.timedelta(hours=1)

# api request
df = api.query_time_series(coordinates, startdate, enddate, interval, parameters, username, password, model=model)

# add timedate column
df['Fecha_Hora'] = pd.date_range(startdate, enddate, freq=interval)

# add coordinates column
df['Latitud'] = coordinates[0][0]
df['Longitud'] = coordinates[0][1]

# save data
df.to_csv('data_Sevilla.csv', index=False)