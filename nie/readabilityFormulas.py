def FleschLabel(flesch: float):
    # US School level equivalence
    if flesch >= 100:
        return 0 # Irrelevant
    if flesch >= 90:
        return 1 # 5th grade
    elif flesch >= 80:
        return 2 # 6th grade
    elif flesch >= 70:
        return 3 # 7th grade
    elif flesch >= 60:
        return 4 # 8th and 9th grade
    elif flesch >= 50:
        return 5 # 10th to 12th grade
    elif flesch >= 30:
        return 6 # College
    elif flesch >= 10:
        return 7 # College graduate
    elif flesch >= 0:
        return 8 # Professional
    else:
        return 9 # Irrelevant