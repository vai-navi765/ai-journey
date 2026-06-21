with open("resume.txt")as file:
    content = file.read()
print(content)
lines = content.split("\n")
print(content)
resume_data = {}
for line in lines:
    if ":" in line:
        parts = line.split(":",1)
        key = parts[0].strip()
        value = parts[1].strip()
        resume_data[key] = value
        
print(resume_data)

