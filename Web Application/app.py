from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder="templates")

# Load the pickle file
with open("E:\\Sem_8\\Project\\models\\raf.pkl", "rb") as f:
    model = pickle.load(f)

print("Successful")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve form data
        data = {
            'CODE_GENDER': request.form['CODE_GENDER'],
            'FLAG_OWN_CAR': request.form['FLAG_OWN_CAR'],
            'FLAG_OWN_REALTY': request.form['FLAG_OWN_REALTY'],
            'CNT_CHILDREN': request.form['CNT_CHILDREN'],
            'AMT_INCOME_TOTAL': request.form['AMT_INCOME_TOTAL'],
            'NAME_INCOME_TYPE': request.form['NAME_INCOME_TYPE'],
            'NAME_EDUCATION_TYPE': request.form['NAME_EDUCATION_TYPE'],
            'NAME_FAMILY_STATUS': request.form['NAME_FAMILY_STATUS'],
            'NAME_HOUSING_TYPE': request.form['NAME_HOUSING_TYPE'],
            'AGE_YEARS': request.form['AGE_YEARS'],
            'YEARS_EMPLOYED': request.form['YEARS_EMPLOYED'],
            'FLAG_MOBIL': request.form['FLAG_MOBIL'],
            'FLAG_WORK_PHONE': request.form['FLAG_WORK_PHONE'],
            'FLAG_PHONE': request.form['FLAG_PHONE'],
            'FLAG_EMAIL': request.form['FLAG_EMAIL'],
            'CNT_FAM_MEMBERS': request.form['CNT_FAM_MEMBERS'],
        }

        # Convert form data to appropriate types and format for model
        input_data = [
            data['CODE_GENDER'],
            data['FLAG_OWN_CAR'],
            data['FLAG_OWN_REALTY'],
            int(data['CNT_CHILDREN']),
            float(data['AMT_INCOME_TOTAL']),
            data['NAME_INCOME_TYPE'],
            data['NAME_EDUCATION_TYPE'],
            data['NAME_FAMILY_STATUS'],
            data['NAME_HOUSING_TYPE'],
            int(data['AGE_YEARS']),
            float(data['YEARS_EMPLOYED']),
            int(data['FLAG_MOBIL']),
            int(data['FLAG_WORK_PHONE']),
            int(data['FLAG_PHONE']),
            int(data['FLAG_EMAIL']),
            int(data['CNT_FAM_MEMBERS'])
        ]

        # Make a prediction using the model
        prediction = model.predict([input_data])
        # Determine the message based on the prediction
        if prediction[0] == 0:
            result_message = "Good Client/Applicant"
        else:
            result_message = "Bad Client/Applicant"

        # Return the prediction result with centered alignment
        return render_template('result.html', result_message=result_message)

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
