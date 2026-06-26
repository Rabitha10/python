student=[]

def calculate_avarege(score):
    if len(score)==0:
        return 0
    return sum(score)/len(score)

def get_lettergrade(avg):
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    elif avg>=60:
        return "D"
    else:
        return "F"
    


