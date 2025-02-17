import pygame
import sys

# Inizializza Pygame
pygame.init()

# Imposta la finestra a schermo intero
schermo = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Riempi lo schermo con il colore nero (RGB: 0, 0, 0)
schermo.fill((0, 0, 0))
pygame.display.flip()

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
