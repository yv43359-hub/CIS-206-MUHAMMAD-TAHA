from datetime import date


class Patient:
    def __init__(self, first_name, middle_name, last_name, address,
                 city, state, zip_code, phone, emergency_name,
                 emergency_phone):

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

    # Mutator methods
    def set_first_name(self, value):
        self.first_name = value

    def set_middle_name(self, value):
        self.middle_name = value

    def set_last_name(self, value):
        self.last_name = value

    def set_address(self, value):
        self.address = value

    def set_city(self, value):
        self.city = value

    def set_state(self, value):
        self.state = value

    def set_zip_code(self, value):
        self.zip_code = value

    def set_phone(self, value):
        self.phone = value

    def set_emergency_name(self, value):
        self.emergency_name = value

    def set_emergency_phone(self, value):
        self.emergency_phone = value

    # Accessor methods
    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.last_name

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip_code(self):
        return self.zip_code

    def get_phone(self):
        return self.phone

    def get_emergency_name(self):
        return self.emergency_name

    def get_emergency_phone(self):
        return self.emergency_phone


class Procedure:
    def __init__(self, procedure_name, procedure_date,
                 practitioner, charges):

        self.procedure_name = procedure_name
        self.procedure_date = procedure_date
        self.practitioner = practitioner
        self.charges = charges

    # Mutator methods
    def set_procedure_name(self, value):
        self.procedure_name = value

    def set_procedure_date(self, value):
        self.procedure_date = value

    def set_practitioner(self, value):
        self.practitioner = value

    def set_charges(self, value):
        self.charges = value

    # Accessor methods
    def get_procedure_name(self):
        return self.procedure_name

    def get_procedure_date(self):
        return self.procedure_date

    def get_practitioner(self):
        return self.practitioner

    def get_charges(self):
        return self.charges


# Create a Patient object
patient = Patient(
    "Muhammad",
    "Taha",
    "Sohail",
    "123 Main Street",
    "Chicago",
    "Illinois",
    "60601",
    "555-123-4567",
    "Ahmed Sohail",
    "555-987-6543"
)

# Today's date
today = date.today()

# Create three Procedure objects
procedure1 = Procedure("Physical Exam", today, "Dr. Irvine", 250.00)
procedure2 = Procedure("X-ray", today, "Dr. Jamison", 500.00)
procedure3 = Procedure("Blood Test", today, "Dr. Smith", 200.00)

# Display patient information
print("Patient Information")
print("-------------------------")
print("Name:", patient.get_first_name(),
      patient.get_middle_name(),
      patient.get_last_name())
print("Address:", patient.get_address())
print("City:", patient.get_city())
print("State:", patient.get_state())
print("ZIP Code:", patient.get_zip_code())
print("Phone:", patient.get_phone())
print("Emergency Contact:", patient.get_emergency_name())
print("Emergency Contact Phone:", patient.get_emergency_phone())

# Display procedure information
print("\nProcedure Information")
print("-------------------------")

print("Procedure 1")
print("Name:", procedure1.get_procedure_name())
print("Date:", procedure1.get_procedure_date())
print("Practitioner:", procedure1.get_practitioner())
print("Charges: $", format(procedure1.get_charges(), ".2f"))

print("\nProcedure 2")
print("Name:", procedure2.get_procedure_name())
print("Date:", procedure2.get_procedure_date())
print("Practitioner:", procedure2.get_practitioner())
print("Charges: $", format(procedure2.get_charges(), ".2f"))

print("\nProcedure 3")
print("Name:", procedure3.get_procedure_name())
print("Date:", procedure3.get_procedure_date())
print("Practitioner:", procedure3.get_practitioner())
print("Charges: $", format(procedure3.get_charges(), ".2f"))

# Calculate total charges
total_charges = (
    procedure1.get_charges()
    + procedure2.get_charges()
    + procedure3.get_charges()
)

print("\nTotal Charges: $", format(total_charges, ".2f"))