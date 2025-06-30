import pygame
import numpy as np

WIDTH, HEIGHT = 800, 600

# Cube vertices
vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Back
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # Front
], dtype=np.float32)

# Cube faces
faces = [
    {'verts': [0, 1, 2, 3], 'color': (102, 51, 0)},    # Back
    {'verts': [4, 5, 6, 7], 'color': (102, 51, 0)},    # Front
    {'verts': [0, 1, 5, 4], 'color': (102, 51, 0)},    # Bottom
    {'verts': [2, 3, 7, 6], 'color': (0, 255, 0)},     # Top
    {'verts': [1, 2, 6, 5], 'color': (102, 51, 0)},    # Right
    {'verts': [0, 3, 7, 4], 'color': (102, 51, 0)}     # Left
]

def rotate(vertex, ax, ay):
    x, y, z = vertex

    cos_x, sin_x = np.cos(ax), np.sin(ax)
    y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x

    cos_y, sin_y = np.cos(ay), np.sin(ay)
    x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y

    return np.array([x, y, z])

def project(vertex):
    x, y, z = vertex
    z += 5
    if z <= 0.1:
        z = 0.1
    f = 300
    factor = f / z
    return np.array([WIDTH // 2 + x * factor, HEIGHT // 2 - y * factor])

def draw_cube(surface, ax, ay):
    transformed = [rotate(v, ax, ay) for v in vertices]
    projected = [project(v) for v in transformed]

    face_list = []
    for face in faces:
        idxs = face['verts']
        z_depth = max(transformed[i][2] for i in idxs)
        face_list.append({
            'points': [projected[i] for i in idxs],
            'color': face['color'],
            'depth': z_depth
        })

    face_list.sort(key=lambda f: f['depth'], reverse=True)
    for face in face_list:
        pygame.draw.polygon(surface, face['color'], face['points'])
        pygame.draw.polygon(surface, (0, 0, 0), face['points'], 1)

def texturetest():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Lumenis3D Texture Test")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mx, my = pygame.mouse.get_pos()
        dx = (mx - WIDTH // 2) / WIDTH * -2 * np.pi
        dy = (my - HEIGHT // 2) / HEIGHT * -2 * np.pi

        screen.fill((30, 30, 30))
        draw_cube(screen, dy, dx)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
