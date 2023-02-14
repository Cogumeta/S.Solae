import pygame
import math

# Inicializa o Pygame
pygame.init()

# Define as propriedades de cada planeta
planetas = []
planetas_pos = [(0, 0), (125, 1), (200, 2), (300, 3), (400, 4), (500, 5), (600, 6), (900, 7)]
planetas_vel = [(10, 100), (20, 200), (30, 300), (40, 400), (50, 500), (60, 600), (70, 700), (80, 800)]
planetas_mass = [1, 2, 3, 4, 5, 6, 7, 8]
planetas_radius = [75, 25, 30, 35, 40, 45, 50, 55]

# Define a constante gravitacional
G = 6.67430 * 10**-11 # m^3 kg^-1 s^-2

# Define a atualização da simulação
def update():
    for i in range(8):
        for j in range(8):
            if i != j:
                delta_x = planetas_pos[j][0] - planetas_pos[i][0]
                delta_y = planetas_pos[j][1] - planetas_pos[i][1]
                distance = math.sqrt(delta_x**2 + delta_y**2)
                force = G * planetas_mass[i] * planetas_mass[j] / distance**2
                angle = math.atan2(delta_y, delta_x)
                force_x = force * math.cos(angle)
                force_y = force * math.sin(angle)
                planetas_vel[i] = (planetas_vel[i][0] + force_x / planetas_mass[i],
                                   planetas_vel[i][1] + force_y / planetas_mass[i])
        planetas_pos[i] = (planetas_pos[i][0] + planetas_vel[i][0],
                           planetas_pos[i][1] + planetas_vel[i][1])

# Define as dimensões da tela
screen = pygame.display.set_mode((1280, 600))

# Define a cor do fundo da tela
background_color = (0, 0, 0)

# Define o loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            update()

    # Preenche o fundo da tela com a cor definida
    screen.fill(background_color)

    # Desenha os planetas na tela
    for i in range(8):
        circle_color = (0, 0, 255)
        circle_x = 1280/2.25 + planetas_pos[i][0]
        circle_y = 600/2.25 + planetas_pos[i][1]
        circle_radius = planetas_radius[i]
        pygame.draw.circle(screen, circle_color, (int(circle_x), int(circle_y)), circle_radius)

    # Atualiza a tela
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
