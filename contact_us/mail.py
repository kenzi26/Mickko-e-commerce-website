from templated_mail.mail import BaseEmailMessage
from os import path
from core.settings import ABS_PATH

class ContactUsEmailUser(BaseEmailMessage):
    """ This handles the templating of a notification in response to a submitted contact us form to 
    the user"""

    template_name = path.join(ABS_PATH,  "contact_us/templates/emails/contactus_email_notification_user.html")
    def get_context_data(self):
        context = super().get_context_data()
        return context
    
class ContactUsEmailAdmin(BaseEmailMessage):
    """ This handles the templating of a contact us form notification to the admin informing him of a new
    form submission"""

    template_name = path.join(ABS_PATH,  "contact_us/templates/emails/contactus_email_notification_admin.html")
    def get_context_data(self):
        context = super().get_context_data()
        return context