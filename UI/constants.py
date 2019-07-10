
def get(key):
    json = {
        "WINDOWNAME" : 'COM',
        "WIDTH" : 700,
        "HEIGHT" : 700,
        "WHITE" : (255, 255, 255),
        "BLACK" : (0, 0, 0),
        "RED" : (255, 0, 0),
        "GREEN" : (0, 255, 0),
        "BLUE" : (0, 0, 255),
        "YELLOW" : (255, 255, 255),
        "REGEX_BINOM" : "(\((-|).*,(-|).*\))",
        "REGEX_POLAR" : "(\[(-|).*;(-|).*\])"
    }
    return json[key]
    