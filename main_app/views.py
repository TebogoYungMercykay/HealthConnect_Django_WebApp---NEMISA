from django.shortcuts import render, redirect
from django.contrib.auth.models import User


HOME_TEMPLATE = 'patient/patient_ui/profile.html'

def home(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            return render(request, 'blog/posts.html')

        else:
            return render(request, 'homepage/index.html')

    else:
        return redirect('')
        
def admin_ui(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            auser = request.user
            Feedbackobj = Feedback.objects.all()

            return render(request, 'admin/admin_ui/admin_ui.html', {"auser": auser, "Feedback": Feedbackobj})

        else:
            return redirect('home')

    if request.method == 'POST':

        return render(request, HOME_TEMPLATE)


def patient_ui(request):

    if request.method == 'GET':

        if request.user.is_authenticated:

            patient_id = request.session['patient_id']
            puser = User.objects.get(username=patient_id)

            return render(request, HOME_TEMPLATE, {"puser": puser})

        else:
            return redirect('home')

    if request.method == 'POST':

        return render(request, HOME_TEMPLATE)


def patient_profile(request, patient_id):

    if request.method == 'GET':

        puser = User.objects.get(username=patient_id)

        return render(request, 'patient/view_profile/view_profile.html', {"puser": puser})


def doctor_ui(request):

    if request.method == 'GET':

        doctor_id = request.session['doctor_id']
        duser = User.objects.get(username=doctor_id)

        return render(request, 'doctor/doctor_ui/profile.html', {"duser": duser})


def doctor_profile(request, doctor_id):

    if request.method == 'GET':

        duser = User.objects.get(username=doctor_id)
        r = rating_review.objects.filter(doctor=duser.doctor)

        return render(request, 'doctor/view_profile/view_profile.html', {"duser": duser, "rate": r})

