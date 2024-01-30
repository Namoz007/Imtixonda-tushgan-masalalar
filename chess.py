
chess_dct_a = {
        'A1' : 'false',
        'A2' : 'false',
        'A3' : 'false',
        'A4' : 'false',
        'A5' : 'false',
        'A6' : 'false',
        'A7' : 'false',
        'A8' : 'false'
    }

chess_dct_b = {
        'B1' : 'false',
        'B2' : 'false',
        'B3' : 'false',
        'B4' : 'false',
        'B5' : 'false',
        'B6' : 'false',
        'B7' : 'false',
        'B8' : 'false'
    }
chess_dct_c = {
        'C1' : 'false',
        'C2' : 'false',
        'C3' : 'false',
        'C4' : 'false',
        'C5' : 'false',
        'C6' : 'false',
        'C7' : 'false',
        'C8' : 'false'
    }

chess_dct_d = {
        'D1' : 'false',
        'D2' : 'false',
        'D3' : 'false',
        'D4' : 'false',
        'D5' : 'false',
        'D6' : 'false',
        'D7' : 'false',
        'D8' : 'false'
    }

chess_dct_e = {
        'E1' : 'false',
        'E2' : 'false',
        'E3' : 'false',
        'E4' : 'false',
        'E5' : 'false',
        'E6' : 'false',
        'E7' : 'false',
        'E8' : 'false'
    }

chess_dct_f = {
        'F1' : 'false',
        'F2' : 'false',
        'F3' : 'false',
        'F4' : 'false',
        'F5' : 'false',
        'F6' : 'false',
        'F7' : 'false',
        'F8' : 'false'
    }

chess_dct_g = {
        'G1' : 'false',
        'G2' : 'false',
        'G3' : 'false',
        'G4' : 'false',
        'G5' : 'false',
        'G6' : 'false',
        'G7' : 'false',
        'G8' : 'false'
    }

chess_dct_h = {
        'H1' : 'false',
        'H2' : 'false',
        'H3' : 'false',
        'H4' : 'false',
        'H5' : 'false',
        'H6' : 'false',
        'H7' : 'false',
        'H8' : 'false' 
    }

enter_you = input("Otning kordinatasi: Masalan: A1 ")
kordinat = enter_you[0];count = 0;ot = '';piyoda = ''
if len(enter_you) == 2 and enter_you[1].isdigit() and int(enter_you[1]) <= 8:
    if kordinat.upper() == 'A':
        chess_dct_a.update({f"{enter_you.upper()}" : 'OT'})
        for i in chess_dct_a:
            if chess_dct_a[i] == 'OT':
                ot = i
        count += 1
    elif kordinat.upper() == 'B':
        chess_dct_b.update({f"{enter_you.upper()}" : 'OT'})
        for i in chess_dct_b:
            if chess_dct_b[i] == 'OT':
                ot = i
        count += 1
    elif kordinat.upper() == 'C':
        chess_dct_c.update({f"{enter_you.upper()}" : 'OT'})
        for i in chess_dct_c:
            if chess_dct_c[i] == 'OT':
                ot = i
        count += 1
    elif kordinat.upper()  == 'D':
        chess_dct_d.update({f"{enter_you.upper()}" : 'OT'})
        for i in chess_dct_d:
            if chess_dct_d[i] == 'OT':
                ot = i
        count += 1
    elif kordinat.upper()  == 'E':
        chess_dct_e.update({f"{enter_you.upper()}" : 'OT'})
        for i in chess_dct_e:
            if chess_dct_e[i] == 'OT':
                ot = i
        count += 1
    elif kordinat.upper()  == 'F':
        chess_dct_f.update({f"{enter_you.upper()}" : 'OT'})
        for i in chess_dct_f:
            if chess_dct_f[i] == 'OT':
                ot = i
        count += 1
    elif kordinat.upper()  == 'G':
        chess_dct_g.update({f"{enter_you.upper()}" : 'OT'})
        for i in chess_dct_g:
            if chess_dct_g[i] == 'OT':
                ot  = i
        count += 1
    elif kordinat.upper()  == 'H':
        chess_dct_h.update({f"{enter_you.upper()}" : 'OT'})
        for i in chess_dct_h:
            if chess_dct_h[i] == 'OT':
                ot = i
        count += 1
    else:
        print("Bunaqa zona mavjud emas.")

