import os #import library os untuk berkomunikasi dengan system
import pandas as pd #import library pandas menjadi pd
import numpy as np #import library numpy menjadi np

def clear ():
    os.system ("cls")

def nilai_random():
    np.random.seed(0)
    nilai_mhs = list(np.random.randint(70,91,size = 10))
    return nilai_mhs

def status():
    nilai_mhs = nilai_random()
    status_mhs = []
    for i in range (len(nilai_mhs)) :
        if nilai_mhs[i] >= 75 :
            status = "sangat memuaskan"
        else :
            status = "cukup"
        status_mhs.append(status)
    return status_mhs

def random_nim():
    global nim_mhs
    nim_mhs = []
    for i in range (10) :
        nim = f"24241010200{i}"
        nim_mhs.append(nim)
    return nim_mhs

def cetak ():
    clear()
    penampung = {
    "NIM" : random_nim(),
    "NILAI" : nilai_random(),
    "STATUS" : status(),
    }
    df = pd.DataFrame(penampung)
    df = df.sort_values(by = "NILAI", ascending=False)
    df.index = range(1,len(df) + 1)
    print (df)

cetak()