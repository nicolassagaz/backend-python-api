def validate_titlw(title):

    if title.strip() == "":
        return False
    
    if len(title) < 3:
        return False
    
    return True