else:
    print("Siz no tog'ri malumot kiritdingiz.")

if count != 0: 
    enter_you_ = input("Piyodaning kordinatalari: Masalan A2 ")
    kordinat = enter_you_[0].upper();count = 0
    if len(enter_you) == 2 and enter_you_[1].isdigit() and enter_you_.upper() != enter_you.upper() and int(enter_you_[1]) <= 8:
        if kordinat.upper() == 'A':
            chess_dct_a.update({f"{enter_you_.upper()}" : 'PIYODA'})
            for i in chess_dct_a:
                if chess_dct_a[i] == 'PIYODA':
                    piyoda = i
            count += 1
        elif kordinat.upper() == 'B':
            chess_dct_b.update({f"{enter_you_.upper()}" : 'PIYODA'})
            for i in chess_dct_b:
                if chess_dct_b[i] == "PIYODA":
                    piyoda = i
            count += 1
        elif kordinat.upper() == 'C':
            chess_dct_c.update({f"{enter_you_.upper()}" : 'PIYODA'})
            for i in chess_dct_c:
                if chess_dct_c[i] == 'PIYODA':
                    piyoda = i
            count += 1
        elif kordinat.upper() == 'D':
            chess_dct_d.update({f"{enter_you_.upper()}" : 'PIYODA'})
            for i in chess_dct_d:
                if chess_dct_d[i] == 'PIYODA':
                    piyoda = i
            count += 1
        elif kordinat.upper() == 'E':
            chess_dct_e.update({f"{enter_you_.upper()}" : 'PIYODA'})
            for i in chess_dct_e:
                if chess_dct_e[i] == 'PIYODA':
                    piyoda = i
            count += 1
        elif kordinat.upper() == 'F':
            chess_dct_f.update({f"{enter_you_.upper()}" : 'PIYODA'})
            for i in chess_dct_f:
                if chess_dct_f[i] == 'PIYODA':
                    piyoda = i
            count += 1
        elif kordinat.upper() == 'G':
            chess_dct_g.update({f"{enter_you_.upper()}" : 'PIYODA'})
            for i in chess_dct_g:
                if chess_dct_g[i] == 'PIYODA':
                    piyoda = i
            count += 1
        elif kordinat.upper() == 'H':
            chess_dct_h.update({f"{enter_you_.upper()}" : 'PIYODA'})
            for i in chess_dct_h:
                if chess_dct_h[i] == 'PIYODA':
                    piyoda = i
            count += 1
        else:
            print("Bunaqa zona mavjud emas.")
    else:
        print("Siz no tog'ri malumot kiritdingiz.")
for i in chess_dct_a:
    if chess_dct_a[i] == 'OT':
        ot = i
