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

    def afficher_heure(self, h=None, m=None, s=None):
        if h is not None and m is not None and s is not None:
            self.heure_actuelle = self.heure_actuelle.replace(hour=h, minute=m, second=s)

        self.is_running = True  # L'horloge commence à tourner
        while self.is_running:
            if not self.pause:
                if self.mode_12h:
                    heure_affichee = self.heure_actuelle.strftime("%I:%M:%S %p")
                else:
                    heure_affichee = self.heure_actuelle.strftime("%H:%M:%S")
                
                print(heure_affichee, end="\r")
                
                if self.alarme and self.heure_actuelle.strftime("%H:%M:%S") == self.alarme.strftime("%H:%M:%S"):
                    print("\nDRING DRING ! C'est l'heure de l'alarme !")
                
                self.heure_actuelle += timedelta(seconds=1)
            else:
                print(f"Horloge en pause - {self.heure_actuelle.strftime('%H:%M:%S')}", end="\r")
            
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
        self.is_running = False  # L'horloge s'arrête


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
            print("Appuyez sur Ctrl+C pour revenir au menu")
            try:
                # Lancer l'affichage de l'heure dans un thread
                thread_affichage = threading.Thread(target=horloge.afficher_heure)
                thread_affichage.daemon = True  # Cela permet de fermer le thread à la fin du programme
                thread_affichage.start()
                
                # Attendre que l'utilisateur appuie sur Ctrl+C pour interrompre
                while True:
                    time.sleep(1)  # Boucle pour garder le menu actif tout en affichant l'heure
            except KeyboardInterrupt:
                horloge.arreter_heure()  # Arrêter l'horloge à la sortie
                print("\nRetour au menu")
                
        elif choix == "2":
            try:
                h = int(input("Heures (0-23) : "))
                m = int(input("Minutes (0-59) : "))
                s = int(input("Secondes (0-59) : "))
                horloge.afficher_heure(h, m, s)
            except ValueError:
                print("Entrée invalide")
                
        elif choix == "3":
            try:
                h = int(input("Heures (0-23) : "))
                m = int(input("Minutes (0-59) : "))
                s = int(input("Secondes (0-59) : "))
                horloge.regler_alarme(h, m, s)
            except ValueError:
                print("Entrée invalide")
                
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
