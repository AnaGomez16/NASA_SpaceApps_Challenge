# FireGuardian - Fire and Natural Resource Monitoring Solution

![FireGuardian Logo](FG-logo-5.png)


# Api request meteomatics File

This script is designed to retrieve weather data using the Meteomatics API for a specific location (in this case, the city of interest) and time period. It imports the necessary libraries, sets up the API credentials, defines the location coordinates, specifies the weather parameters of interest, and sets the date range for data retrieval.

- **Importing Libraries:** The script imports the required Python libraries, including `datetime` and `meteomatics.api` for working with date-time objects and making API requests, respectively. It also uses `pandas` for data manipulation.

- **API Request:** It sends a request to the Meteomatics API to retrieve weather data for the specified location, time period, and parameters.

- **Data Processing:** After receiving the data, the script adds a date-time column and coordinates columns to the dataset for better analysis and visualization.

- **Saving Data:** Finally, the script saves the processed data to a CSV file named 'data_Sevilla.csv'.

To use this script, you need to replace `'username_example'` and `'password_example'` with your actual Meteomatics API credentials. You can modify the `coordinates`, `parameters`, `startdate`, `enddate`, and `interval` variables to customize the data retrieval for your specific needs.

Make sure to have the required libraries (`datetime`, `meteomatics.api`, and `pandas`) installed in your Python environment before running the script.

Feel free to adapt and integrate this script into your project as needed to fetch weather data for your desired location and time frame.

# Data Cleaning meteomatics File

This Python script is designed for data processing and manipulation. It performs the following tasks:

1. **Importing Libraries:** The script imports essential libraries, including `pandas` and `numpy`, for data manipulation and numerical operations.

2. **Loading Datasets:** It loads several datasets from different sources, including Meteomatics and individual CSV files for different regions such as Madrid, Asturias, Cantabria, Galicia, Murcia, Navarra, and Sevilla. These datasets likely contain weather or meteorological data.

3. **Data Transformation:** The script defines two functions for data transformation. 
   - `change_colum_datetime`: Splits the 'Fecha_Hora' column into two separate columns, 'Fecha' and 'Hora', and removes the original 'Fecha_Hora' column.
   - `change_time`: Converts the 'Hora' column to a string, and then extracts the first two characters to keep only the hour part.

4. **Applying Data Transformation:** The defined transformation functions are applied to the loaded dataframes for each region.

5. **Saving Data:** The modified dataframes are then saved as separate CSV files for each region, effectively updating the existing files with the transformed data.

To use this script, you need to ensure that you have the required libraries (`pandas` and `numpy`) installed in your Python environment. You should also have the necessary CSV files (e.g., 'datos_meteorologicos_madrid_2020.csv' and others) in the same directory as the script.

You can modify the script to work with other datasets or customize the data transformation functions to suit your specific needs. Make sure to provide the correct file paths for your datasets.

Feel free to integrate and adapt this script into your data processing workflow as needed.
