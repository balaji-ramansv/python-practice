def rgb(r, g, b):
    rgb = ""
    for i in [r, g, b]:
        if i > 255:
            i = 255
        elif i < 0:
            i = 0
        temp = str(hex(i)).replace('0x','')
        if len(temp) == 1:
            temp = f"0{temp}"
        rgb += temp.upper()
    return rgb

print(rgb(-20,275,125))