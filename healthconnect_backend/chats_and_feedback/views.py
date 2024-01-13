from django.shortcuts import render
from django.http import HttpResponse


def post_feedback(request, user_id):
    
    if request.method == "POST":

        feedback = request.POST.get('feedback', None)
        if feedback != '':  
            f = Feedback(sender=request.user, feedback=feedback)
            f.save()        
            print(feedback)   

            try:
                if (request.user.patient.is_patient == True) :
                    return HttpResponse("Feedback successfully sent.")
            except:
                pass
            if (request.user.doctor.is_doctor == True) :
                return HttpResponse("Feedback successfully sent.")

        else :
            return HttpResponse("Feedback field is empty   .")


def user_feedback(request, user_id):
    
    if request.method == "GET":

      obj = Feedback.objects.all()
      
      return redirect(request, 'consultation/chat_body.html',{"obj":obj})


def chat_messages(request, user_id):

    if request.method == "GET":

        consultation_id = request.session['consultation_id']

        c = Chat.objects.filter(consultation_id=consultation_id)
        return render(request, 'consultation/chat_body.html', {'chat': c})


def create_chat(request, user_id):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)

        consultation_id = request.session['consultation_id']
        consultation_obj = consultation.objects.get(id=consultation_id)

        c = Chat(consultation_id=consultation_obj,
                 sender=request.user, message=msg)

        # msg = c.user.username+": "+msg

        if msg != '':
            c.save()
            print("msg saved" + msg)
            return JsonResponse({'msg': msg})
    else:
        return HttpResponse('Request must be POST.')


def whatsapp(request):

    if request.method == 'POST':
        
        body =  request.POST.get('body')
        mobile =  request.POST.get('mobile')

        account_sid = 'tt'
        auth_token = 'tt'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body = str(body),
            to = 'whatsapp:' + str(mobile)
        )

        print(message.sid)

        return redirect('admin_ui')


def meeting(request):
    return render(request, 'consultation/videocall.html', {'name': request.user.first_name + " " + request.user.last_name})

