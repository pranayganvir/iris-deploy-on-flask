
# Iris Flower Classification ☘️

The Iris Flower Classification Project is a web-based application developed using Flask, designed to demonstrate the use of machine learning models for predicting the species of the Iris flower based on its physical attributes. The project leverages the widely-used Iris dataset, which contains 150 records of flowers categorized into three species: Setosa, Versicolor, and Virginica. Each record includes four features: sepal length, sepal width, petal length, and petal width.

# ## Features 🛠️

- **Machine Learning Model**:
  - Trained using the Iris dataset.
  - Implements algorithms such as Random Forests Classifier.
  - Provides high accuracy with appropriate evaluation metrics.

- **Web Interface**:
  - User-friendly form to input flower measurements.
  - Displays predictions in real-time.
  - Optional insights and visualizations about the model and dataset.

- **Flask Framework**:
  - Backend server for handling requests and predictions.
  - Lightweight and easy to deploy.

- **Deployment-Ready**:
  - Ready to be hosted on platforms like Heroku, AWS, or Azure.
  - Modular and maintainable codebase.

---



# Working of the Project 

- The program takes data from the load_iris() function available in sklearn module.
- The program then creates a decision tree based on the dataset for classification.
- The user is then asked to enter the four parameters of his sample and prediction about the species of the flower is printed to the user.

## Installation

### Prerequisites
- Python 3.8 or higher
- Flask
- Scikit-learn
- Pandas
- Numpy
- Matplotlib (optional for visualizations)

--- 

## **Getting Started** 🚀 
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iris-ml-flask.git
   cd iris-ml-flask
   ```

2. Create and activate a virtual environment:
``` bash
python -m venv venv
venv\Scripts\activate
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask application:
```bash
python app.py
```
The application will be available at http://127.0.0.1:5000/.

---

## Usage
- Open the web application in your browser (http://127.0.0.1:5000/).
- Enter the sepal length, sepal width, petal length, and petal width of the flower.
- Click the Predict button to see the predicted species.

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)



