import time
from viewmodel.timerViewmodel import set_pomodoro, confirm_timer_setup, start_timer
import utils.helper as helper

def display_timer_setup(username):
    helper.clear()
    print("Tentukan waktu timer")
    
    while True:
        try:
            while True:
                jam = int(input("Jam: "))
                menit = int(input("Menit (Minimal 10 menit): "))
                if not (jam == 0) and (menit < 10):
                    break
            
            jam += menit // 60
            menit = menit % 60
            break
        except ValueError:
            print("Input anda tidak valid! Silahkan coba lagi.\n")
            time.sleep(1)

    
    while True:
        pomodoro_input = input("Gunakan pomodoro timer (setiap 25 menit istirahat 5 menit)? [Y/n] ").strip().lower()
        if pomodoro_input in ['y', 'n']:
            break
        else:
            print("Input invalid! Harap masukkan 'Y' untuk ya atau 'n' untuk tidak.")
            time.sleep(1)
    
    pomodoro = set_pomodoro(pomodoro_input)

    if confirm_timer_setup(jam, menit, pomodoro):
        start_timer(jam, menit, pomodoro, username)
