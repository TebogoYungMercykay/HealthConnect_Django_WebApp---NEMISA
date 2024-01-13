# views.py

from django.shortcuts import render
from django.http import HttpResponse

def all_consultations(request, id):
    return HttpResponse('view')

def make_consultation(request):

    if request.method == 'POST':

        patientusername = request.session['patientusername']
        puser = User.objects.get(username=patientusername)
        patient_obj = puser.patient

        # doctorusername = request.session['doctorusername']
        duser = User.objects.get(username=doctorusername)
        doctor_obj = duser.doctor
        request.session['doctorusername'] = doctorusername

        diseaseinfo_id = request.session['diseaseinfo_id']
        diseaseinfo_obj = diseaseinfo.objects.get(id=diseaseinfo_id)

        consultation_date = date.today()
        status = "active"

        consultation_new = consultation(patient=patient_obj, doctor=doctor_obj,
                                        diseaseinfo=diseaseinfo_obj, consultation_date=consultation_date, status=status)
        consultation_new.save()

        request.session['consultation_id'] = consultation_new.id

        print("consultation record is saved sucessfully.............................")

        return redirect('consultationview', consultation_new.id)


def consultation_view_patient(request, consultation_id):

    if request.method == 'GET':

        request.session['consultation_id'] = consultation_id
        consultation_obj = consultation.objects.get(id=consultation_id)

        return render(request, 'consultation/consultation.html', {"consultation": consultation_obj})

     #  if request.method == 'POST':
     #    return render(request,'consultation/consultation.html' )
     

def consultation_view_doctor(request, consultation_id):

    if request.method == 'GET':

        request.session['consultation_id'] = consultation_id
        consultation_obj = consultation.objects.get(id=consultation_id)

        return render(request, 'consultation/consultation.html', {"consultation": consultation_obj})

     #  if request.method == 'POST':
     #    return render(request,'consultation/consultation.html' )


def consultation_history_patient(request):

    if request.method == 'GET':

        patientusername = request.session['patientusername']
        puser = User.objects.get(username=patientusername)
        patient_obj = puser.patient

        consultationnew = consultation.objects.filter(patient=patient_obj)

        return render(request, 'patient/consultation_history/consultation_history.html', {"consultation": consultationnew})



def consultation_history_doctor(request):

    if request.method == 'GET':

        doctorusername = request.session['doctorusername']
        duser = User.objects.get(username=doctorusername)
        doctor_obj = duser.doctor

        consultationnew = consultation.objects.filter(doctor=doctor_obj)

        return render(request, 'doctor/consultation_history/consultation_history.html', {"consultation": consultationnew})



def close_consultation(request, consultation_id):
    if request.method == "POST":

        consultation.objects.filter(pk=consultation_id).update(status="closed")

        return redirect('home')


def create_review(request, doctor_id):
    if request.method == "POST":

        consultation_obj = consultation.objects.get(id=consultation_id)
        patient = consultation_obj.patient
        doctor1 = consultation_obj.doctor
        rating = request.POST.get('rating')
        review = request.POST.get('review')

        rating_obj = rating_review(
            patient=patient, doctor=doctor1, rating=rating, review=review)
        rating_obj.save()

        rate = int(rating_obj.rating_is)
        doctor.objects.filter(pk=doctor1).update(rating=rate)

        return redirect('consultationview', consultation_id)


def get_reviews_id(request, doctor_id):
    return HttpResponse('view')


def get_reviews(request):
    return HttpResponse('view')

