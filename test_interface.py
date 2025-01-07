import customtkinter as ctk
import time
from datetime import datetime, timedelta
import threading

class HorlogeGUI:
    def __init__(self):
        # Configuration de base de CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configuration principale de la fenêtre
        self.root = ctk.CTk()
        self.root.title("Horloge Élégante")
        self.root.geometry("800x600")

        # Variables de l'horloge
        self.heure_actuelle = datetime.now()
        self.alarme = None
        self.mode_12h = False
        self.pause = False
        self.running = True

        # Création de l'interface
        self.creer_interface()
        
        # Démarrer le thread de l'horloge
        self.thread_horloge = threading.Thread(target=self.actualiser_heure, daemon=True)
        self.thread_horloge.start()

    def creer_interface(self):
        # Frame principale
        self.frame_principale = ctk.CTkFrame(self.root)
        self.frame_principale.pack(pady=20, padx=20, fill="both", expand=True)

        # Affichage de l'heure
        self.label_heure = ctk.CTkLabel(
            self.frame_principale, 
            text="00:00:00",
            font=ctk.CTkFont(size=60, weight="bold")
        )
        self.label_heure.pack(pady=30)

        # Frame pour les boutons
        self.frame_boutons = ctk.CTkFrame(self.frame_principale)
        self.frame_boutons.pack(pady=20)

        # Boutons
        self.btn_regler_heure = ctk.CTkButton(
            self.frame_boutons,
            text="Régler l'heure",
            command=self.fenetre_regler_heure
        )
        self.btn_regler_heure.pack(pady=10)

        self.btn_alarme = ctk.CTkButton(
            self.frame_boutons,
            text="Régler l'alarme",
            command=self.fenetre_regler_alarme
        )
        self.btn_alarme.pack(pady=10)

        self.btn_mode = ctk.CTkButton(
            self.frame_boutons,
            text="Changer mode 12h/24h",
            command=self.changer_mode
        )
        self.btn_mode.pack(pady=10)

        self.btn_pause = ctk.CTkButton(
            self.frame_boutons,
            text="Pause/Reprendre",
            command=self.basculer_pause
        )
        self.btn_pause.pack(pady=10)

        # Status
        self.label_status = ctk.CTkLabel(
            self.frame_principale,
            text="En marche",
            font=ctk.CTkFont(size=14)
        )
        self.label_status.pack(pady=20)

    def fenetre_regler_heure(self):
        dialog = ctk.CTkInputDialog(
            text="Entrez l'heure (format HH:MM:SS):",
            title="Régler l'heure"
        )
        result = dialog.get_input()
        if result:
            try:
                h, m, s = map(int, result.split(':'))
                self.heure_actuelle = self.heure_actuelle.replace(hour=h, minute=m, second=s)
            except:
                self.montrer_erreur("Format invalide! Utilisez HH:MM:SS")

    def fenetre_regler_alarme(self):
        dialog = ctk.CTkInputDialog(
            text="Entrez l'heure de l'alarme (format HH:MM:SS):",
            title="Régler l'alarme"
        )
        result = dialog.get_input()
        if result:
            try:
                h, m, s = map(int, result.split(':'))
                self.alarme = self.heure_actuelle.replace(hour=h, minute=m, second=s)
                self.montrer_info(f"Alarme réglée pour {h:02d}:{m:02d}:{s:02d}")
            except:
                self.montrer_erreur("Format invalide! Utilisez HH:MM:SS")

    def changer_mode(self):
        self.mode_12h = not self.mode_12h
        mode = "12h" if self.mode_12h else "24h"
        self.montrer_info(f"Mode changé en {mode}")

    def basculer_pause(self):
        self.pause = not self.pause
        etat = "en pause" if self.pause else "en marche"
        self.label_status.configure(text=f"Horloge {etat}")

    def actualiser_heure(self):
        while self.running:
            if not self.pause:
                if self.mode_12h:
                    heure_affichee = self.heure_actuelle.strftime("%I:%M:%S %p")
                else:
                    heure_affichee = self.heure_actuelle.strftime("%H:%M:%S")
                
                self.label_heure.configure(text=heure_affichee)
                
                if self.alarme and self.heure_actuelle.strftime("%H:%M:%S") == self.alarme.strftime("%H:%M:%S"):
                    self.montrer_alarme()
                
                self.heure_actuelle += timedelta(seconds=1)
            time.sleep(1)

    def montrer_erreur(self, message):
        dialog = ctk.CTkInputDialog(title="Erreur", text=message)
        dialog.destroy()

    def montrer_info(self, message):
        dialog = ctk.CTkInputDialog(title="Information", text=message)
        dialog.destroy()

    def montrer_alarme(self):
        dialog = ctk.CTkInputDialog(title="ALARME!", text="DRING DRING ! C'est l'heure !")
        dialog.destroy()

    def demarrer(self):
        self.root.mainloop()

    def arreter(self):
        self.running = False
        self.root.quit()

if __name__ == "__main__":
    app = HorlogeGUI()
    try:
        app.demarrer()
    except KeyboardInterrupt:
        app.arreter()