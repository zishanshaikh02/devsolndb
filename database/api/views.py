from django.shortcuts import render

# Create your views here.
from .serializer import BlogSerializer
from .models import Blog
from rest_framework.viewsets import ModelViewSet 



class BlogViewSet(ModelViewSet):

    queryset = Blog.objects.all()

    serializer_class = BlogSerializer

    def get_queryset(self):
        key = self.request.query_params.get('key', None)
        print(key)
        
        # Filter queryset based on the 'key' parameter
        if key:
            return Blog.objects.filter(pop_post=True)
        else:
            return Blog.objects.all()
        
# views.py
# myapp/views.py
# views.py
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Contact
# from .serializer import ContactSerializer
# from django.core.mail import send_mail

# @api_view(['POST'])
# def contact_view(request):
#     if request.method == 'POST':
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             # Save the contact details to the database
#             contact = serializer.save()
#             first_name = serializer.save()
#             last_name = serializer.save()
           
            

#             # Send email
#             subject = 'New Contact Form Submission'
#             message = f'You have a new contact form submission:\n\n{contact} {first_name} {last_name}  '
#             from_email = 'devsoln17@gmail.com'
#             recipient_list = ['devsoln17@gmail.com']  # Add your recipient email address here
#             send_mail(subject, message, from_email, recipient_list)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Contact
from .serializer import ContactSerializer
from django.core.mail import send_mail

@api_view(['POST'])
def contact_view(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            # Save the contact details to the database
            contact = serializer.save()

            # Extract individual fields from the serializer
            first_name = serializer.validated_data.get('first_name', '')
            last_name = serializer.validated_data.get('last_name', '')
            email = serializer.validated_data.get('email', '')
            mobile = serializer.validated_data.get('mobile', '')
            usermessage = serializer.validated_data.get('message', '')

            # Send email with all details
            subject = 'New Contact Form Submission'
            message = f'You have a new contact form submission:\n\n'
            message += f'First Name: {first_name}\n'
            message += f'Last Name: {last_name}\n'
            message += f'Email: {email}\n'
            message += f'Mobile: {mobile}\n'
            message += f'Message: {usermessage}\n'

            from_email = 'devsoln17@gmail.com'
            recipient_list = ['devsoln17@gmail.com']  # Add your recipient email address here
            send_mail(subject, message, from_email, recipient_list)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
