from django.http import JsonResponse
from django.core.mail import mail_admins, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage

from playground.tasks import notify_customers

def celery(request):
  notify_customers.delay('Hello, this is a message from Celery!')
  return JsonResponse({'message': 'Task was sent to Celery!'})

def hello_world(request):
  try:
    # mail_admins('Django', 'Hello, World!', html_message='<p>Hello, World!</p>')
    
    # message = EmailMessage('Django', 'Hello, World!', to=['khangtrann8198@gmail.com'])
    # message.attach_file('playground/static/images/inspectorio.jpeg') 
    # message.send()
    
    message = BaseEmailMessage(
      template_name='emails/hello.html',
      context={'name': 'Khang'},
    )
    
    message.send(['khangtrann8198@gmail.com'])
  except BadHeaderError:
    pass
  
  return JsonResponse({'message': 'Hello, World!'})