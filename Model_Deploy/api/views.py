from django.shortcuts import render
import pickle as pkl
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# Create your views here.

with open('/home/shubham/Shubham_work/AI_Days/day8/House_Prediction/House_Prediction/housemodel.pkl','rb') as f:
    model_housing = pkl.load(f)

with open('/home/shubham/Shubham_work/AI_Days/day8/House_Prediction/House_Prediction/svc_model_for_scam.pkl', 'rb') as f:
    vectorizer, model_scam = pkl.load(f)

# Congratulations! You have won a lottery. Claim now!

def predict_price (request):
    if request.method =='POST':
        house_size = float(request.POST.get('size'))
        no_of_Bedrooms = float(request.POST.get('bedrooms'))
        no_of_Bathrooms = float(request.POST.get('bathrooms'))
        house_age = float(request.POST.get('age'))
        distance_from_city = float(request.POST.get('distance'))
        floors = float(request.POST.get('floors'))

        features = np.array([house_size,
                             no_of_Bedrooms,
                             no_of_Bathrooms,
                             house_age,
                             distance_from_city,
                             floors])

        predicted_price= model_housing.predict(features.reshape(1,-1))[0]
        return render(request,'index.html',{'Predicated_Price':predicted_price})
    return render(request,'index.html')


def predict_scam(request):
    if request.method == 'POST':
        msg = str(request.POST.get('msg'))
        
        # Transform the new message using the same trained vectorizer
        X_new = vectorizer.transform([msg])
        
        # Predict the scam status
        predicted_scam = model_scam.predict(X_new)[0]
        
        return render(request, 'scam.html', {'Predicted_Scam': predicted_scam})

    return render(request, 'scam.html')