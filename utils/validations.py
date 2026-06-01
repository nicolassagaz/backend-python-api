def validate_title(title):

    if title.strip() == "":
        return False
    
    if len(title) < 3:
        return False
    
    return True