class Doctor:
    def __init__(self, Id, Name, Speciality, Timing, Qualification, RoomNumber):
        self.Id = Id
        self.Name = Name
        self.Speciality = Speciality
        self.Timing = Timing
        self.Qualification = Qualification
        self.RoomNumber = RoomNumber

    def display(self):
        print(
            f"{self.Id:<5}{self.Name:<24}{self.Speciality:<15}{self.Timing:<15}{self.Qualification:<15}{self.RoomNumber:<10}")


doctors = [
    Doctor(21, "Dr.Gody", "ENT", "5am-11aM", "MBBS,MD", 17),
    Doctor(32, "Dr.Vikram", "Physician", "10pm-3am", "MBBS,MD", 45),
    Doctor(17, "Dr.Amy", "Surgeon", "8pm-2am", "BDM", 8),
    Doctor(33, "Dr.David", "Artho", "10am-4pm", "MBBS,MS", 40),
    Doctor(123, "Dr. Ross", "Headackes", "8pm-10am", "MST", 102),
    Doctor(66, "Dr. Mike", "Heart", "9am-5pm", "MS", 2)
]


class Facility:
    def __init__(self, Name):
        self.Name = Name

    def display(self):
        print(f"{self.Name:<20}")


facilities = [
    Facility("Ambulance"),
    Facility("Admissions"),
    Facility("Canteen"),
    Facility("Emergency")
]


class Laboratory:
    def __init__(self, Name, Cost):
        self.Name = Name
        self.Cost = Cost

    def display(self):
        print(f"{self.Name:<15}{self.Cost:<10}")


laboratories = [
    Laboratory("Lab1", 800),
    Laboratory("Lab2", 1200),
    Laboratory("Lab3", 500),
    Laboratory("Lab4", 50)
]


class Patient:
    def __init__(self, ID, Name, Disease, Gender, Age):
        self.ID = ID
        self.Name = Name
        self.Disease = Disease
        self.Gender = Gender
        self.Age = Age

    def display(self):
        print(f"{self.ID:<5}{self.Name:<24}{self.Disease:<15}{self.Gender:<15}{self.Age:<10}")


patients = [
    Patient(12, "Pankaj", "Cancer", "Male", 30),
    Patient(13, "Janina", "Cold", "Female", 23),
    Patient(14, "Alonna", "Malaria", "Female", 45),
    Patient(15, "Ravi", "Diabetes", "Male", 65)
]


