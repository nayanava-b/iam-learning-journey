users = [ #Sample user data to be processed
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

region_map = { #Key-value pairs to map the location of the user to a region
    "IN": "India",
    "US": "United States",
}
deptcode_map = { #Key-value pairs to map the department of the user to a department code
    "Engineering": "ENG",
    "Consulting": "CNS"
}

def preprocessor(user):
    location = user.get("location") #To bring in the location of the user within the scope of the preprocessor
    department = user.get("department")
    projectCode = user.get("projectCode")
    region = region_map.get(location, "Global")
    dept_code = deptcode_map.get(department, "GENERAL")
    if projectCode is not None:
        if projectCode.startswith("Z"): #To map the condition for generation of project groups
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
    project_group = enriched['project_group']
    dept_code = enriched['dept_code']
    first_name = enriched['firstName']
    last_name = enriched['lastName']
    region = enriched['region']
    user_tag = f"{project_group}-{dept_code}{first_name}.{last_name}@{region}"
    print(user_tag)
    enriched = preprocessor(user) #Variable to call the preprocessor function on each user
    user_tag = f"{enriched['project_group']}-{enriched['dept_code']}{enriched['firstName']}.{enriched['lastName']}@{enriched['region']}"
    print(user_tag)