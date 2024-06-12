# Credit_Card_Approval_Prediction

ABSTRACT:

Credit scorecards are a common risk control method in the financial industry. They use personal information and data submitted by credit card applicants to predict the probability of future defaults and credit card borrowings. This allows banks to decide whether to issue a credit card to the applicant. This project involves building a machine learning model to predict if an applicant is a 'good' (0) or 'bad' (1) client. The model is trained using various machine learning algorithms such as Logistic Regression, Decision Tree, and Random Forest Classifier among them, the Random Forest classifier demonstrated the highest accuracy.

WEB APPLICATION:

A web application was developed using HTML, CSS, and Flask. The application presents a form to the user where they input their information based on specific questions. The application then uses the trained Random Forest model to predict the outcome, indicating whether the user is a 'good' or 'bad' client. The user accesses the web application and fills out a form with their personal and financial information. Upon submission, the Random Forest model processes the input data and predicts whether the applicant is a 'good' or 'bad' client. The result is then displayed to the user on the web interface.

DATASET DESCRIPTION:

The dataset is taken from Kaggle. The number of rows within the dataset is 438557 and the number of columns is 18.
The data is in the form of Feature_name - Explanation    

ID - Client number  
CODE_GENDER - Gender  
FLAG_OWN_CAR - Is there a car  
FLAG_OWN_REALTY - Is there a property  
CNT_CHILDREN - Number of children  
AMT_INCOME_TOTAL - Annual income  
NAME_INCOME_TYPE - Income category  
NAME_EDUCATION_TYPE - Education level  
NAME_FAMILY_STATUS - Marital status  
NAME_HOUSING_TYPE - Way of living  
DAYS_BIRTH - Birthday  
DAYS_EMPLOYED - Start date of employment  
FLAG_MOBIL - Is there a mobile phone  
FLAG_WORK_PHONE - Is there a work phone  
FLAG_PHONE - Is there a phone  
FLAG_EMAIL - Is there an email  
OCCUPATION_TYPE - Occupation  
CNT_FAM_MEMBERS - Family size  

DATASET SOURCE: https://www.kaggle.com/rikdifos/credit-card-approval-prediction


