import time
from datetime import datetime, timedelta
import threading

class Horloge:
    def __init__(self):
        """
        Initialise l'horloge avec l'heure actuelle, sans alarme, en mode 24 heures, et sans pause.
        """
        self.heure_actuelle = datetime.now()  # Initialisation de l'heure actuelle
        self.alarme = None  # L'alarme est définie sur None au départ
        self.mode_12h = False  # Par défaut, le mode est 24 heures
        self.en_pause = False  # L'horloge n'est pas en pause au départ
        self.en_cours = False  # L'horloge n'est pas en cours d'exécution au départ

    def afficher_heure(self):
        """
        Affiche en continu l'heure actuelle, se mettant à jour chaque seconde.
        Si une alarme est réglée, elle notifie l'utilisateur lorsque l'heure de l'alarme est atteinte.
        """
        self.en_cours = True  # Le programme est maintenant en cours
        self.message_pause_affiche = False  # Le message de pause n'a pas encore été affiché
        while self.en_cours:
            if not self.en_pause:  # Si l'horloge n'est pas en pause
                # Formater l'heure selon le mode 12 heures ou 24 heures
                heure_affichee = self.heure_actuelle.strftime("%I:%M:%S %p" if self.mode_12h else "%H:%M:%S")
                print(heure_affichee, end="\r")  # Afficher l'heure sur la même ligne

                # Vérifier si l'heure actuelle correspond à l'heure de l'alarme
                if self.alarme and self.heure_actuelle.strftime("%H:%M:%S") == self.alarme.strftime("%H:%M:%S"):
                    print("\nALARME ! C'est l'heure !")  # Alerter l'utilisateur lorsque l'alarme sonne
                    self.alarme = None  # Désactiver l'alarme après qu'elle ait sonné

                # Incrémenter l'heure de une seconde
                self.heure_actuelle += timedelta(seconds=1)
                self.message_pause_affiche = False  # Réinitialiser le message de pause
            else:
                # Si l'horloge est en pause, afficher un message
                if not self.message_pause_affiche:
                    print(f"Horloge en pause - {self.heure_actuelle.strftime('%H:%M:%S')}", end="\r")
                    self.message_pause_affiche = True  # Empêcher l'affichage répétitif du message de pause

            time.sleep(1)  # Attendre 1 seconde avant de rafraîchir l'heure

    def regler_heure_depuis_tuple(self, tuple_heure):
        """
        Définit l'heure à partir d'un tuple (heures, minutes, secondes).
        Cela convertira le tuple en un objet datetime.
        """
        h, m, s = tuple_heure  # Décomposer le tuple en heures, minutes et secondes
        self.heure_actuelle = self.heure_actuelle.replace(hour=h, minute=m, second=s)  # Régler l'heure
        print(f"Temps réglé avec succès à {h:02d}:{m:02d}:{s:02d}")  # Afficher l'heure mise à jour

    def regler_alarme(self, tuple_alarme):
        """
        Définit une alarme pour une heure spécifique à partir d'un tuple (heures, minutes, secondes).
        """
        h, m, s = tuple_alarme  # Décomposer le tuple pour régler l'heure de l'alarme
        self.alarme = self.heure_actuelle.replace(hour=h, minute=m, second=s)  # Régler l'alarme
        print(f"Alarme réglée à {h:02d}:{m:02d}:{s:02d}")  # Afficher l'heure de l'alarme

    def basculer_mode(self):
        """
        Change le mode d'affichage de l'horloge entre 12 heures et 24 heures.
        """
        self.mode_12h = not self.mode_12h  # Passer entre le mode 12 heures et 24 heures
        mode = "12 heures" if self.mode_12h else "24 heures"  # Déterminer le mode actuel
        print(f"Mode changé en {mode}")  # Afficher le mode sélectionné

    def basculer_pause(self):
        """
        Change l'état de l'horloge entre pause et fonctionnement.
        """
        self.en_pause = not self.en_pause  # Passer entre pause et fonctionnement
        etat = "en pause" if self.en_pause else "en fonctionnement"  # Afficher l'état actuel
        print(f"L'horloge est maintenant {etat}")  # Afficher l'état de l'horloge

    def arreter_horloge(self):
        """
        Arrête l'horloge.
        """
        self.en_cours = False  # Arrêter l'horloge

