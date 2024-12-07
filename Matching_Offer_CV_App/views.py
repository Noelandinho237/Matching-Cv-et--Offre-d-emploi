from django.shortcuts import render, redirect, get_object_or_404

from Matching_Offer_CV_App.forms import OfferForm
from Matching_Offer_CV_App.forms import CvForm

from Matching_Offer_CV_App.models import Cv
from Matching_Offer_CV_App.models import Offer


from joblib import load
from PyPDF2 import PdfReader



# Create your views here.
def home(request):
    return render(request,'home.html')





#************************************* Functions that will be useful ****************************
def read_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            
            # Iterate through each page and extract text
            for page in reader.pages:
                text += page.extract_text() or ''
                
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return text





#**************************************** Offer Views *****************************************
# View to show offers available
def offer_list(request):
    offers = Offer.objects.all()
    return render(request, 'offer_list.html', {'offers': offers})


# View responsible for adding an offer
def offer_add(request):
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('offer_list')
    else:
        form = OfferForm()
    return render(request, 'offer_form.html', {'form': form, 'action': 'Add'})


# View responsible for showing the content of the pdf file 
def offer_view(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    pdf_path = offer.description_offer.path
    text = read_pdf(pdf_path)
    return render(request, 'offer_view.html', {'pdf_url': pdf_path, 'offer': offer, 'text':text})


# View responsible for Editing an Offer
def offer_edit(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('offer_list')
    else:
        form = OfferForm(instance=offer)
    return render(request, 'offer_form.html', {'form': form, 'action': 'Edit'})


# View to delete an offer 
def offer_delete(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    if request.method == 'POST':
        offer.delete()
        return redirect('offer_list')
    return render(request, 'offer_confirm_delete.html', {'offer': offer})





#**************************************** CVs Views *****************************************
# Listing all the cv in the Data base 
def cv_list(request):
    cvs = Cv.objects.all()
    return render(request, 'cv_list.html', {'cvs': cvs})


# To add a Cv in DB
def cv_add(request):
    if request.method == 'POST':
        form = CvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cv_list')
    else:
        form = CvForm()
    return render(request, 'cv_form.html', {'form': form, 'action': 'Add'})


# To edit a cv already in db 
def cv_edit(request, pk):
    cv = get_object_or_404(Cv, pk=pk)
    if request.method == 'POST':
        form = CvForm(request.POST, request.FILES, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('cv_list')
    else:
        form = CvForm(instance=cv)
    return render(request, 'cv_form.html', {'form': form, 'action': 'Edit'})


#Delete a cv in our db
def cv_delete(request, pk):
    cv = get_object_or_404(Cv, pk=pk)
    if request.method == 'POST':
        cv.delete()
        return redirect('cv_list')
    return render(request, 'cv_confirm_delete.html', {'cv': cv, 'action': 'Delete'})


# View Cv that is in DB
def cv_view(request, pk):
    cv = get_object_or_404(Cv, pk=pk)
    pdf_path = cv.description_cv.path
    text = read_pdf(pdf_path)
    return render(request, 'cv_view.html', {'pdf_path': pdf_path, 'cv': cv, 'text':text})





#********************************************************************************************

# Example: Load the trained pipeline
model = load('model.joblib')

def predict_from_pdf(model, file_path):
    # Read and preprocess the PDF text
    pdf_text = read_pdf(file_path)
    
    # Make prediction
    prediction = model.predict([pdf_text])
    
    return prediction[0]


def cv_add_and_predict(request):
    if request.method == 'POST':
        form = CvForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=True)
            
            # Extract text from the PDF
            pdf_path = cv.description_cv.path
            text = read_pdf(pdf_path)
            
            # Predict the category
            category = predict_from_pdf(model,cv.description_cv.path)
            
            # Set the predicted category
            cv.category = category  
            
            # Save the new CV with the predicted category
            cv.save()  
            
            # Redirect to a page where the user can see the list of CVs or another relevant page
            return redirect('cv_list')  
    else:
        form = CvForm()
    
    return render(request, 'cv_add_and_predict.html', {'form': form})


def offer_add_and_predict(request):
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)

        if form.is_valid():
            offer = form.save(commit=True)
            #offer = form.save(commit=False)

            # Extract text from the PDF
            pdf_path = offer.description_offer.path
            text = read_pdf(pdf_path)
            
            # Predict the category
            category = predict_from_pdf(model,offer.description_offer.path)

            # Set the predicted category
            offer.category = category  
            
            # Save the new CV with the predicted category
            offer.save()  
            
            # Redirect to a page where the user can see the list of CVs or another relevant page
            return redirect('offer_list')  
    else:
        form = OfferForm()
    
    return render(request, 'offer_add_and_predict.html', {'form': form})

def resultat(request):
    jobs = Offer.objects.all()
    return render(request, 'resultat.html', {'jobs': jobs})





#********************************************************************************************
#Offre liste pour les dropdown

#Pour la page des gestion
def offer_list_gestion(request):
	offers = Offer.objects.all()
	return render(request,
	'offer_list_gestion.html',
	{'offers' : offers}
	)


#Pour la page des informatique
def offer_list_informatique(request):
	offers = Offer.objects.all()
	return render(request,
	'offer_list_informatique.html',
	{'offers' : offers}
	)


#Pour la page des immobilier
def offer_list_immobilier(request):
	offers = Offer.objects.all()
	return render(request,
	'offer_list_immobilier.html',
	{'offers' : offers}
	)


#Pour la page des finance
def offer_list_finance(request):
	offers = Offer.objects.all()
	return render(request,
	'offer_list_finance.html',
	{'offers' : offers}
	)


#Pour la page des commerce 
def offer_list_commerce(request):
	offers = Offer.objects.all()
	return render(request,
	'offer_list_commerce.html',
	{'offers' : offers}
	)





#********************************************************************************************
#CV liste pour les dropdown

#Pour la page des gestion
def cv_list_gestion(request):
	cvs = Cv.objects.all()
	return render(request,
	'cv_list_gestion.html',
	{'cvs' : cvs}
	)


#Pour la page des informatique
def cv_list_informatique(request):
	cvs = Cv.objects.all()
	return render(request,
	'cv_list_informatique.html',
	{'cvs' : cvs}
	)


#Pour la page des finance
def cv_list_finance(request):
	cvs = Cv.objects.all()
	return render(request,
	'cv_list_finance.html',
	{'cvs' : cvs}
	)


#Pour la page des immobilier
def cv_list_immobilier(request):
	cvs = Cv.objects.all()
	return render(request,
	'cv_list_immobilier.html',
	{'cvs' : cvs}
	)


#Pour la page des commerce
def cv_list_commerce(request):
	cvs = Cv.objects.all()
	return render(request,
	'cv_list_commerce.html',
	{'cvs' : cvs}
	)











