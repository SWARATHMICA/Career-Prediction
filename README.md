# Career Recommendation System
This Django-based web application predicts the most suitable career path for a user based on their input, using a pre-trained machine learning model. The application incorporates preprocessing, scaling, and encoding to deliver precise recommendations.

# Features
Accepts user input through a simple web interface.
Predicts a career path using a Logistic Regression model.
Supports encoding of categorical features and standardization of numerical values.
Displays career recommendations with accuracy.

# Dataset
The application uses a dataset career prediction dataset from kaagle. Dataset has been uploaded in this repo.

# Data Preprocessing:
learning_style is one-hot encoded.
Missing values in ROLE are imputed using the mode.
Features are standardized using StandardScaler.

# Tech Stack
Backend: Django 5.1.3
Machine Learning: Logistic Regression
Frontend: Django templates, HTML, CSS
Dataset Preprocessing: Pandas, Scikit-learn
Model Storage: Joblib

# Installation and Setup
1. Clone the Repository
git clone https://github.com/SWARATHMICA/Career-Prediction.git
cd career-prediction

3. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

4. Install Dependencies
pip install -r requirements.txt

5. Run Migrations
python manage.py migrate

6. Start the Development Server
python manage.py runserver
Access the application at http://127.0.0.1:8000.

# How It Works
Input: Users provide details like their learning style, skills, and preferences.
Processing: Inputs are encoded and scaled using the trained preprocessing pipeline.
Prediction: The Logistic Regression model predicts the most suitable career role.
Output: The recommended career role is displayed to the user.

# Requirements
A requirements.txt file is included. 

# Output screenshots
![image](https://github.com/user-attachments/assets/6e9feeb3-9c9c-45ab-878c-2709c88126a8)
![image](https://github.com/user-attachments/assets/19bd3b87-b020-434c-99f2-3825f8cfa631)
![image](https://github.com/user-attachments/assets/b160a412-fb65-41e9-8977-9f58815a4aa1)



