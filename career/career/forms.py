from django import forms

class PredictionForm(forms.Form):
    # Numerical fields
    sslc = forms.IntegerField(label="SSLC Marks", min_value=0, max_value=100)
    hsc = forms.IntegerField(label="HSC Marks", min_value=0, max_value=100)
    cgpa = forms.IntegerField(label="CGPA", min_value=0, max_value=10)
    school_type = forms.ChoiceField(label="School Type", choices=[(1, 'Government'), (2, 'Private')])
    no_of_miniprojects = forms.IntegerField(label="Number of Mini Projects")
    no_of_projects = forms.IntegerField(label="Number of Projects")
    coresub_skill = forms.IntegerField(label="Core Subject Skill", min_value=0, max_value=10)
    aptitude_skill = forms.IntegerField(label="Aptitude Skill", min_value=0, max_value=10)
    problemsolving_skill = forms.IntegerField(label="Problem Solving Skill", min_value=0, max_value=10)
    programming_skill = forms.IntegerField(label="Programming Skill", min_value=0, max_value=10)
    abstractthink_skill = forms.IntegerField(label="Abstract Thinking Skill", min_value=0, max_value=10)
    design_skill = forms.IntegerField(label="Design Skill", min_value=0, max_value=10)
    first_computer = forms.ChoiceField(label="First Computer Experience", choices=[(1, 'Yes'), (0, 'No')])
    first_program = forms.ChoiceField(label="First Program Experience", choices=[(1, 'Yes'), (0, 'No')])
    lab_programs = forms.IntegerField(label="Number of Lab Programs")
    ds_coding = forms.IntegerField(label="Data Structures & Coding")
    technology_used = forms.IntegerField(label="Technology Used")
    sympos_attend = forms.IntegerField(label="Number of Symposia Attended")
    sympos_won = forms.IntegerField(label="Number of Symposia Won")
    extracurricular = forms.IntegerField(label="Extracurricular Activities")
    learning_style = forms.ChoiceField(label="Learning Style", choices=[('Visual', 'Visual'), ('Auditory', 'Auditory'), ('Kinesthetic', 'Kinesthetic')])
    college_bench = forms.IntegerField(label="College Bench")
    clg_teachers_know = forms.IntegerField(label="Teachers Know in College")
    college_performence = forms.IntegerField(label="College Performance")
    college_skills = forms.IntegerField(label="College Skills")

    # Optional: Add any extra fields or validation rules as needed
