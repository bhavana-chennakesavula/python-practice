students = {
    "Bhavana": {"marks": [92, 88, 95, 78, 85], "branch": "AI/ML"},
    "Ravi":    {"marks": [70, 65, 80, 72, 68], "branch": "CSE"},
    "Priya":   {"marks": [95, 98, 92, 96, 99], "branch": "AI/ML"},
    "Arjun":   {"marks": [50, 45, 60, 55, 48], "branch": "CSE"},
    "Sneha":   {"marks": [75, 80, 78, 82, 79], "branch": "AI/ML"}
}
print(f"Total no.of students: {len(students)}")
avg_bhavana = sum(students['Bhavana']['marks']) / len(students['Bhavana']['marks'])
print(f"Bhavana: {avg_bhavana:.2f}")
avg_ravi = sum(students['Ravi']['marks']) / len(students['Ravi']['marks'])
print(f"Ravi: {avg_ravi:.2f}")
avg_priya = sum(students['Priya']['marks']) / len(students['Priya']['marks'])
print(f"Priya: {avg_priya:.2f}")
avg_arjun = sum(students['Arjun']['marks']) / len(students['Arjun']['marks'])
print(f"Arjun: {avg_arjun:.2f}")
avg_sneha = sum(students['Sneha']['marks']) / len(students['Sneha']['marks'])
print(f"Sneha: {avg_sneha:.2f}")
averages = {"Bhavana": avg_bhavana, "Ravi": avg_ravi, "Priya": avg_priya, "Arjun": avg_arjun, "Sneha": avg_sneha}
topper = max(averages, key=averages.get)
lowest_student = min(averages, key=averages.get)
print(f"Topper: {topper} with {averages[topper]:.2f}")
print(f"Lowest: {lowest_student} with {averages[lowest_student]:.2f}")
branches = students['Arjun']['branch'], students['Ravi']['branch'], students['Priya']['branch'], students['Sneha']['branch'], students['Bhavana']['branch']
branch_set = set(branches)
print(f"Total unique branches: {len(branch_set)}")
passing_mark = 60
result = {True: "Pass", False: "Fail"}
pf_bhavana = avg_bhavana >= passing_mark
pf_ravi = avg_ravi >= passing_mark  
pf_priya = avg_priya >= passing_mark
pf_arjun = avg_arjun >= passing_mark
pf_sneha = avg_sneha >= passing_mark
print(f"Bhavana: {result[pf_bhavana]}")
print(f"Ravi: {result[pf_ravi]}")
print(f"Priya: {result[pf_priya]}")
print(f"Arjun: {result[pf_arjun]}")
print(f"Sneha: {result[pf_sneha]}")
aiml_count = (students['Bhavana']['branch'] == 'AI/ML') + (students['Ravi']['branch'] == 'AI/ML') + (students['Priya']['branch'] == 'AI/ML') + (students['Arjun']['branch'] == 'AI/ML') + (students['Sneha']['branch'] == 'AI/ML')
print(f"Students from AI/ML: {aiml_count}")