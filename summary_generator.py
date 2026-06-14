import json

# Read transcript file
with open("sample_transcript.txt", "r") as file:
    transcript = file.read().lower()

# Extract information
skills = []
strengths = []
improvements = []

# Skills detection
skill_keywords = ["python", "java", "sql", "c++", "javascript"]

skill_names = {
    "python": "Python",
    "java": "Java",
    "sql": "SQL",
    "c++": "C++",
    "javascript": "JavaScript"
}

for skill in skill_keywords:
    if skill in transcript:
        skills.append(skill_names[skill])

# Strengths detection
if "problem solving" in transcript:
    strengths.append("Problem Solving")

if "teamwork" in transcript:
    strengths.append("Teamwork")

if "leadership" in transcript:
    strengths.append("Leadership")

# Areas for improvement detection
if "communication" in transcript:
    improvements.append("Communication Skills")

if "time management" in transcript:
    improvements.append("Time Management")

# Generate summary
summary = f"Candidate demonstrated knowledge of {', '.join(skills)}. "

if strengths:
    summary += f"Key strengths include {', '.join(strengths)}. "

if improvements:
    summary += f"Areas for improvement include {', '.join(improvements)}."

# JSON Output
output = {
    "summary": summary
}

print(json.dumps(output, indent=4))