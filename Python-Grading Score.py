#GRADING SCORE
sg = input("Enter Score: ")
sg = float(sg)

if sg < 0.0 or sg > 1.0:
    print("Error: Score out of range")
else:
    if sg >= 0.9:
        grade = 'A'
    elif sg >= 0.8:
        grade = 'B'
    elif sg >= 0.7:
        grade = 'C'
    elif sg >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
        
    print(grade)

