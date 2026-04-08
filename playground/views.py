from django.http import JsonResponse
from django.core.mail import mail_admins, BadHeaderError, EmailMessage

def hello_world(request):
  try:
    # mail_admins('Django', 'Hello, World!', html_message='<p>Hello, World!</p>')
    message = EmailMessage('Django', 'Hello, World!', to=['khangtrann8198@gmail.com'])
    message.attach_file('playground/static/images/inspectorio.jpeg') 
    message.send()
  except BadHeaderError:
    pass
  
  return JsonResponse({'message': 'Hello, World!'})