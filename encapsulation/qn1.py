class Patient:
    def __init__(self, patient_id, patient_name, disease, bill_amount):
        self.__patient_id = patient_id
        self.__patient_name = patient_name
        self.__disease = disease
        self.__bill_amount = bill_amount

   
    def get_patient_id(self):
        return self.__patient_id

    def get_patient_name(self):
        return self.__patient_name

    def get_disease(self):
        return self.__disease

    def get_bill_amount(self):
        return self.__bill_amount

  
    def set_patient_name(self, name):
        self.__patient_name = name

    def set_disease(self, disease):
        self.__disease = disease

    def set_bill_amount(self, amount):
        if amount >= 0:
            self.__bill_amount = amount
        else:
            print("Invalid bill amount.")


    def add_extra_charge(self, charge):
        if charge > 0:
            self.__bill_amount += charge
            print("Extra charge added.")
        else:
            print("Invalid charge.")

    def display_details(self):
        print("\n----- Patient Details -----")
        print("Patient ID :", self.__patient_id)
        print("Patient Name :", self.__patient_name)
        print("Disease :", self.__disease)
        print("Bill Amount :", self.__bill_amount)



patient = Patient(101, "Sanjay", "Fever", 5000)

patient.display_details()

patient.add_extra_charge(1500)

patient.display_details()