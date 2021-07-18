
"""
weight = float(input())
height = float(input())

BMI = weight / pow(height, 2)
if(BMI < 18.5):
    print('Underweight')
elif (( (BMI >= 18.5)  and (BMI < 25))):
    print('Normal')
elif (BMI >= 25 and BMI < 30) :
    print('Overweight')
else :
    print('Obesity')
"""

def BMI(cannang,chieucao):
    return cannang/(chieucao**2)

def PhanLoai(BMI):
    if BMI < 18.5:
        return 'Bạn quá gầy'
    elif BMI <= 24.9:
        return  'Bạn bình thường'
    elif BMI <= 29.9:
        return 'Bạn hơi béo'
    elif BMI <= 34.9:
        return 'Bạn béo phì cấp độ 1'
    elif BMI <= 39.9:
        return 'Bạn béo phì cấp độ 2'
    else:
        return 'Bạn béo phì cấp độ 3'

def NguyCoBenh(BMI):
    if BMI < 18.5:
        return 'Nguy cơ mắc bệnh thấp'
    elif BMI <= 24.9:
        return  'Nguy cơ mắc bệnh trung bình'
    elif BMI <= 29.9:
        return 'Nguy cơ mắc bệnh cao'
    elif BMI <= 34.9:
        return 'Nguy cơ mắc bệnh cao'
    elif BMI <= 39.9:
        return 'Nguy cơ mắc bệnh rất  cao'
    else:
        return 'Nguy  hiểm'

x = float(input('Nhập vào cân nặng của bạn : '))
y = float(input('Nhập vào chiều cao của bạn : '))
bmi = BMI(x, y)
print('BMI của bạn = ', bmi)
print(PhanLoai(bmi))
print(NguyCoBenh(bmi))