def executer_horloge(horloge):
    """
    Démarre l'horloge dans une boucle continue. L'utilisateur peut appuyer sur Ctrl+C pour revenir au menu.
    """
    print("Appuyez sur Ctrl+C pour revenir au menu")  # Informer l'utilisateur de la méthode pour quitter
    try:
        if not horloge.en_cours:
            # Démarrer un fil d'exécution pour faire fonctionner l'horloge en arrière-plan
            thread_affichage = threading.Thread(target=horloge.afficher_heure)
            thread_affichage.daemon = True  # Démoniser le fil pour qu'il s'arrête lorsque le programme quitte
            thread_affichage.start()

        while True:  # Boucle principale pour maintenir le programme en cours
            time.sleep(1)
    except KeyboardInterrupt:  # Si l'utilisateur appuie sur Ctrl+C
        horloge.arreter_horloge()  # Arrêter l'horloge
        print("\nRetour au menu")  # Informer l'utilisateur que le menu est à nouveau affiché

def menu():
    """
    Affiche le menu principal du programme d'horloge, permettant à l'utilisateur de choisir différentes options.
    """
    horloge = Horloge()  # Créer une instance de l'horloge

    while True:  # Afficher le menu dans une boucle
        print("\n=== MENU ===")
        print("1. Afficher l'heure actuelle en temps réel")
        print("2. Régler l'heure")
        print("3. Régler une alarme")
        print("4. Changer le mode d'affichage (12 heures/24 heures)")
        print("5. Mettre en pause/Reprendre l'horloge")
        print("6. Quitter")

        choix = input("\nVotre choix : ")  # Demander à l'utilisateur de choisir une option

        if choix == "1":
            executer_horloge(horloge)  # Lancer l'horloge en temps réel

        elif choix == "2":
            try:
                # Demander à l'utilisateur de régler une nouvelle heure
                h = int(input("Heures (0-23) : "))
                m = int(input("Minutes (0-59) : "))
                s = int(input("Secondes (0-59) : "))
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:  # Valider l'entrée
                    horloge.regler_heure_depuis_tuple((h, m, s))  # Régler l'heure avec le tuple
                    executer_horloge(horloge)  # Lancer l'horloge après avoir réglé l'heure
                else:
                    print("Valeurs invalides.")  # Afficher un message d'erreur si les valeurs sont invalides
            except ValueError:
                print("Entrée invalide.")  # Gérer les erreurs d'entrée invalides

        elif choix == "3":
            try:
                # Demander à l'utilisateur de régler l'heure de l'alarme
                h = int(input("Heures (0-23) : "))
                m = int(input("Minutes (0-59) : "))
                s = int(input("Secondes (0-59) : "))
                if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:  # Valider l'entrée
                    horloge.regler_alarme((h, m, s))  # Régler l'alarme avec le tuple
                    executer_horloge(horloge)  # Lancer l'horloge après avoir réglé l'alarme
                else:
                    print("Valeurs invalides.")  # Afficher un message d'erreur si les valeurs sont invalides
            except ValueError:
                print("Entrée invalide.")  # Gérer les erreurs d'entrée invalides

        elif choix == "4":
            horloge.basculer_mode()  # Changer le mode d'affichage (12 heures ou 24 heures)

        elif choix == "5":
            horloge.basculer_pause()  # Mettre en pause ou reprendre l'horloge

        elif choix == "6":
            print("Au revoir !")  # Afficher un message d'adieu
            break  # Quitter la boucle et terminer le programme

        else:
            print("Choix invalide.")  # Afficher un message d'erreur pour un choix invalide


if __name__ == "__main__":
    menu()  # Démarrer le menu principal lorsque le programme est exécuté
