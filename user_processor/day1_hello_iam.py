print(" Starting my IAM automation journey!")
print("=" * 50)
users = [
    'john.doe@company.com',
    'jane.smith@company.com', 
    'bob.wilson@company.com'
]

department={
    'john.doe@company.com':'IT Security',
    'jane.smith@company.com': 'Human Resources',
    'bob.wilson@company.com': 'Finance'
}
print("📋 Current Users in System:")
print("-" * 30)

for user in users :
     dept=department.get(user,'Unknown')
     print(user + "|" +dept)
print("-" * 30)
print(f"Total users processed: {len(users)}")
print("Next: Add more IAM features!")