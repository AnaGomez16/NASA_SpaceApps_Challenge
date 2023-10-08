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

# IA Predict Images File

This Python script uses a pre-trained deep learning model to make predictions on an input image. It performs the following tasks:

1. **Loading Pre-trained Model:** The script loads a pre-trained deep learning model using Keras. This model is ready for making predictions without the need for further compilation.

2. **Loading Labels:** It loads a list of class labels from a file called "labels.txt." These labels correspond to the categories that the model can recognize.

3. **Preparing Input Image:** The script loads an image from a specified path and prepares it for prediction. It resizes the image to a size of 224x224 pixels and normalizes the pixel values.

4. **Making Predictions:** The script feeds the prepared image to the loaded model and predicts the class label for the image along with a confidence score.

5. **Displaying Prediction:** The predicted class and confidence score are printed to the console.

To use this script, you need to have TensorFlow and Keras installed in your Python environment. Ensure that you have a pre-trained model saved as "keras_Model.h5" and a file containing class labels as "labels.txt" in the same directory as the script.

Replace `<IMAGE_PATH>` with the actual path to the image you want to make predictions on. The script will print the predicted class and confidence score for that image.

Feel free to integrate this script into your image classification project and adapt it as needed.


# ML Model File

This Python script performs classification using several machine learning models and evaluates their performance. It includes the following tasks:

1. **Model Initialization:** The script initializes a Gradient Boosting Classifier (`GradientBoostingClassifier`) with specified hyperparameters.

2. **Model Training and Evaluation:** It trains the Gradient Boosting Classifier on the provided data (`X_transformed`) and labels (`y`) using a custom function called `train_predict_test`. This function fits the model, makes predictions, and evaluates the model's performance using various metrics.

3. **List of Models:** The script defines a list of machine learning models, including Random Forest, Logistic Regression, AdaBoost, LightGBM, XGBoost, and K-Nearest Neighbors (KNN).

4. **Model Evaluation:** The `train_predict_test` function is then used to train and evaluate each model in the list. The function fits the model to the data, makes predictions, and prints out evaluation metrics for each model.
