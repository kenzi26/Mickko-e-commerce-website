#from core.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMessage
from .models import ContactUs
from .mail import ContactUsEmailUser, ContactUsEmailAdmin
from django.templatetags.static import static

#logo_path = "https://res.cloudinary.com/dsdao3ylr/image/upload/v1692818453/dcfoodlogo_ma9cws.png"

admin_email = "support@mickko.com"

class ContactUsController():

    def send_contact_us_mail_user( contact_us:ContactUs):
        #this handles sending a 'contact us message received' mail notification to the user       
        mail = ContactUsEmailUser(
          
            context={
                "name": contact_us.full_name,
                "email": contact_us.email,
                #"logo": logo_path
            }
        )
        to_emails = [contact_us.email]
       
#        mail.send(to_emails, from_email=DEFAULT_FROM_EMAIL)


    def send_contact_us_mail_admin( contact_us:ContactUs):
        #this handles sending a mail notification to the admin to inform him of a new contact us form
        to_email = admin_email
        
        mail = ContactUsEmailAdmin(
          
            context={
                "name": contact_us.full_name,
                "email": contact_us.email,
                "phone": contact_us.phone_number,
                "subject": contact_us.subject,
                "message": contact_us.message,
                #"logo": logo_path
               
            }
        )
        to_emails = [to_email]
       
#        mail.send(to_emails, from_email=DEFAULT_FROM_EMAIL)
    
   