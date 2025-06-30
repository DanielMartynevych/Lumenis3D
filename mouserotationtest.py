import pygame
import math
import numpy as np

WIDTH, HEIGHT = 800, 600
vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Back face
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # Front face
], dtype=np.float32)

edges = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (0,4), (1,5), (2,6), (3,7)
]

scale = 100

def rotate_point(point, angle_x, angle_y):
    x, y, z = point
    cos_x, sin_x = np.cos(angle_x), np.sin(angle_x)
    y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x
    cos_y, sin_y = np.cos(angle_y), np.sin(angle_y)
    x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y
    return np.array([x, y, z])

def project_point(point):
    x, y, z = point
    return (WIDTH//2 + int(x * scale), HEIGHT//2 + int(y * scale))

def get_rotated_vertices(angle_x, angle_y):
    rotated = []
    for vertex in vertices:
        rv = rotate_point(vertex, angle_x, angle_y)
        rotated.append([round(float(rv[0]), 4), round(float(rv[1]), 4), round(float(rv[2]), 4)])
    return rotated

def print_vertex_coords(angle_x, angle_y):
    rotated = get_rotated_vertices(angle_x, angle_y)
    print("\nvertices = [")
    for v in rotated:
        print(f"    {v},")
    print("]")

def mouserotationtest():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Lumenis3D Mouse Rotation Test")
    font = pygame.font.SysFont('VCR OSD Mono', 16)
    clock = pygame.time.Clock()

    angle_x, angle_y = 0, 0
    dragging = False
    last_mouse_pos = (0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                dragging = True
                last_mouse_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                dragging = False
                print_vertex_coords(angle_x, angle_y)
            elif event.type == pygame.MOUSEMOTION and dragging:
                dx = (event.pos[0] - last_mouse_pos[0]) * -0.01
                dy = (event.pos[1] - last_mouse_pos[1]) * 0.01
                angle_y += dx
                angle_x += dy
                last_mouse_pos = event.pos

        screen.fill((0, 0, 0))

        for edge in edges:
            p1 = rotate_point(vertices[edge[0]], angle_x, angle_y)
            p2 = rotate_point(vertices[edge[1]], angle_x, angle_y)
            pygame.draw.line(screen, (255, 255, 255), project_point(p1), project_point(p2), 2)

        text = font.render("Left-click and drag to rotate. Release to print vertex coordinate list.", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
