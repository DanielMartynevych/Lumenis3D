#Lumenis3D MAIN
import pygame
import numpy as np
vertices = np.array([
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], #back
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]  #front
], dtype=np.float32)
faces = [
    {'verts': [0, 1, 2, 3], 'color': (102, 51, 0)},    # Back
    {'verts': [4, 5, 6, 7], 'color': (102, 51, 0)},    # Front
    {'verts': [0, 1, 5, 4], 'color': (102, 51, 0)},    # Bottom
    {'verts': [2, 3, 7, 6], 'color': (0, 255, 0)},   # Top
    {'verts': [1, 2, 6, 5], 'color': (102, 51, 0)},   # Right
    {'verts': [0, 3, 7, 4], 'color': (102, 51, 0)}    # Left
]
def vertices(vertexlist):
     vertices = vertexlist
     return print("Vertices created. Make sure the list is a np.array because we do not have detection and/or error raising at the moment")
def faces(facelist):
    faces = facelist
    return print("Faces created. Make sure the example face entry looks like `{'verts': [0, 1, 2, 3], 'color': (102, 51, 0)}`")
def rotate(vertexlist, ax, ay):
    cos_x, sin_x = np.cos(ax), np.sin(ax)
    rot_x = np.array([
        [1,      0,       0     ],
        [0,  cos_x,  -sin_x],
        [0,  sin_x,   cos_x]
    ])

    cos_y, sin_y = np.cos(ay), np.sin(ay)
    rot_y = np.array([
        [ cos_y, 0, sin_y],
        [     0, 1,     0],
        [-sin_y, 0, cos_y]
    ])

    return vertexlist @ rot_x.T @ rot_y.T

def project(vertex, width, height):
    x, y, z = vertex
    z += 5
    if z <= 0.1:
        z = 0.1
    f = 300
    factor = f / z
    return (width // 2 + int(x * factor), height // 2 - int(y * factor))

def draw(surface, vertices, faces, width, height):
    face_data = []

    for face in faces:
        idxs = face['verts']
        pts_3d = vertices[idxs]
        pts_2d = [project(v, width, height) for v in pts_3d]  # pass width, height here

        avg_z = np.mean(pts_3d[:, 2])
        face_data.append({'points': pts_2d, 'color': face['color'], 'depth': avg_z})

    face_data.sort(key=lambda f: f['depth'], reverse=True)

    for face in face_data:
        pygame.draw.polygon(surface, face['color'], face['points'])
        pygame.draw.polygon(surface, (0, 0, 0), face['points'], 1)