def main():
    while True:
        print("\nWelcome to Alberta Hospital (AH) Management system")
        print("Select from the following options, or select 0 to stop:")
        print("1 - Doctors")
        print("2 - Facilities")
        print("3 - Laboratories")
        print("4 - Patients")

        main_choice = input()

        if main_choice == '0':
            break
        elif main_choice == '1':
            while True:
                print("\nDoctors Menu:")
                print("1 - Display Doctors list")
                print("2 - Search for doctor by ID")
                print("3 - Search for doctor by name")
                print("4 - Add doctor")
                print("5 - Edit doctor info")
                print("6 - Back to the Main Menu")

                doctor_choice = input()

                if doctor_choice == '6':
                    break
                elif doctor_choice == '1':
                    print("\nId   Name                   Speciality      Timing          Qualification   Room Number")
                    for doctor in doctors:
                        doctor.display()
                elif doctor_choice == '2':
                    doctor_id = input("\nEnter the doctor Id:\n")
                    found = False
                    for doctor in doctors:
                        if str(doctor.Id) == doctor_id:
                            doctor.display()
                            found = True
                            break
                    if not found:
                        print("\nCan't find the doctor with the same ID on the system")
                elif doctor_choice == '3':
                    doctor_name = input("\nEnter the doctor name:\n")
                    found = False
                    for doctor in doctors:
                        if doctor.Name == doctor_name:
                            doctor.display()
                            found = True
                            break
                    if not found:
                        print("\nCan't find the doctor with the same name on the system")
                elif doctor_choice == '4':
                    id = int(input("\nEnter the doctor's ID:\n"))
                    name = input("Enter the doctor's name:\n")
                    speciality = input("Enter the doctor's speciality:\n")
                    timing = input("Enter the doctor's timing (e.g., 7am-10pm):\n")
                    qualification = input("Enter the doctor's qualification:\n")
                    room_number = int(input("Enter the doctor's room number:\n"))
                    new_doctor = Doctor(id, name, speciality, timing, qualification, room_number)
                    doctors.append(new_doctor)
                    print("\nDoctor added successfully!")
                elif doctor_choice == '5':
                    doctor_id = input("\nPlease enter the id of the doctor that you want to edit their information:\n")
                    found = False
                    for doctor in doctors:
                        if str(doctor.Id) == doctor_id:
                            print("\nEnter new Name:")
                            doctor.Name = input()
                            print("\nEnter new Specilist in:")
                            doctor.Speciality = input()
                            print("\nEnter new Timing:")
                            doctor.Timing = input()
                            print("\nEnter new Qualification:")
                            doctor.Qualification = input()
                            print("\nEnter new Room number:")
                            doctor.RoomNumber = input()
                            print("\nDoctor information updated successfully!")
                            found = True
                            break
                    if not found:
                        print("\nCan't find the doctor with the same ID on the system")
                else:
                    print("Invalid choice. Please select a valid option.")
        elif main_choice == '2':
            while True:
                print("\nFacilities Menu:")
                print("1 - Display Facilities list")
                print("2 - Add Facility")
                print("3 - Back to the Main Menu")

                facility_choice = input()

                if facility_choice == '3':
                    break
                elif facility_choice == '1':
                    print("\nThe Hospital  Facilities are:")
                    for facility in facilities:
                        facility.display()
                elif facility_choice == '2':
                    facility_name = input("\nEnter Facility name:\n")
                    new_facility = Facility(facility_name)
                    facilities.append(new_facility)
                    print("\nFacility added successfully!")
                else:
                    print("Invalid choice. Please select a valid option.")
        elif main_choice == '3':
            while True:
                print("\nLaboratories Menu:")
                print("1 - Display laboratories list")
                print("2 - Add laboratory")
                print("3 - Back to the Main Menu")

                laboratory_choice = input()

                if laboratory_choice == '3':
                    break
                elif laboratory_choice == '1':
                    print("\nLab             Cost")
                    for laboratory in laboratories:
                        laboratory.display()
                elif laboratory_choice == '2':
                    laboratory_name = input("\nEnter Laboratory facility:\n")
                    laboratory_cost = int(input("Enter Laboratory cost:\n"))
                    new_laboratory = Laboratory(laboratory_name, laboratory_cost)
                    laboratories.append(new_laboratory)
                    print("\nLaboratory added successfully!")
                else:
                    print("Invalid choice. Please select a valid option.")
        elif main_choice == '4':
            while True:
                print("\nPatients Menu:")
                print("1 - Display patients list")
                print("2 - Search for patient by ID")
                print("3 - Add patient")
                print("4 - Edit patient info")
                print("5 - Back to the Main Menu")

                patient_choice = input()

                if patient_choice == '5':
                    break
                elif patient_choice == '1':
                    print("\nID   Name                   Disease         Gender          Age")
                    for patient in patients:
                        patient.display()
                elif patient_choice == '2':
                    patient_id = int(input("\nEnter the Patient Id:\n"))
                    found = False
                    for patient in patients:
                        if patient.ID == patient_id:
                            patient.display()
                            found = True
                            break
                    if not found:
                        print("\nCan't find the Patient with the same id on the system")
                elif patient_choice == '3':
                    id = int(input("\nEnter Patient id:\n"))
                    name = input("Enter Patient name:\n")
                    disease = input("Enter Patient disease:\n")
                    gender = input("Enter Patient gender:\n")
                    age = int(input("Enter Patient age:\n"))
                    new_patient = Patient(id, name, disease, gender, age)
                    patients.append(new_patient)
                    print("\nPatient added successfully!")
                elif patient_choice == '4':
                    patient_id = int(
                        input("\nPlease enter the id of the Patient that you want to edit their information:\n"))
                    found = False
                    for patient in patients:
                        if patient.ID == patient_id:
                            print("\nEnter new Name:")
                            patient.Name = input()
                            print("\nEnter new disease:")
                            patient.Disease = input()
                            print("\nEnter new gender:")
                            patient.Gender = input()
                            print("\nEnter new age:")
                            patient.Age = int(input())
                            print("\nPatient information updated successfully!")
                            found = True
                            break
                    if not found:
                        print("\nCan't find the Patient with the same id on the system")
                else:
                    print("Invalid choice. Please select a valid option.")
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
