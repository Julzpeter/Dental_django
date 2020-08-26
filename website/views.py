from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def contact(request):
    return render(request, 'contact.html', {})

    # if request.method == 'POST':
    #     # do stuff
    #     message_name = request.POST['message-name']
    #     message_email = request.POST['message_email']
    #     message = request.POST['message']

        
    # else:
    #     return render(request, 'contact.html',{})

        
        
        
