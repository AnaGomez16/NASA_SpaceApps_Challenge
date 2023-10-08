# FireGuardian - Fire and Natural Resource Monitoring Solution

![FireGuardian Logo](FG-logo-5.png)


## Api_request_meteomatics

### Description

This script is designed to retrieve weather data using the Meteomatics API for a specific location (in this case, the city of interest) and time period. It imports the necessary libraries, sets up the API credentials, defines the location coordinates, specifies the weather parameters of interest, and sets the date range for data retrieval.

### Key Components

- **Importing Libraries:** The script imports the required Python libraries, including `datetime` and `meteomatics.api` for working with date-time objects and making API requests, respectively. It also uses `pandas` for data manipulation.

- **API Request:** It sends a request to the Meteomatics API to retrieve weather data for the specified location, time period, and parameters.

- **Data Processing:** After receiving the data, the script adds a date-time column and coordinates columns to the dataset for better analysis and visualization.

- **Saving Data:** Finally, the script saves the processed data to a CSV file named 'data_Sevilla.csv'.

### Usage

To use this script, you need to replace `'username_example'` and `'password_example'` with your actual Meteomatics API credentials. You can modify the `coordinates`, `parameters`, `startdate`, `enddate`, and `interval` variables to customize the data retrieval for your specific needs.

Make sure to have the required libraries (`datetime`, `meteomatics.api`, and `pandas`) installed in your Python environment before running the script.

Feel free to adapt and integrate this script into your project as needed to fetch weather data for your desired location and time frame.
