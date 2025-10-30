#!/usr/bin/env python3
# BankOfAmerica.py
# Created by BUSTED MARKET
# Pure Troll
# Usage: python3 aaa.py

import os
import sys
import time
import getpass
import platform

def set_console_title(title: str):
    """Définit le titre de la console (Windows et *nix)."""
    system = platform.system().lower()
    try:
        if 'windows' in system:
            os.system(f"title {title}")
        else:
            # AHHHH
            sys.stdout.write(f"\x1b]0;{title}\x07")
            sys.stdout.flush()
    except Exception:
        pass

def fake_processing(duration=3):
    """Progess BAR."""
    for i in range(duration * 4):
        pct = int((i + 1) / (duration * 4) * 100)
        bar = '#' * (pct // 5) + '-' * (20 - (pct // 5))
        sys.stdout.write(f"\rProcessing: [{bar}] {pct}%")
        sys.stdout.flush()
        time.sleep(0.25)
    print()

def main():
    # The Victim think he do virement
    set_console_title("Bank Of America")

    print("=" * 40)
    print("Bank Of America")
    print("No Refundable if you missed or added a number that you dont want , we cant do nothing.")
    print("=" * 40)
    print()

    # We saying to do all informations and write
    email = input("Enter email: ")
    pwd = input("Enter password: ")   # demandé de façon plus réaliste mais ne sera pas stocké
    recipient = input("Type the RIB That you want give ? ")
    amount = input("Amount (ex: 50.00): ")

    print()
    print("Confirming details...")
    # all informations for the scammers see the details
    print(f"Email: {email}")
    print(f"Recipient: {recipient}")
    print(f"Amount: {amount}")
    print(f"Password: {pwd}")


    # Faux traitement
    fake_processing(duration=4)

    # Fake RESULTATS OF SUCCESS AND FAILED But this not working
    import random
    if random.random() < 0.75:
        print("\nTRANSFER SUCCESSFUL ✓")
        print("Transaction ID: Support-" + str(random.randint(100000, 999999)))
    else:
        print("\nTRANSFER SUCESS ✗")

    print("\n" + "*" * 40)
    print("All your informations are not leaked")
    print("Bank Of America @ Copyright 2025. Press Enter to exit.")
    print("*" * 40)

    input()  # pause finale

if __name__ == "__main__":
    main()

