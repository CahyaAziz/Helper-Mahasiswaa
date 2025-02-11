import re
import getpass
import time
import utils.helper as helper
import sys
from viewmodel.loginViewmodel import register_user, authenticate_user

def display_main_menu():
    while True:
        helper.clear()
        print("========================================")
        print("| No |    Masuk Ke Helper Mahasiswa    |")
        print("========================================")
        print("| 1  | Login                           |")
        print("| 2  | Register                        |")
        print("| 0  | Keluar                          |")
        print("========================================")

        choice = input("Pilih dengan angka: ")
        if choice == '1':
            helper.clear()
            username = helper.validate_nospace("Masukkan username: ")
            while True:
                password = getpass.getpass("Masukkan password: ")
                if not password.strip():
                        print("Input tidak boleh kosong! Coba lagi.")
                        time.sleep(1)
                        helper.clear()
                else:
                    break
            if authenticate_user(username, password):
                print(f"\nLogin berhasil. Welcome, {username}!")
                time.sleep(1)
                return username
            else:
                print("\nUsername atau Password salah. Silahkan coba lagi.")
                time.sleep(1)
        elif choice == '2':
            helper.clear()
            while True:
                username = helper.validate_nospace("Masukkan username: ")
                if len(username) < 3 or len(username) > 20:
                    print("Username harus memiliki minimal 3-20 karakter. Coba lagi.")
                    time.sleep(1)
                    helper.clear()
                else:
                    break
            while True:
                password = getpass.getpass("Masukkan password baru: ")
                if len(password) < 6:
                    print("Password harus memiliki minimal 6 karakter. Coba lagi.")
                    time.sleep(1)
                    helper.clear()
                elif not password.strip():
                    print("Input tidak boleh kosong! Coba lagi.")
                    time.sleep(1)
                    helper.clear()
                elif not re.match("^[a-zA-Z0-9!@#$%^&*_ ]+$", password):
                    print("Input tidak valid! Password hanya boleh berisi huruf, angka, dan simbol khusus (!@#$%^&*_)")
                    time.sleep(1)
                    helper.clear()
                else:
                    break
            if register_user(username, password):
                print("Berhasil Register.")
                time.sleep(1)
            else:
                print("\nUsername sudah ada! Silakan coba login kembali.")
                time.sleep(1)
        elif choice == '0':
            sys.exit()
        else:
            print("\nInput tidak valid! Silakan coba lagi.")
            time.sleep(1)
