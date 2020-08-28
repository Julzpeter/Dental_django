from django.shortcuts import render
from django.core.mail import send_mail 

def index(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == 'POST':
        # do stuff
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send email
        send_mail(
            message_name,#subject
            message,#message
            message_email,#from email;
            ['chepngetichjuliet@gmail.com'],#to email
            fail_silently=False,
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        #return page
        return render(request, 'contact.html', {})

def about (request):
    return render(request, 'about.html',{}) 
    
def blog(request):
    return render(request, 'blog.html',{})

        
        
        
