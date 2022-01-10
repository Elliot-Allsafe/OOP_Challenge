class Organs:
    name = ""
    age = 0
class left_eye:
    name = "Left Eye"
    medical_condition = "Short Sighted"
    color = "Blue"
class right_eye(left_eye):
    name = "Right Eye"
class Heart:
    name = "Heart"
    medical_condition = "Perfect"
class Stomach:
    name = "Stomach"
    medical_condition = "Need to Be Fed."
    fed_status = "NO"

    def fed_s(self):
        Stomach.fed_status = "Yes"
        Stomach.medical_condition = "Perfect."
class Skin:
    name = "Skin"
    medical_condition = "Burned."
    operation_status = "NO"

    def sk(self):
        Skin.medical_condition = "Perfect"
        Skin.operation_status = "Yes"
