#  Hre I will use adapter patern for making a send email service that use intenal email send and third party email service.

from abc import ABC, abstractmethod

class SendEailNotification(ABC):
     
     @abstractmethod
     def send_mail(self, to:str, subject:str, body:str):
          pass
     

# This is our internal email service here we used send_mail method to send email notification.

class InternalEmailService(SendEailNotification):
     def send_mail(self, to:str, subject:str, body:str):
          mail = {
               
               "To": to,
               "Subject": subject,
               "Body": body
          }
          
          print(f"/n Sending email using internal service:")
          print(f"To: {mail['To']}")
          print(f"Subject: {mail['Subject']}")
          print(f"Body: {mail['Body']}")
          
     
     
#  This is third party email service provider taht uses send_email method to send email notofications.

class ThirdPartyEmailService:
     def send_email(self, recipient:str, title:str, content:str):
          email = {
               "Recipient": recipient,
               "Title": title,
               "Content": content
          }
          
          print(f"/n Sending email using third party service:")
          print(f"Recipient: {email['Recipient']}")
          print(f"Title: {email['Title']}")
          print(f"Content: {email['Content']}")
          
          
#  Adapter class for the tird party email service 

class EmailAdapter(SendEailNotification):
     
     def __init__(self,email_service: ThirdPartyEmailService):
           self.__email_service = email_service
     
     def send_mail(self, to:str, subject:str, body:str):
          self.__email_service.send_email(to, subject, body)
           

          
   
#  Client side class taht sends email services 

  
class SendMail:
     def __init__(self, email_service: SendEailNotification):
          self.__email_service = email_service
          
     def send_message(self, to:str, subject:str, body:str):
          self.__email_service.send_mail(to, subject, body)
          


internal_email_service = InternalEmailService()  # for the internal system 
third_party_email_service = ThirdPartyEmailService() # for third party email service provider
adapter_email_service = EmailAdapter(third_party_email_service) 
send_mail = SendMail(adapter_email_service)
send_mail.send_message("Dev", "Testing of adapter Email Service", "This is our external email service provider" )
          
