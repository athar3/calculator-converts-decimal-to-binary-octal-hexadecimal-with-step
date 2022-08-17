#CALCULATOR CONVERTS DECIMAL TO BINARY, OCTAL, AND HEXADECIMAL WITH STEP

#ATHAR MADE THIS SHIT WITH LOVE

#HOPE U CAN ENJOY!

#=============DECIMAL TO BINARY============================

def biner(desimal):
    des=desimal
    hasil=[]
    while(desimal != 0):
        bagi = desimal % 2
        print(f"{desimal} : 2 = {desimal//2} sisa {bagi}")
        desimal = desimal // 2
        hasil.append(bagi)

    hasil.reverse()
    print(f"desimal ke biner dari {des} = {hasil}")

#=============DECIMAL TO OCTAL============================

def oktal(desimal):
    okt=desimal
    hasil=[]
    while(desimal != 0):
        bagi = desimal % 8
        print(f"{desimal} : 8 = {desimal//8} sisa {bagi}")
        desimal = desimal // 8
        hasil.append(bagi)

    hasil.reverse()
    print(f"desimal ke oktal dari {okt} = {hasil}")

#=============DECIMAL TO HEXADECIMAL=====================

def hexa(desimal):
    hex=desimal
    hasil=[]
    while(desimal != 0):
        bagi = desimal % 16
        def konversi(bagi):
            if (bagi == 10):
                return "A"
            elif (bagi == 11):
                return "B"
            elif (bagi == 12):
                return "C"
            elif (bagi == 13):
                return "D"
            elif (bagi == 14):
                return "E"
            elif (bagi == 15):
                return "F"
            else:
                return bagi
        print(f"{desimal} : 16 = {desimal//16} sisa {bagi} atau {str(konversi(bagi))}")
        desimal = desimal // 16
        hasil.append(konversi(bagi))

    hasil.reverse()
    print(f"desimal ke hexa dari {hex} = {hasil}")


#=========SHIT START ON MAIN=============================
    
if __name__ == '__main__':
    desimal = int(input("masukkan angka desimal: "))
    print("="*20, end= "\n")
    
    print("BINARY\n")
    biner(desimal)
    print("="*20)

    print("OCTAL\n")
    oktal(desimal)
    print("="*20)

    print("HEXADECIMAL\n")
    hexa(desimal)
    print("="*20)

    
    
#anyways, if u guys can make in some simpler way. i would love to know it!