chess_dct_lst = ['A','B','C','D','E','F','G','H'];count = 0
chess_letter = ot[0]
chess_number = int(ot[1])
chess_ind = chess_dct_lst.index(chess_letter)
if chess_ind == 0:
    ind = chess_ind
    if (chess_number - 3) > 0:
        you = 'B' + f"{(chess_number - 3)}"
        if chess_dct_b[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'B' + f"{(chess_number + 3)}" 
        if chess_dct_b[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number + 1) <= 8:
        you = 'C' + f"{(chess_number + 1)}" 
        if chess_dct_c[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number - 1) > 0:
        you = 'C' + f"{(chess_number - 1)}" 
        if chess_dct_c[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

elif chess_ind == 7:
    if (chess_number - 3) > 0:
        you = 'G' + f"{(chess_number - 3)}"
        if chess_dct_g[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'G' + f"{(chess_number + 3)}" 
        if chess_dct_g[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number + 1) <= 8:
        you = 'F' + f"{(chess_number + 1)}" 
        if chess_dct_f[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'F' + f"{(chess_number - 1)}" 
        if chess_dct_f[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

elif chess_ind == 1:
    if (chess_number - 3) > 0:
        you = 'A' + f"{(chess_number - 3)}"
        if chess_dct_a[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'A' + f"{(chess_number + 3)}" 
        if chess_dct_a[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number + 1) <= 8:
        you = 'D' + f"{(chess_number + 1)}" 
        if chess_dct_d[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'D' + f"{(chess_number - 1)}" 
        if chess_dct_d[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number - 3) > 0:
        you = 'C' + f"{(chess_number - 3)}"
        if chess_dct_c[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'C' + f"{(chess_number + 3)}" 
        if chess_dct_c[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
elif chess_ind == 6:
    if (chess_number - 3) > 0:
        you = 'H' + f"{(chess_number - 3)}"
        if chess_dct_h[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'H' + f"{(chess_number + 3)}" 
        if chess_dct_h[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number + 1) <= 8:
        you = 'E' + f"{(chess_number + 1)}" 
        if chess_dct_e[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'E' + f"{(chess_number - 1)}" 
        if chess_dct_e[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number - 3) > 0:
        you = 'F' + f"{(chess_number - 3)}"
        if chess_dct_f[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'F' + f"{(chess_number + 3)}" 
        if chess_dct_f[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

elif chess_ind == 2:
    if (chess_number - 3) > 0:
        you = 'B' + f"{(chess_number - 3)}"
        if chess_dct_b[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'B' + f"{(chess_number + 3)}" 
        if chess_dct_b[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number + 1) <= 8:
        you = 'A' + f"{(chess_number + 1)}" 
        if chess_dct_a[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'A' + f"{(chess_number - 1)}" 
        if chess_dct_a[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number - 3) > 0:
        you = 'D' + f"{(chess_number - 3)}"
        if chess_dct_d[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'D' + f"{(chess_number + 3)}" 
        if chess_dct_d[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number + 1) <= 8:
        you = 'E' + f"{(chess_number + 1)}" 
        if chess_dct_e[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'E' + f"{(chess_number - 1)}" 
        if chess_dct_e[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

elif chess_ind == 3:
    if (chess_number - 3) > 0:
        you = 'C' + f"{(chess_number - 3)}"
        if chess_dct_c[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'C' + f"{(chess_number + 3)}" 
        if chess_dct_c[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number + 1) <= 8:
        you = 'B' + f"{(chess_number + 1)}" 
        if chess_dct_b[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'B' + f"{(chess_number - 1)}" 
        if chess_dct_b[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number - 3) > 0:
        you = 'E' + f"{(chess_number - 3)}"
        if chess_dct_e[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'E' + f"{(chess_number + 3)}" 
        if chess_dct_e[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number + 1) <= 8:
        you = 'F' + f"{(chess_number + 1)}" 
        if chess_dct_f[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'F' + f"{(chess_number - 1)}" 
        if chess_dct_f[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

elif chess_ind == 4:
    if (chess_number - 3) > 0:
        you = 'D' + f"{(chess_number - 3)}"
        if chess_dct_d[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'D' + f"{(chess_number + 3)}" 
        if chess_dct_d[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number + 1) <= 8:
        you = 'C' + f"{(chess_number + 1)}" 
        if chess_dct_c[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'C' + f"{(chess_number - 1)}" 
        if chess_dct_c[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number - 3) > 0:
        you = 'F' + f"{(chess_number - 3)}"
        if chess_dct_f[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'F' + f"{(chess_number + 3)}" 
        if chess_dct_f[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number + 1) <= 8:
        you = 'G' + f"{(chess_number + 1)}" 
        if chess_dct_g[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'G' + f"{(chess_number - 1)}" 
        if chess_dct_g[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

elif chess_ind == 5:
    if (chess_number - 3) > 0:
        you = 'E' + f"{(chess_number - 3)}"
        if chess_dct_e[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'E' + f"{(chess_number + 3)}" 
        if chess_dct_e[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number + 1) <= 8:
        you = 'D' + f"{(chess_number + 1)}" 
        if chess_dct_d[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'D' + f"{(chess_number - 1)}" 
        if chess_dct_d[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1
    
    if (chess_number - 3) > 0:
        you = 'G' + f"{(chess_number - 3)}"
        if chess_dct_g[you] == 'PIYODA':
            print('Ot piyodani ura oladi.')
            count += 1
    
    if (chess_number + 3) <= 8:
        you = 'G' + f"{(chess_number + 3)}" 
        if chess_dct_g[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number + 1) <= 8:
        you = 'H' + f"{(chess_number + 1)}" 
        if chess_dct_h[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

    if (chess_number - 1) > 0:
        you = 'H' + f"{(chess_number - 1)}" 
        if chess_dct_h[you] == 'PIYODA':
            print("Ot piyodani ura oladi.")
            count += 1

if count == 0:
    print(f"{ot} da turgan ot {piyoda} da turgan piyodani ura olmaydi.")