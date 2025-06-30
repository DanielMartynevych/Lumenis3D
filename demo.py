import pygame
import math
import numpy as np

WIDTH, HEIGHT = 800, 600
vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
], dtype=np.float32)

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

scale = 100
rotation_speed = 0.01

def rotate_point(point, angle_x, angle_y, angle_z):
    x, y, z = point

    # Rotate around X
    cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
    y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x

    # Rotate around Y
    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
    x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y

    # Rotate around Z
    cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)
    x, y = x * cos_z - y * sin_z, x * sin_z + y * cos_z

    return np.array([x, y, z])

def project_point(point):
    x, y, z = point
    return (WIDTH // 2 + int(x * scale), HEIGHT // 2 + int(y * scale))

def demo():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Lumenis3D Demo")
    font = pygame.font.SysFont('VCR OSD Mono', 20)
    clock = pygame.time.Clock()

    angle_x = angle_y = angle_z = 0
    running = True

    print("Lumenis3D Demo Mode")

    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        angle_x += rotation_speed * dt * 60
        angle_y += rotation_speed * dt * 60
        angle_z += rotation_speed * dt * 60

        screen.fill((0, 0, 0))

        for edge in edges:
            p1 = rotate_point(vertices[edge[0]], angle_x, angle_y, angle_z)
            p2 = rotate_point(vertices[edge[1]], angle_x, angle_y, angle_z)
            pygame.draw.line(screen, (255, 255, 255), project_point(p1), project_point(p2), 2)

        fps_text = font.render("Lumenis 3D DEMO", True, (255, 255, 255))
        screen.blit(fps_text, (10, 10))

        pygame.display.flip()

    pygame.quit()
