from templated_mail.mail import BaseEmailMessage
from os import path
from core.settings import ABS_PATH

class QuotationEmail(BaseEmailMessage):
    template_name = path.join(ABS_PATH,  "templates/emails/quotation.html")
    def get_context_data(self):
        # QuotationEmail can be deleted
        context = super().get_context_data()
        return context
