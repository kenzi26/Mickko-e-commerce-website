from core.settings import DEFAULT_FROM_EMAIL
from .serializers import Quotation
from .mail import QuotationEmail
from biodata.models import BioData

class QuotationController():
    def send_create_quote_mail( quotation:Quotation):
        cc_email = BioData.objects.first()

        cc_emails = [cc_email.sales_email] if cc_email.sales_email else []
      
        mail = QuotationEmail(
          
            context={
                "name": quotation. name,
                "email": quotation. email,
                "phone": quotation.phone,
                "message": quotation.message,
                "quotation_items": quotation.quotation_items.all().values()
            }
        )

        to_emails = [quotation.email]
        mail.send(to_emails, cc=cc_emails, from_email=DEFAULT_FROM_EMAIL)
    