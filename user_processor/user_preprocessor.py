users = [  # Sample user data to be processed
    {
        "firstName": "Nayanava",
        "lastName": "Biswas",
        "projectCode": "A11234",
        "location": "IN",
        "department": "Engineering"
    },
    {
        "firstName": "Bilqis",
        "lastName": "Afroz",
        "projectCode": "Z1234",
        "location": "IN",
        "department": "Engineering"
    },
    {
        "firstName": "Ravi",
        "lastName": "Gupta",
        "projectCode": "K1234",
        "location": "IN",
        "department": "Engineering"
    }
]

region_map = {
    "IN": "India",
    "US": "United States"
}
deptcode_map = {
    "Engineering": "ENG",
    "Consulting": "CNS"
}

def preprocessor(user):
    location = user.get("location")
    department = user.get("department")
    projectCode = user.get("projectCode")
    region = region_map.get(location, "Global")
    dept_code = deptcode_map.get(department, "GENERAL")
    
    if projectCode:
        if projectCode.startswith("Z"):
            project_group = "Zeta"
        elif projectCode.startswith("A"):
            project_group = "Alpha"
        else:
            project_group = "Misc"
    else:
        project_group = "Misc"
    
    return {
        "firstName": user["firstName"],
        "lastName": user["lastName"],
        "region": region,
        "dept_code": dept_code,
        "project_group": project_group
    }

# Generate user tags and print
for user in users:
    enriched = preprocessor(user)
    user_tag = f"{enriched['project_group']}-{enriched['dept_code']}{enriched['firstName']}.{enriched['lastName']}@{enriched['region']}"
    print(user_tag)