from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        email = data['email']
        message = data['message']

        if not (name and email and message):
            return JsonResponse({'message': 'Missing parameters'}, status=400)

        try:
            subject = 'Contact Form Submission'
            message_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['harissh0110@gmail.com']  # Replace with your recipient email address

            send_mail(subject, message_body, email_from, recipient_list)
            return JsonResponse({'message': 'Email sent successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'message': f'An error occurred: {str(e)}'}, status=500)  # Properly include the error message
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)
