import time
import pygame
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime, timedelta

pygame.init()
window = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Reloj Digital")

font = pygame.font.Font(None, 74)
color = (255, 255, 255)
bg_color = (0, 0, 0)

def display_hour(hour_tuple):
    """Función para ajustar la hora manualmente ingresada por el usuario."""
    return datetime.now().replace(hour=hour_tuple[0], minute=hour_tuple[1], second=hour_tuple[2], microsecond=0)

def ask_new_time():
    """Función para solicitar la nueva hora al usuario a través de una ventana emergente."""
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de tkinter
    new_hour = simpledialog.askinteger("Input", "Nueva Hora (HH):", minvalue=0, maxvalue=23)
    new_minute = simpledialog.askinteger("Input", "Nuevos Minutos (MM):", minvalue=0, maxvalue=59)
    new_second = simpledialog.askinteger("Input", "Nuevos Segundos (SS):", minvalue=0, maxvalue=59)
    root.destroy()  # Cerrar la ventana principal de tkinter
    return (new_hour, new_minute, new_second)

running = True
current_time = datetime.now()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Abrir la ventana emergente para solicitar la nueva hora
                manual_time = ask_new_time()
                current_time = display_hour(manual_time)
    
    current_time += timedelta(seconds=1)
    formatted_time = current_time.strftime('%H:%M:%S')
    
    window.fill(bg_color)
    text = font.render(formatted_time, True, color)
    window.blit(text, (50, 50))
    
    pygame.display.flip()
    time.sleep(1)

pygame.quit()
