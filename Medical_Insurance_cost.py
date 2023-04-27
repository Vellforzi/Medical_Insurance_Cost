import csv

# tasks:
# 1) Average age of the patients+
# 2) Where a majority of the individuals are from+
# 3) Insurance cost between smokers vs non_smokers+
# 4) Average age for someone who has at least one child+
# 5) How BMI influence to insurance cost+
# insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_children + 24000 * smoker - 12500

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


def load_data(list_, csv_file, column_name):  # transfer all info from csv file to according list
    with open(csv_file) as insurance_file:
        insurance_dict = csv.DictReader(insurance_file)
        for row in insurance_dict:
            list_.append(row[column_name])
        return list_


load_data(ages, "insurance.csv", "age")
load_data(sexes, "insurance.csv", "sex")
load_data(bmis, "insurance.csv", "bmi")
load_data(num_children, "insurance.csv", "children")
load_data(smoker_statuses, "insurance.csv", "smoker")
load_data(regions, "insurance.csv", "region")
load_data(insurance_charges, "insurance.csv", "charges")
# print(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)


class PatientsAnalysis:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children,
                 patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_dictionary = None
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    def create_dictionary(self):  # full patients info in dict
        self.patients_dictionary = {"Age": [int(age) for age in self.patients_ages],
                                    "Sex": [1 if sex == "male" else 0 for sex in self.patients_ages],
                                    "BMI": [float(bmi) for bmi in self.patients_bmis],
                                    "Children": [int(children) for children in self.patients_num_children],
                                    "Smoker": [1 if smoker == "yes" else 0 for smoker in self.patients_smoker_statuses],
                                    "Region": self.patients_regions,
                                    "Charges": [float(charges) for charges in self.patients_charges]}
        return self.patients_dictionary

    def average_age(self):  # method finds the average age of patients
        total_age = 0
        for age in self.patients_ages:  # counts all ages
            total_age += int(age)
        return f"Average patient age: {round(total_age/len(self.patients_ages), 2)} years."  # total ages divided
        # by length of ages list

    def unique_region(self):  # method finds unique region individuals are from
        unique_region = []
        for region in self.patients_regions:
            if region not in unique_region:
                unique_region.append(region)
        return unique_region

    def average_charges(self):  # method finds average charges for all patients
        total_charges = 0
        for charge in self.patients_charges:
            total_charges += float(charge)
        return f"Average patients charge: {round(total_charges/len(self.patients_charges), 2)} dollars."  # total
        # charges divided by length of insurance charges list

    def sexes_analysis(self):  # method finds how many males and females in dataset
        males = 0
        females = 0
        for sex in self.patients_sexes:
            if sex == "male":
                males += 1
            else:
                females += 1
        print(f'Total amount of Males: {males}')
        print(f'Total amount of Females: {females}')

    def average_age_with_child(self):  # method finds average age of patients with at least one child
        patient_with_child = 0
        total_age = 0
        for child in self.patients_num_children:
            if child != "0":
                patient_with_child += 1
                current_index = self.patients_num_children.index(child)
                current_age = int(self.patients_ages[current_index])
                total_age += current_age
        return f'Average patients age with at least one child: {round(total_age/patient_with_child, 2)}'

    def min_max_bmi(self):  # method finds min and max value of bmi
        min_value = 0
        max_value = 0
        for bmi in self.patients_bmis:
            bmi = float(bmi)
            if min_value == 0 and max_value == 0:
                min_value = bmi
                max_value = bmi
            if bmi > max_value:
                max_value = bmi
            elif bmi < min_value:
                min_value = bmi
        return f'Min BMI: {min_value}. Max BMI: {max_value}.'

    # method finds influence bmi on insurance cost not changing rest data
    def bmi_influence(self, patient_number, min_value, max_value):
        patient_number -= 1
        print(f"Number 1 patient's info: age - {self.patients_dictionary['Age'][patient_number]}, "
              f"sex - {self.patients_dictionary['Sex'][patient_number]}, "
              f"num_of_children - {self.patients_dictionary['Children'][patient_number]},"
              f"smoker - {self.patients_dictionary['Smoker'][patient_number]}.")
        bmi_range = [round(min_value), round(max_value)]
        for bmi in range(bmi_range[0], bmi_range[1] + 1):
            new_insurance_cost = 250 * self.patients_dictionary["Age"][patient_number] - \
                             128 * self.patients_dictionary["Sex"][patient_number] + \
                             370 * bmi + 425 * self.patients_dictionary["Children"][patient_number] + \
                             24000 * self.patients_dictionary["Smoker"][patient_number] - 12500
            print(f"His insurance cost depending on BMI: {new_insurance_cost}")

    def smoker_vs_no_smoker(self):  # method compare insurance costs with smoker and no-smoker statuses
        i = 0
        for smoker_status in self.patients_smoker_statuses:
            insurance_cost = self.patients_dictionary["Charges"][i]
            if smoker_status == "yes":
                vs_insurance_cost = round((250 * self.patients_dictionary["Age"][i] -
                                           128 * self.patients_dictionary["Sex"][i] +
                                           370 * self.patients_dictionary["BMI"][i] +
                                           425 * self.patients_dictionary["Children"][i] + 24000 * 0 - 12500), 5)
            else:
                vs_insurance_cost = round((250 * self.patients_dictionary["Age"][i] -
                                           128 * self.patients_dictionary["Sex"][i] +
                                           370 * self.patients_dictionary["BMI"][i] +
                                           425 * self.patients_dictionary["Children"][i] + 24000 * 1 - 12500), 5)
            print(f"Smoker: {smoker_status}. Original cost: {insurance_cost}. New cost: {vs_insurance_cost}. "
                  f"The difference: {round(abs(vs_insurance_cost-insurance_cost), 5)}")
            i += 1


patient_info = PatientsAnalysis(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
patient_info.create_dictionary()
print(patient_info.smoker_vs_no_smoker())
