#GRADING SCORE with subject sumary
subject = input("Enter subject name: ")

gg = input("Enter Score: ")
gg = float(gg)

if gg < 0.0 or gg > 1.0:
    print("Error: Score out of range")
else:
    if gg >= 0.9:
        grade = 'A'
    elif gg >= 0.8:
        grade = 'B'
    elif gg >= 0.7:
        grade = 'C'
    elif gg >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
        
    print(grade)





