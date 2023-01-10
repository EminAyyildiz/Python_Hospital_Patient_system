import time

class Hospital:
    def __init__(self):
        self.patient_add = {}
    def add_patients(self, patient):
        self.patient_add[patient.ID] = patient
    def search_patient(self, ID):
        if ID in self.patient_add:
            return self.patient_add[ID]
        return None
    def update_patient(self, ID,patient):
        if ID in self.patient_add:
            self.patient_add[ID] = patient
            return True
        return False
    def delete_patient(self, ID):
        if ID in self.patient_add:
            del self.patient_add[ID]
            return True
        return False

class Patient:
    def __init__(self,first_name, last_name, ID, birthdate, gender,City):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.birthdate = birthdate
        self.gender = gender
        self.City = City

    def show_information(self):
        return self.first_name + " " + self.last_name + " " + self.ID + " " + self.birthdate + " " + self.gender + " " + self.City

hospital = Hospital()
class Security:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def check_authorization(self):
        print("\nWelcome to the hospital automation system.. \n")
        username = input("Please enter your username :")
        password = input("Please enter your password :")
        if username == self.username and password == self.password:
            return True
        elif username == "q" or username == "Q":
            quit()
        return False

administrator = Security("emin", "6001")
while True:
    if administrator.check_authorization():
        while True:

            print("1. Add patient\n2. View patient information\n3. Update patient information\n4. Delete patient record\n5. Exit\n----> ")

            choice = int(input("Enter the number of the transaction you want to do: "))

            if choice == 1:
                first_name = input("First name: ")
                last_name = input("Last name: ")
                ID = input("ID: ")
                birthdate = input("Birthdate: ")
                gender = input("Gender: ")
                City = input("City : ")
                patient = Patient(first_name, last_name, ID, birthdate, gender,City)
                hospital.add_patients(patient)
            elif choice == 2:
                ID = input("ID: ")
                patient =hospital.search_patient(ID)
                if patient:
                    print(patient.show_information())
                else :
                    print("There is no patient with this information.\n")
            elif choice == 3:
                ID = input("ID : ")
                patient = hospital.search_patient(ID)
                if patient:
                    first_name = input("First name: ")
                    last_name = input("Last name: ")
                    ID = input("ID: ")
                    birthdate = input("Birthdate: ")
                    gender = input("Gender: ")
                    City = input("City : ")
                    updated_patient = Patient(first_name, last_name, ID, birthdate, gender,City)
                    hospital.update_patient(ID,updated_patient)
                    print("Patient information is being updated. Please wait...")
                    time.sleep(1.5)
                    print("Patient information updated...\n")
                else:
                    print("There is no patient with this information.\n")
            elif choice == 4:
                ID = input("ID : ")
                if hospital.delete_patient(ID):
                    print("Patient registration is deleting...")
                    time.sleep(1.5)
                    print("Patient registration deleted.\n")
                else:
                    print("There is no patient with this information.\n")
            elif choice == 5:
                print("Exiting program...")
                time.sleep(1.5)
                print("THANK YOU FOR USING OUR SYSTEM")
                break
            else:
                print("Invalid choice. Please pay attention\n")


