from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        #collect the data of the form
        if form.is_valid():
            print("Data is Valid")

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # This is the email information
            message_body = (
                f"You have a new email from your portfolio \n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message: {message}"
            )

            #Try to send the email! 
            try:
                #send_mail <-- Django Core Email
                send_mail(
                    "Email from Portfolio",      #Subject
                    message_body,                #Message Body -> What the user typed in message
                    email,                       #From email -> The user's email
                    ['derrickelapp@hotmail.com'] #To Email -> Where you want to get the email message
                )

                print("Email sent successfully")

                #Render and redirect user
                return render(request, 'pages/contact.html', {
                    'form':form
                    })

            except Exception as e:
                #catching malicious behavior
                print(f"Error sending the email:{e}")

                return render(request, 'pages/contact.html', {
                    'form':form,
                    'error':str(e)
                })
                
        else:
            print("Data is NOT Valid")
    else:
        #There is not POST request
        form = ContactForm()
    form = ContactForm()
    return render(request, 'pages/contact.html', {"form": form})

