def es_bisiesto(anyo):
    
    if anyo % 4 == 0:
        if anyo % 100 == 0 and anyo % 400 != 0:
            return False
        else:
            return True
    return False

