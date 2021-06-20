def to_hex(dec):
 igits = "0123456789ABCDEF"
 digits = list(igits)
 x = (dec % 16)
 rest = dec // 16
 if (rest == 0):
    return digits[x]
 return print(to_hex(rest) + digits[x])


def hex_color(a,b,c):
    if a < 0 or b < 0 or c < 0:
        print("Your number can`t be negative")
    elif a > 255 or b > 255 or c > 255:
        print("Your number can`t be greater than 255 ")
    else:
       print("#"),
       print(to_hex(a)),
       print(to_hex(b)),
       print(to_hex(c))
       return print("Color")



hex_color(22,799,41)
hex_color(-12,25,41)
hex_color(31,25,41)












