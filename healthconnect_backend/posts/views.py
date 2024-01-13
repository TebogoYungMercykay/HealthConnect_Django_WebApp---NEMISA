from django.shortcuts import render
from django.http import HttpResponse

def get_posts(request):
    return HttpResponse('view')


def all_posts(request):
    print("The request method ..........................................", request)
    if request.method == 'GET':
        # retrieving the public posts
        all_posts = public_post.objects.all()
        return render(request, 'blog/posts.html', {'all_posts': all_posts})


def create_post(request):
    return HttpResponse('view')


def get_post(request, post_id):
    if request.method == 'POST':
        # Get data from the form
        public_user_name = request.user.username

        public_post_text = request.POST.get('posttext', None)
        print("##", public_user_name, public_post_text)
        # Create a new post instance
        new_post = public_post(
            post_header=public_user_name, post_text=public_post_text)
        new_post.save()

        # Redirect to the retrieve_public_post view using GET
        return JsonResponse({'msg': "Done"})


def update_post(request, post_id):
    return HttpResponse('view')


def delete_post(request, post_id):
    return HttpResponse('view')


def create_reply(request, post_id):
    if request.method == 'POST':
        # Get data from the form
        print("**", request.user)
        replymsg = request.POST.get('replycontent')
        print("FER4EW", replymsg)
        postID = request.POST.get('postID',None)
        post = public_post.objects.get(post_id=postID)
        user =doctor.objects.get(user_id =request.user.id)#this will be ther doctor
        print(user)

        print("###",replymsg,postID)
          # Create a new post instance
        newreply = Reply(post=post, content=replymsg, user=user)
        newreply.save()

        # Redirect to the retrieve_public_post view using GET
        return JsonResponse({'msg': "Done"})


def vote(request):
    return HttpResponse('view')

