class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def display_info(self):
        print("Hospital Name:", self.name)
        print("Location:", self.location)
class Patient:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def view_patient(self):
        print("Patient Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
    def search_patient(self, search_name):
        if self.name.lower() == search_name.lower():
            print("Patient Name:", self.name)
            print("Age:", self.age)
            print("Gender:", self.gender)
        else:
            print("Patient not found!")
class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
    def view_doctor(self):
        print("Doctor Name:", self.name)
        print("Specialization:", self.specialization)
class Appointment:
    def __init__(self, patient_name, doctor_name, date, time):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time
    def view_appointment(self):
        print("Patient:", self.patient_name)
        print("Doctor:", self.doctor_name)
        print("Date:", self.date)
        print("Time:", self.time)
Books=[]
while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patient")
    print("3. Search Patient")
    print("4. Add Doctor")
    print("5. View Doctor")
    print("6. Book Appointment")
    print("7. View Appointment")
    print("8. Exit")
    choice = int(input("Enter your choice (1-8): "))
    if choice == 1:
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        gender = input("Enter patient gender: ")
        patient = Patient(name, age, gender)
        print("Patient added successfully!")
    elif choice == 2:
        if patient is not None:
            patient.view_patient()
        else:
            print("No patient found. Please add a patient first.")
    elif choice == 3:
        if patient is not None:
            search_name = input("Enter patient name to search: ")
            patient.search_patient(search_name)
        else:
            print("No patient found.")
    elif choice == 4:
        name = input("Enter doctor name: ")
        specialization = input("Enter specialization: ")
        doctor = Doctor(name, specialization)
        print("Doctor added successfully!")
    elif choice == 5:
        if doctor is not None:
            doctor.view_doctor()
        else:
            print("No doctor found. Please add a doctor first.")
    elif choice == 6:
        if patient is not None and doctor is not None:
            patient_name = input("Enter patient name: ")
            doctor_name = input("Enter doctor name: ")
            date = input("Enter date: ")
            time = input("Enter time: ")
            appointment = Appointment(
                patient_name,
                doctor_name,
                date,
                time
            )
            print("Appointment booked successfully!")
        else:
            print("Please add a patient and doctor first.")
    elif choice == 7:
        if appointment is not None:
            appointment.view_appointment()
        else:
            print("No appointment found.")
    elif choice == 8:
        print("Exiting the hospital management system.")
        break
    else:
        print("Invalid choice! Please enter a valid option.")