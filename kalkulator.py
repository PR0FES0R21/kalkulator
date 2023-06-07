import os
import sys
import time

x = True

def mengetik(z):
    for i in z + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.00100)


def go():
    global x
    os.system('clear') if x == True else ''

    landing = ''' \033[92m
 _            _  _            _         _                
| |          | || |          | |       | |               
| | __  __ _ | || | __ _   _ | |  __ _ | |_   ___   _ __ 
| |/ / / _` || || |/ /| | | || | / _` || __| / _ \ | '__|
|   < | (|  || ||   < | |_| || || (_| || | |  (_) || |   
|_|\_\ \__,_||_||_|\_\ \__,_||_| \__,_| \__| \___/ |_|
---------------------------------------------------------
            \033[93m by.sayoga pratama \033[92m| \033[91m profesor21
\033[92m=========================================================
    '''
    print(landing) if x == True else ''
    mengetik("\033[96mgunakan (+) untuk penjumlahan (*) untuk perkalian") if x == True else ''
    mengetik("(-) untuk pengurangan, dan (/) untuk penjumlahan") if x == True else ''
    print('          \033[91m\033[1mexample: 2+1 or 2*1 or 2/1 or 2-1\033[0m' ) if x == True else ''

    print("")
    inputan = input("\033[97msilahkan masukan angka: ")

    if "+" in inputan:
        process = inputan.split('+')
        result = int(process[0]) + int(process[1])
        print(f"hasil penjumlahan {process[0]} + {process[1]} = \033[92m{result}\033[0;m")
        next = input("Tekan Y/Enter untuk mengulang program ini ")
        if next == "y":
            x = False
            go()
        else:
            x = False
            go()
    elif "*" in inputan:
        process = inputan.split('*')
        result = int(process[0]) * int(process[1])
        print(f"hasil perkalian {process[0]} * {process[1]} = \033[92m{result}\033[0;m")
        next = input("Tekan Y/Enter untuk mengulang program ini ")
        if next == "y":
            x = False
            go()
        else:
            x = False
            go()
    elif "-" in inputan:
        process = inputan.split('-')
        result = int(process[0]) - int(process[1])
        print(f"hasil pengurangan {process[0]} - {process[1]} = \033[92m{result}\033[0;m")
        next = input("Tekan Y/Enter untuk mengulang program ini ")
        if next == "y":
            x = False
            go()
            
        else:
            x = False
            go()
    elif "/" in inputan:
        process = inputan.split('/')
        result = int(process[0]) / int(process[1])
        print(f"hasil pembagian {process[0]} / {process[1]} = \033[92m{result}\033[0;m")
        next = input("Tekan Y/Enter untuk mengulang program ini ")
        if next == "y":
            x = False
            go()
        else:
            x = False
            go()
    else:
        print("tidak di ketahui")
        next = input("apakah anda ingin mengulan program ini? tekan Enter ")
        if next == "y":
            x = False
            go()
        else:
            x = False
            go()
if __name__ == "__main__":
        go()