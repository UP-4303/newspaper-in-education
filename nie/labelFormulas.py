# Classes are based on US K-12 grades system
# For the functions named XX17, optimally:
# [0] Irrelevant (too easy)
# [1;12] correspond directly to the school year
# [13] College undergrad
# [14] College graduate
# [15] Professional
# [16] Irrelevant (too hard)
# For a total of 17 classes

# Fort the other functions, optimally:
# [3;12] correspond directly to the school year
# Returns None on irrelevant data

def fleschKincaidLabel(fleschKincaidScore: float | None):
    if fleschKincaidScore == None:
        return None
    label = int(fleschKincaidScore)
    if label < 3 or label > 12:
        return None
    else:
        return label

def fleschLabel17(flesch: float | None):
    if flesch == None:
        return None
    if flesch >= 100:
        return 0 # Irrelevant
    if flesch >= 90:
        return 5
    elif flesch >= 80:
        return 6
    elif flesch >= 70:
        return 7
    
    # Splitted manually
    elif flesch >= 65:
        return 8
    elif flesch >= 60:
        return 9
    
    # Splitted manually
    elif flesch >= 50 + (10/3*2): # (56.6)
        return 10
    elif flesch >= 50 + (10/3): # (53.3)
        return 11
    elif flesch >= 50:
        return 12

    elif flesch >= 30:
        return 13
    elif flesch >= 10:
        return 14
    elif flesch >= 0:
        return 15
    else:
        return 16 # Irrelevant