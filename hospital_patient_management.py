def search_patients_by_disease(patients_records, disease_name):
    found_patients = []
    for patient in patients_records:
        if patient.get("Disease", "").lower() == disease_name.lower():
            found_patients.append(patient["Name"])
            
    return found_patients
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"},
    {"Name": "David", "Age": 50, "Disease": "Pneumonia"}
]
search_disease = "Flu"
matching_patients = search_patients_by_disease(patients, search_disease)
print(f"Patients with {search_disease}: {matching_patients}")