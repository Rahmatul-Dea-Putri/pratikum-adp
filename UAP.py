import time
import os
import threading
import pygame
from termcolor import colored, cprint
from plyer import notification

os.system('cls')

POMODORO_DURATION = 10 * 1  

histori_sesi = {
    "total_sesi": 0,
    "durasi_total": 0
    }

def pomodoro_file() :
    with open("pomodoro.txt", "w") as file:
        for key, value in histori_sesi.items():
            file.write(f"{key}: {value}\n")

def kirim_notif(judul, pesan) :
    notification.notify(title = judul, message = pesan, timeout = 10)
    print(colored(f"HALLOWW🫲 {judul} - {pesan}","yellow"))

def hitung_mundur(detik) :
    while detik:
        menit, sisa_detik = divmod(detik, 60)
        timer = f"{menit:02d}:{sisa_detik:02d}"
        print(colored(f"\r⏳ [Waktu]: {timer}","cyan"),end="")
        time.sleep(1)
        detik -= 1
    print()

def putar_suara() :
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()

def animasi_istirahat(durasi_menit = 1 ) :
    total_detik = durasi_menit * 60
    ikon_nyantai = ["😴", "🛌", "☕", "🌙", "🧘"]  
    pesan_motivasi = [
        ["Tarik napas", "Fokus kembali", "Tenang"],
        ["Santai", "Nikmati waktu", "Hirup udara"]
    ]  
    for sisa in range(total_detik, -1, -1):
        menit, detik = divmod(sisa, 60)
        waktu_format = f"{menit:02d}:{detik:02d}"
        progres = int(((total_detik - sisa) / total_detik) * 30)
        bar = "[" + "■" * progres + "-" * (30 - progres) + "]" 

        os.system('cls')

        motivasi = ""
        if sisa % 2 == 0:
            motivasi = pesan_motivasi[0][sisa % 3]
        else:
            motivasi = pesan_motivasi[1][sisa % 3]
        
        if sisa == total_detik or sisa == total_detik - 1 or sisa == total_detik - 2 or sisa == total_detik - 3 or sisa == total_detik - 4:
            threading.Thread(target=putar_suara).start()

        elif sisa in [4, 3, 2, 1, 0]:
            threading.Thread(target=putar_suara).start()

        os.system('cls')

        cprint("\n" + "="*50,"white","on_magenta")
        cprint(f"{motivasi.center(50)}","cyan","on_white")
        cprint(f"{ikon_nyantai[sisa % len(ikon_nyantai)].center(49)}","light_red","on_white")
        cprint(f"{waktu_format.center(50)}","green","on_white")
        cprint(f"{bar.center(50)}","yellow","on_white")
        cprint("="*50,"white","on_magenta")
        time.sleep(1)

    os.system('cls')

    print(colored("\n" + "="*50,"magenta"))
    print(colored(f"{'✅ WAKTU ISTIRAHAT TELAH SELESAI! ✅'.center(50)}","light_green"))
    print(colored(f"{'FOKUS LAGI GUYS 🎯'.center(50)}","yellow"))
    print(colored("="*50,"magenta"))
    time.sleep(3)

def animasi_istirahat_panjang(durasi_menit = 3 ) :
    total_detik = durasi_menit * 60
    ikon_jam = ["🕛", "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚"]
    
    for sisa in range(total_detik, -1, -1):
        menit, detik = divmod(sisa, 60)
        format_waktu = f"{menit:02d}:{detik:02d}"
        progres = int(((total_detik - sisa) / total_detik) * 30)
        bar = "[" + "■" * progres + "-" * (30 - progres) + "]"
        
        if sisa == total_detik or sisa == total_detik - 1 or sisa == total_detik - 2 or sisa == total_detik - 3 or sisa == total_detik - 4:
            threading.Thread(target = putar_suara).start()

        elif sisa in [4, 3, 2, 1, 0]:
            threading.Thread(target = putar_suara).start()

        os.system('cls')
        cprint("\n" + "="*50,"white","on_magenta")
        cprint(f"{'WAKTU ISTIRAHAT PANJANG'.center(50)}","cyan","on_white")
        cprint(f"{ikon_jam[sisa % len(ikon_jam)].center(49)}","light_red","on_white")
        cprint(f"{format_waktu.center(50)}","green","on_white")
        cprint(f"{bar.center(50)}","yellow","on_white")
        cprint("="*50,"white","on_magenta")
        time.sleep(1)

    os.system('cls')
    print(colored("\n" + "="*50,"magenta"))
    print(colored(f"{'✅ WAKTU ISTIRAHAT TELAH SELESAI ✅'.center(50)}","light_green"))
    print(colored(f"{'FOKUS GUYSS 🎯'.center(50)}","yellow"))
    print(colored("="*50,"magenta"))
    time.sleep(3)


def pomodoro_sesi():
    sesi = 0
    while True:
        sesi += 1
        print(colored(f"\n🍅 Pomodoro section {sesi} dimulai!","green"))
        kirim_notif("FOKUS", f"Pomodoro ke-{sesi} dimulai!")
        hitung_mundur(POMODORO_DURATION)
        
        histori_sesi["durasi_total"] += POMODORO_DURATION

        if sesi % 4 == 0:
            print(colored("\n🌴 LONG BREAK","blue"))
            kirim_notif("Istirahat Panjang", "Saatnya istirahat panjang!")
            animasi_istirahat_panjang()

        else:
            print(colored("\n🛋️ SHORT BREAK","blue"))
            kirim_notif("Istirahat", "Istirahat pendek dimulai!")
            animasi_istirahat()
        
        berikutnya = input(colored("\n➡️  Lanjut ato ngga nih??? (iya dong/udah dulu deh): ","white")).lower()
        if berikutnya != 'iya dong':
            print(colored("\n🎓 GOOD JOB,KAMU TELAH BEKERJA KERAS,SAMPAI JUMPA DI LAIN WAKTU 🎓","yellow"))
            pomodoro_file()
            break
        os.system('cls')

if __name__ == "__main__":
    print(colored("=== 🎯 WELCOME TO POMODORO TIMER YOUROBUNNN ✨ ===","magenta"))
    nama = input("Kenalan yuk bestie,ketik dong namanya: ")  
    print(colored(f"ANNYEONG 🫲 {nama}, are u ready {nama}? Coba deh,tekan enter nya ...","light_blue"))
    input()
    pomodoro_sesi()

  