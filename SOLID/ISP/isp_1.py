#  this is for the interface seggregation property of solid 

from abc import ABC, abstractmethod

class Hospital(ABC):
     
     def __init__(self,patient_name,patient_disease,doctor_name,department):
          
          self.patient_name = patient_name
          self.patient_disease = patient_disease
          self.doctor = doctor_name
          self.department = department
     
     # Patient details 
     
     def patient(self, patient_name,patient_disease):
          print(f"The name of the patient is {self.patient_name} and he/she is diagnosed with {self.patient_disease}")
          
     #  registered or not 
     
     @abstractmethod
     def registered(self,patient_name) -> bool:
          pass
     
     
# Appointment class 

class Appointment(Hospital):
     
     def registered(self, patient_name):
          return super().registered(patient_name)
     
     def appointment (self, patient_name, doctor_name):
          if self.registered(patient_name):
               print(f"{patient_name} has an appointment with {doctor_name}")
          else:
               print(f"{patient_name} is not registered and cannot have an appointment with {doctor_name}")


# Billing class --> Payment 

class Billing(Appointment):
     
     def registered(self, patient_name):
          return super().registered(patient_name) 
     
     def billing(self, patient_name, amount):
          if self.registered(patient_name) == True and self.appointment(patient_name, self.doctor):
               print(f"{patient_name} has to pay {amount} for the treatment")
          else:
               print(f"{patient_name} is not registered and cannot be billed for the treatment")
     
     
#  Patient History class 

class PatientHistory(Billing):
     
     def registered(self, patient_name):
          return super().registered(patient_name) 
     
     def patient_history(self, patient_name):
          if self.registered(patient_name) == True and self.appointment(patient_name, self.doctor):
               print(f"{patient_name} has a history of {self.patient_disease} and has been treated by {self.doctor} in the {self.department} department")
          else:
               print(f"{patient_name} is not registered and cannot have a history of the disease")
          

patient1 = PatientHistory("Devesh", "Allergy", "Dr. Varsha", "Dermatology")

patient1.patient(patient1.patient_name, patient1.patient_disease)

    