import time
import faker
from random import randint


# Faker
fake = faker.Faker()

# Patient class
class PatientRecord:
    def __init__(self, id, name, admission_date):
        self.id = id
        self.name = name
        self.admission_date = admission_date
    
    def __str__(self):
        return f"Patient {self.name} (ID: {self.id}) admitted on {self.admission_date}"

#Patient Generator
def generate_patients(num_patients=1000):
    patients = []
    for _ in range(num_patients):
        patient_id = randint(100, 1000000)
        name = fake.name()
        admission_date = fake.date_between(start_date="-30d", end_date="today").strftime('%m/%d/%Y')
        patients.append(PatientRecord(patient_id, name, admission_date))
    return patients

#Bubble Sort
def bubble_sort(patients):
    start = time.time()
    for i in range(len(patients)):
        for j in range(len(patients) - 1):
            if patients[j].id > patients[j + 1].id:
                patients[j], patients[j + 1] = patients[j + 1], patients[j]
    end = time.time()
    return patients, end - start

#Merge Sort
def merge(left_half, right_half):
    left_index = 0
    right_index = 0
    tmp_list = []
    
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index].id > right_half[right_index].id:
            tmp_list.append(right_half[right_index])
            right_index += 1
        else:
            tmp_list.append(left_half[left_index])
            left_index += 1
            
    # Add remaining elements from left half
    tmp_list.extend(left_half[left_index:])
    # Add remaining elements from right half
    tmp_list.extend(right_half[right_index:])
    
    return tmp_list

def merge_sort_timer(patients):
    start = time.time()
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        
        return merge(left_half, right_half)
    
    sorted_patients = merge_sort(patients)
    end = time.time()
    return sorted_patients, end - start

#Run Tests
def test_sorting():
    patients = generate_patients()
    print("Patients before sorting:")
    for patient in patients[:5]: 
        print(patient)
    
    print("\nStarting Bubble Sort...")
    sorted_bubble, bubble_time = bubble_sort(patients.copy())
    for patient in sorted_bubble[:5]:
        print(patient)
    print(f"Bubble Sort took {bubble_time:.6f} seconds")
    
    print("\nStarting Merge Sort...")
    sorted_merge, merge_time = merge_sort_timer(patients.copy())
    for patient in sorted_merge[:5]:
        print(patient)
    print(f"Merge Sort took {merge_time:.6f} seconds")

if __name__ == "__main__":
    test_sorting()