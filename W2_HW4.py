def bmi(weight,height):
    kg = weight * 0.45359237
    h_square = (height * 0.0254) ** 2
    bmi = kg / h_square
    return bmi