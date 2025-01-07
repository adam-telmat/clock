import time
from datetime import datetime, timedelta
import threading

class Horloge:
    def __init__(self):
        self.heure_actuelle = datetime.now()
        self.alarme = None
        self.mode_12h = False
        self.pause = False
        self.is_running = False

    def afficher_heure(self):
        self.is_running = True
        self.pause_message_shown = False
        while self.is_running:
            if not self.pause:
                heure_affichee = self.heure_actuelle.strftime("%I:%M:%S %p" if self.mode_12h else "%H:%M:%S")
                print(heure_affichee, end="\r")
                
                if self.alarme and self.heure_actuelle.strftime("%H:%M:%S") == self.alarme.strftime("%H:%M:%S"):
                    print("\nDRING DRING ! C'est l'heure de l'alarme !")
                    self.alarme = None  # Désactive l'alarme après qu'elle a sonné
                
                self.heure_actuelle += timedelta(seconds=1)
                self.pause_message_shown = False
            else:
                if not self.pause_message_shown:
                    print(f"Horloge en pause - {self.heure_actuelle.strftime('%H:%M:%S')}", end="\r")
                    self.pause_message_shown = True
            
            time.sleep(1)

    def regler_alarme(self, h, m, s):
        self.alarme = self.heure_actuelle.replace(hour=h, minute=m, second=s)
        print(f"Alarme réglée pour {h:02d}:{m:02d}:{s:02d}")

    def changer_mode(self):
        self.mode_12h = not self.mode_12h
        mode = "12h" if self.mode_12h else "24h"
        print(f"Mode changé en {mode}")

    def basculer_pause(self):
        self.pause = not self.pause
        etat = "en pause" if self.pause else "en marche"
        print(f"Horloge {etat}")

    def arreter_heure(self):
        self.is_running = False


def lancer_horloge(horloge):
    """
    Permet de lancer l'horloge en continu après avoir réglé l'heure ou l'alarme.
    L'utilisateur reste ici jusqu'à ce qu'il décide de revenir au menu principal.
    """
    print("Appuyez sur Ctrl+C pour revenir au menu")
    try:
        if not horloge.is_running:
            thread_affichage = threading.Thread(target=horloge.afficher_heure)
            thread_affichage.daemon = True
            thread_affichage.start()
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        horloge.arreter_heure()
        print("\nRetour au menu")


def menu():
    horloge = Horloge()

    while True:
        print("\n=== MENU ===")
        print("1. Afficher l'heure en temps réel")
        print("2. Régler l'heure")
        print("3. Régler l'alarme")
        print("4. Changer le mode d'affichage (12h/24h)")
        print("5. Mettre en pause/reprendre")
        print("6. Quitter")
        
        choix = input("\nVotre choix : ")
        
        if choix == "1":
            lancer_horloge(horloge)

        elif choix == "2":
            try:
                h = int(input("Heures (0-23) : "))
                m = int(input("Minutes (0-59) : "))
                s = int(input("Secondes (0-59) : "))
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                    horloge.heure_actuelle = horloge.heure_actuelle.replace(hour=h, minute=m, second=s)
                    print("Heure réglée avec succès.")
                    lancer_horloge(horloge)
                else:
                    print("Valeurs invalides.")
            except ValueError:
                print("Entrée invalide.")

        elif choix == "3":
            try:
                h = int(input("Heures (0-23) : "))
                m = int(input("Minutes (0-59) : "))
                s = int(input("Secondes (0-59) : "))
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                    horloge.regler_alarme(h, m, s)
                    lancer_horloge(horloge)  # Permet de rester dans l'affichage après l'alarme
                else:
                    print("Valeurs invalides.")
            except ValueError:
                print("Entrée invalide.")

        elif choix == "4":
            horloge.changer_mode()

        elif choix == "5":
            horloge.basculer_pause()

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Choix invalide")


if __name__ == "__main__":
    menu()

