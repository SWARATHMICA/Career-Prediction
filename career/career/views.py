from django.shortcuts import render
from .forms import PredictionForm
from .ml_model import predict_career  # Assuming you've created this function in a separate Python file

def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get cleaned data from form
            form_data = form.cleaned_data

            # Extract features for prediction
            features = [
                form_data['sslc'],
                form_data['hsc'],
                form_data['cgpa'],
                form_data['school_type'],
                form_data['no_of_miniprojects'],
                form_data['no_of_projects'],
                form_data['coresub_skill'],
                form_data['aptitude_skill'],
                form_data['problemsolving_skill'],
                form_data['programming_skill'],
                form_data['abstractthink_skill'],
                form_data['design_skill'],
                form_data['first_computer'],
                form_data['first_program'],
                form_data['lab_programs'],
                form_data['ds_coding'],
                form_data['technology_used'],
                form_data['sympos_attend'],
                form_data['sympos_won'],
                form_data['extracurricular'],
                form_data['learning_style'],  # Make sure to encode this field if it's categorical
                form_data['college_bench'],
                form_data['clg_teachers_know'],
                form_data['college_performence'],
                form_data['college_skills']
            ]

            # Call the ML prediction function (you should implement this function)
            predicted_role = predict_career(features)

            # Render the result page with the prediction
            return render(request, 'result.html', {'predicted_role': predicted_role})

    else:
        # Handle GET request: render the form
        form = PredictionForm()

    return render(request, 'predict.html', {'form': form})
