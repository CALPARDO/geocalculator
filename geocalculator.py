import time
print("-------------------------------------------")
print("| Geometry Calculator by Derin Durak V2.1 |")
print("-------------------------------------------")
time.sleep(2)
print("")
print("")
print("Press ENTER to start")
prs = input()
if prs == "":
    print("")
else:
    exit()

#main loop
while True:
    #print the instructions and the shape options
    print("----------------------------------")
    print("Choose a Shape:")
    print("1 -> Triangle")
    print("2 -> Rectangle")
    print("3 -> Square")
    print("4 -> Trapezoid")
    print("----------------")
    menu = input()

    #Triangle Option
    if menu == "1":
        print("----------------")
        print("Choose an Action:")
        print("1 -> Area")
        print("2 -> Surround")
        print("----------------") 
        action1 = input()
        if action1 == "1":
            print("----------------")
            tri_base =   float(input ("Enter the triangle's base in cm: "))
            tri_height =   float(input ("Enter the triangle's height in cm: "))
            print("----------------")
            print("Your Triangle's Area is ",format(tri_base*tri_height/2),"cm2")
        elif action1 == "2":
            print("----------------")
            tri_edge1 =   float(input ("Enter the triangle's first edge in cm: "))
            tri_edge2 =   float(input ("Enter the triangle's second edge in cm: "))
            tri_edge3 =   float(input ("Enter the triangle's third edge in cm: "))
            print("----------------")
            print("Your Triangle's Surround is ",format(tri_edge1+tri_edge2+tri_edge3),"cm")
        else :
            print("----------------")
            print("You Entered Wrong Value")

    #Rectangle Option
    if menu == "2":
        print("----------------")
        print("Choose an Action:")
        print("1 -> Area")
        print("2 -> Surround")
        print("----------------")  
        action2 = input()
        if action2 == "1":
            print("----------------")
            rec_edge1 =   float(input ("Enter the rectangle's first edge in cm: "))
            rec_edge2 =   float(input ("Enter the rectangle's second edge in cm: "))
            print("----------------")
            print("Your Rectangular's Area is ",format(rec_edge1*rec_edge2),"cm2")
        elif action2 == "2":
            print("----------------")
            rec_edge1 =   float(input ("Enter the rectangle's first edge in cm: "))
            rec_edge2 =   float(input ("Enter the rectangle's second edge in cm: "))
            print("----------------")
            print("Your Rectangular's Surround is ",format(2*rec_edge1 + 2*rec_edge2),"cm")
        else :
            print("----------------")
            print("You Entered a Wrong Value")

    #Square Option
    if menu == "3":
        print("----------------")
        print("Choose an Action:")
        print("1 -> Area")
        print("2 -> Surround")
        print("----------------")  
        action3 = input()
        if action3 == "1":
            print("----------------")
            squ_edge =   float(input ("Enter the square's edge in cm: "))
            print("----------------")
            print("Your Square's Area is ",format(squ_edge**2),"cm2")
        elif action3 == "2":
            print("----------------")
            squ_edge =   float(input ("Enter the square's edge in cm: "))
            print("----------------")
            print("Your Rectangular's Surround is ",format(4*squ_edge),"cm")
        else :
            print("----------------")
            print("You Entered Wrong Value")

    #Trapezoid Option
    if menu == "4":

        print("----------------")
        print("Choose an Action:")
        print("1 -> Area")
        print("2 -> Surround")
        print("----------------")  
        action4 = input()
        if action4 == "1":
            print("----------------")
            trap_edge1 =   float(input ("Enter the trapezoid's top edge in cm: "))
            trap_edge2 =   float(input ("Enter the rectangle's bottom edge in cm: "))
            trap_h =   float(input ("Enter the trapezoid's height in cm: "))
            print("----------------")
            print("Your Trapezoid's Area is ",format((trap_edge1+trap_edge2)*trap_h/2),"cm2")
        elif action4 == "2":
            print("----------------")
            trap_edge1 =   float(input ("Enter the rectangle's top edge in cm: "))
            trap_edge2 =   float(input ("Enter the rectangle's bottom edge in cm: "))
            trap_edge3 =   float(input ("Enter the trapezoid's right edge in cm: "))
            trap_edge4 =   float(input ("Enter the trapezoid's left edge in cm: "))
            print("----------------")
            print("Your Trapezoid's Surround is ",format(trap_edge1+trap_edge2+trap_edge3+trap_edge4),"cm")
        else :
            print("----------------")
            print("You Entered Wrong Value")

    #Wrong Value
    if menu != "1" and menu != "2" and menu != "3" and menu != "4":
        print("----------------------------------")
        print("I don't understand, try again")
        time.sleep(1)
        continue

    #Do you want to continue part in the end
    print("----------------")
    time.sleep(2)
    print("Do you want to continue?")
    ans = input()
    if ans == "no":
        exit()
    if ans == "yes" or "y" or "ja" or "evet":
        continue
    else:
        exit()