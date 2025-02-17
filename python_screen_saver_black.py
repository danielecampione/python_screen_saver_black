import pygame
import sys

# Inizializza Pygame
pygame.init()

# Imposta la finestra a schermo intero
schermo = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Nasconde il puntatore del mouse
pygame.mouse.set_visible(False)

# Riempi lo schermo con il colore nero (RGB: 0, 0, 0)
schermo.fill((0, 0, 0))
pygame.display.flip()

# Posizione iniziale del puntatore
posizione_iniziale = pygame.mouse.get_pos()

# Loop principale
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    # Ottieni la posizione attuale del puntatore del mouse
    posizione_attuale = pygame.mouse.get_pos()
    
    # Calcola lo spostamento del puntatore
    spostamento = ((posizione_attuale[0] - posizione_iniziale[0]) ** 2 + (posizione_attuale[1] - posizione_iniziale[1]) ** 2) ** 0.5
    
    # Se lo spostamento è superiore a 5 pixel, chiudi l'applicazione
    if spostamento > 5:
        pygame.quit()
        sys.exit()
