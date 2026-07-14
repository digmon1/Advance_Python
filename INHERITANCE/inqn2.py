# Parent Class
class Patient:
    def __init__(self, patient_id, name, disease, bill):
        self.__patient_id = patient_id
        self.__name = name
        self.__disease = disease
        self.__bill = bill

    # Getters
    def get_patient_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name

    def get_disease(self):
        return self.__disease

    def get_bill(self):
        return self.__bill

    # Setters
    def set_patient_id(self, patient_id):
        self.__patient_id = patient_id

    def set_name(self, name):
        self.__name = name

    def set_disease(self, disease):
        self.__disease = disease

    def set_bill(self, bill):
        self.__bill = bill

    # Display Details
    def display_details(self):
        print(self)

    # String Method
    def __str__(self):
        return (f"Patient ID : {self.__patient_id}\n"
                f"Name       : {self.__name}\n"
                f"Disease    : {self.__disease}\n"
                f"Daily Bill : Rs.{self.__bill}")


# Child Class
class InPatient(Patient):
    def __init__(self, patient_id, name, disease, bill, days_admitted):
        super().__init__(patient_id, name, disease, bill)
        self.__days_admitted = days_admitted

    # Getter
    def get_days_admitted(self):
        return self.__days_admitted

    # Setter
    def set_days_admitted(self, days):
        self.__days_admitted = days

    # Calculate Total Bill
    def calculate_total_bill(self):
        return self.get_bill() * self.__days_admitted

    # Overriding __str__()
    def __str__(self):
        return (super().__str__() +
                f"\nDays Admitted : {self.__days_admitted}"
                f"\nTotal Bill    : Rs.{self.calculate_total_bill()}")


# Driver Program
patient = InPatient("P101", "Sanjay", "Dengue", 2500, 5)

print("Patient Details")
patient.display_details()

print("\nAfter Updating Admission Days")
patient.set_days_admitted(7)
print(patient)