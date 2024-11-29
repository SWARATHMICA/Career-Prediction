import joblib
import numpy as np
import pandas as pd

def predict_career(features):
    # Load the saved model and components
    model_data = joblib.load('career_model.pkl')
    model = model_data['model']
    scaler = model_data['scaler']
    dummy_columns = model_data['dummy_columns']  # Load the dummy column names

    # Extract and encode the 'learning_style' feature
    learning_style = features.pop(-5)  # Extract 'learning_style' (last feature in the list)
    learning_style_encoded = pd.get_dummies([learning_style], drop_first=True)
    learning_style_encoded = learning_style_encoded.reindex(columns=dummy_columns, fill_value=0)

    # Combine with other features
    features = np.array(features).reshape(1, -1)  # Reshape the remaining features
    full_features = np.hstack((features, learning_style_encoded.values))  # Combine arrays

    # Apply scaling
    full_features_scaled = scaler.transform(full_features)

    # Perform prediction
    prediction = model.predict(full_features_scaled)

    return prediction[0]  # Return the predicted role
