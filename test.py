users=[{
      "username": "Ajay",
      "location": "IN",
      "role": "Admin",
      "department": "Engineering"	
    },
    {
      "username": "Karen",
      "location": "US",
      "role": "Developer",
      "department": "Consulting"
    },
    {
      "username": "Fahmie",
      "location": "FR",
      "role": "Intern",
      "department": "HR"
    }
    ]

admin_list = []
developer_list = []
transformed_list = []

for user in users:
    chosendataset = {
        "username": user["username"],
        "country": user["location"],
        "is_admin": user["role"] == "Admin"
    }
    admin_list.append(chosendataset)

for user in users:
    if user["location"] == "IN" or user["role"] == "Developer":
        anotherset = {
            "username": user["username"],
            "country": user["location"],
            "is_developer": user["role"] == "Developer"
        }
        developer_list.append(anotherset)

for user in users:
    if user["role"] == "Admin":
        transformed_role = "SYSTEM-ADMIN"
    elif user["role"] == "Developer":
        transformed_role = "ENG-DEV"
    elif user["role"] == "Intern":
        transformed_role = "TEMP-CONTRACT"
    else:
        transformed_role = "UNKNOWN"
    transformed = {
        "username": user["username"],
        "location": user["location"],
        "transformed_role": transformed_role
    }
    transformed_list.append(transformed)
    
print(transformed_list)