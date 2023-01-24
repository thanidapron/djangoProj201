from django.shortcuts import render

# Create your views here.
def Header(request):
    return render(request, 'Header.html')
def base(request):
    return render(request, 'base.html')
def Home(request):
    return render(request, 'Home.html')
def Profile(request):
    return render(request, 'Profile.html')
def Education(request):
    return render(request, 'Education.html')
def Interests(request):
    return render(request, 'Interests.html')
def Sale(request):
    return render(request, 'Sale.html')
def Idol(request):
    return render(request, 'Idol.html')

def myShowData(request):
    ID = '65342310201-1'
    name = 'Thanidapron chaisomdet'
    gender = 'หญิง'
    Height = '174'
    weight = '56'
    Food = 'หมูกะทะ'
    Color = 'เหลือง'
    domicile = 'ร้อยเอ็ด'
    car = 'CPX'
    Pet = 'หมา'
    product = [
        ['CM001', '/static/images/myShowData/data1.jpg', 'DD Cream Watermelon SPF50 PA+++ ดีดีครีมกันแดดแตงโม', '39฿'],
        ['CM002', '/static/images/myShowData/data2.jpg', 'Jula s Herb Watermelon EE Cushion SPF50 PA+++', '49฿'],
        ['CM003', '/static/images/myShowData/data3.jpg', 'Carrot Daily Serum เซรั่มหน้าใสแครอท', '39฿'],
        ['CM004', '/static/images/myShowData/data4.jpg', 'Longan Melasma Serum เซรั่มลำไยลดฝ้า', '49฿'],
        ['CM005', '/static/images/myShowData/data5.jpg', 'Jula s Herb จุฬาเฮิร์บ หัวเชื้อเซรั่มกลูต้า-ไฮยาส้มแดง', '39฿'],
        ['CM006', '/static/images/myShowData/data6.jpg', 'Black Ginger all in one men serum เซรั่มบำรุงผิวหน้าขิงดำ สำหรับผู้ชาย', '49฿'],
        ['CM007', '/static/images/myShowData/data7.jpg', 'MORINGA ADVANCE REPAIR GEL เจลมะรุม ลดหลุมสิว ลดรอยดำ รอยแดง รอยแผลเป็น', '49฿'],
        ['CM008', '/static/images/myShowData/data8.jpg', 'MARIGOLD INTENSIVE CLEAR GEL เจลดาวเรืองลดสิวสูตรใหม่ ', '39฿'],
        ['CM009', '/static/images/myShowData/data9.jpg', 'Jula s Herb จุฬาเฮิร์บ สบู่แตงโมผิวกระจ่างใส', '49฿'],
        ['CM010', '/static/images/myShowData/data10.jpg', 'Jula s Herb จุฬาเฮิร์บ สบู่ดาวเรืองลดสิว', '49฿'],
    ]
    context = {'ID':ID,'name':name,'gender':gender,'Height':Height,'weight':weight
        ,'Food':Food,'Color':Color,'domicile':domicile,'car':car,'Pet':Pet,'product':product}
    return render(request, 'myShowData.html',context)