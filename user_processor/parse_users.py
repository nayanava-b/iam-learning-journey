import json
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
combined_users=[]
for user in users:
    # Build admin_list
    chosendataset = {
        "username": user["username"],
        "country": user["location"],
        "is_admin": user["role"] == "Admin"
    }
    if user["role"] == "Admin":
        admin_list.append(chosendataset)

    # Build developer_list
    if user["location"] == "IN" or user["role"] == "Developer":
        anotherset = {
            "username": user["username"],
            "country": user["location"],
            "is_developer": user["role"] == "Developer"
        }
        developer_list.append(anotherset)

    # Build transformed_list
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

# Write admin_list to file
with open('admin_list.json', 'w') as f:
    json.dump(admin_list, f, indent=3)
# Write developer_list to file
with open('developer_list.json', 'w') as f:
    json.dump(developer_list, f, indent=3)
# Write transformed_list to file
with open('transformed_list.json', 'w') as f:
    json.dump(transformed_list, f, indent=3)

# Combine all lists into a single dictionary and write to file
combine_users = {
    "admin_list": admin_list,
    "developer_list": developer_list,
    "transformed_list": transformed_list
}
print(combine_users)
with open('allusers.json', 'w') as f:
    json.dump(combine_users, f, indent=3)
