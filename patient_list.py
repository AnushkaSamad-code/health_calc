patient = [
    {"name":"Anushka", "weight" : 60 , "status" : "Healthy"},
    {"name":"Laiba", "weight" : 85 , "status" : "Overweight"},
    {"name":"Samiya", "weight" :45 , "status" : "Underweight"},
]
print("---HOSPTAL PATIENT RECORD---")
for p in patient:
    print(f"Patient Name:{p['name']} | Weight: {p['weight']}kg | Status: {p['status']}")