from django.shortcuts import render
#from sklearn.externals import joblib

import pickle
import joblib
import pandas as pd


# Create your views here.
reloadModel=joblib.load("./pred_model/house_price_pred_1.pkl")
#reloadModel=pickle.load(open("./pred_price/house_price_pred.pkl",'rb'))
# with open('pred_model/house_price_pred.pkl', 'rb') as f:
#     reloadModel = pickle.load(f)

def home(request):
    
    return render( request, "index.html")

def pred_price(request):

    if request.method == 'POST':

        temp={}

        temp['area_type']=int(request.POST.get('area_type'))

        temp['size']=int(request.POST.get('size'))

        temp['new_total_sqft']=request.POST.get('new_total_sqft')

        temp['bath']=request.POST.get('bath')

        temp['balcony']=request.POST.get('balcony')

           



    testDtaa=pd.DataFrame({'x':temp}).transpose()

    scoreval=reloadModel.predict(testDtaa)

    print(scoreval)
    context={'scoreval':scoreval,'temp':temp}
    return render( request, "index.html",context)