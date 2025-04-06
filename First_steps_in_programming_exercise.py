#
import math

def UsdtoBgn():
    usd = float(input())
    bgn = usd * 1.79549
    print(bgn)

def RadianstoDegrees():
    radians = float(input("Enter radians amount: ")) 
    degrees = radians * 180 / pi
    print (degrees)

def DepositCalculator():
    DepositAmount = float(input())
    Time = int(input())
    YIR = float(input())
    interest = DepositAmount * (YIR/100)
    monthInterest = interest/12
    total_sum = Time * monthInterest + DepositAmount
    print(total_sum)

def VacationBookList():
    pages = int(input())
    pagesPerHour = int(input())
    days = int(input())
    TotalHours = pages / pagesPerHour
    neededHoursPerDay = TotalHours / days
    print(math.floor(neededHoursPerDay))

def SuppliesForSchool():
    pens = int(input())
    markers = int(input())
    liquid = int(input())
    discount = int(input())
    pricePens = pens * 5.8
    priceMarkers = markers * 7.2
    priceLiquid = liquid * 1.20
    TotalPrice = priceLiquid + priceMarkers + pricePens
    FinalSum = TotalPrice - (TotalPrice * discount/100)
    print(FinalSum)

def Repainting():
    nailon = int(input())
    paint = int(input())
    thinner = int(input())
    WorkHours = int(input())
    bag = 0.4
    nailonSum = (nailon + 2) * 1.5
    paintSum = (paint + paint*0.1) * 14.5
    thinnerSum = thinner * 5
    TotalSumMaterials = nailonSum + paintSum + thinnerSum + bag
    TotalSumWorkers = (TotalSumMaterials * 0.3) * WorkHours
    TotalSum = TotalSumMaterials + TotalSumWorkers
    print(TotalSum)

def FoodDelivery():
    chickenMenu = 10.35
    fishMenu = 12.40
    vegeterianMenu = 8.15

    chicken = int(input())
    fish = int(input())
    vegeterian = int(input())

    totalMenuSum = chickenMenu * chicken + fish*fishMenu + vegeterian * vegeterianMenu
    dessertPrice = totalMenuSum * 0.2
    total_Sum = totalMenuSum + dessertPrice + 2.50

    print(total_Sum)

def BasketballEquipment():
    basketballPrice = float(input())
    shoesPrice = basketballPrice - basketballPrice * 0.4
    jerseyPrice = shoesPrice - shoesPrice * 0.2
    ballPrice = jerseyPrice / 4
    accPrice = ballPrice / 5
    Total = basketballPrice + shoesPrice + jerseyPrice + ballPrice + accPrice
    print(Total)

def Aquarim():
    a = int(input())
    b = int(input())
    c = int(input())
    percent = float(input())
    s = a * b * c
    liters = s * 0.001
    neededliters = liters * (1-percent/100)
    print(neededliters)
