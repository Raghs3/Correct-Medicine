from prescription_data import patients, adverse_interactions
from set_union import meds_to_watch

for patient, prescription in patients.items():
    overlap = prescription & meds_to_watch

    for interaction in adverse_interactions:
        if interaction <= overlap:
            print(f"{patient} is taking a medication that interacts with another medication.")
            break
