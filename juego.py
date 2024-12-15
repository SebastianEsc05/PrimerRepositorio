import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Colisión: Detener el Movimiento")

# Colores (por si los necesitas)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Obtener el rectángulo del jugador para moverlo

# Rectángulos de obstáculos
jugador_rect = pygame.Rect(50,50,50, 50)
obstaculo = pygame.Rect(300, 200, 100, 100)  # x, y, ancho, alto
obstaculo2 = pygame.Rect(500, 400, 25, 25)  # x, y, ancho, alto
velocidad = 10

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detectar teclas
    teclas = pygame.key.get_pressed()

    # Movimiento del jugador con detección de colisión
    if teclas[pygame.K_UP]:
        nuevo_rect = jugador_rect.move(0, -velocidad)
        if not nuevo_rect.colliderect(obstaculo) and not nuevo_rect.colliderect(obstaculo2):  # Si no hay colisión con ambos, se mueve
            jugador_rect.y -= velocidad
    if teclas[pygame.K_DOWN]:
        nuevo_rect = jugador_rect.move(0, velocidad)
        if not nuevo_rect.colliderect(obstaculo) and not nuevo_rect.colliderect(obstaculo2):  # Si no hay colisión con ambos, se mueve
            jugador_rect.y += velocidad
    if teclas[pygame.K_LEFT]:
        nuevo_rect = jugador_rect.move(-velocidad, 0)
        if not nuevo_rect.colliderect(obstaculo) and not nuevo_rect.colliderect(obstaculo2):  # Si no hay colisión con ambos, se mueve
            jugador_rect.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        nuevo_rect = jugador_rect.move(velocidad, 0)
        if not nuevo_rect.colliderect(obstaculo) and not nuevo_rect.colliderect(obstaculo2):  # Si no hay colisión con ambos, se mueve
            jugador_rect.x += velocidad

    # Dibujar en pantalla
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana,AZUL,jugador_rect)
    pygame.draw.rect(ventana, AZUL, obstaculo)  # Obstáculo
    pygame.draw.rect(ventana, AZUL, obstaculo2) # Segundo obstáculo
    pygame.display.flip()

    reloj.tick(30)
