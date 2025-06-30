This is a short README with some commands:
1. rotate(vertexlist, ax, ay) Function

 Purpose:
Applies 3D rotation transformations to an array of vertices around the X and Y axes.

 Parameters:
- vertexlist: A NumPy array of shape (n, 3) containing 3D vertex coordinates
- ax: Rotation angle (in radians) around the X-axis
- ay: Rotation angle (in radians) around the Y-axis

 Vertexlist example:
vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
])
 Notes
- Rotation order matters (X then Y)
- Input angles must be in radians (use np.radians() to convert from degrees)

2. draw(surface, vertices, faces, width, height)

 Purpose:
Renders the shape onto a 2D window

 Parameters:
- surface: Pygame surface to draw on
- vertices: Transformed 3D vertex coordinates (output from rotate())
- faces: List of face definitions containing:
  - verts: Indices of vertices that form the face
  - color: RGB color tuple for the face
  Example:
  faces = [
      {'verts': [0, 1, 2, 3], 'color': (102, 51, 0)},    # Back
      {'verts': [4, 5, 6, 7], 'color': (102, 51, 0)},    # Front
      {'verts': [0, 1, 5, 4], 'color': (102, 51, 0)},    # Bottom
      {'verts': [2, 3, 7, 6], 'color': (0, 255, 0)},   # Top
      {'verts': [1, 2, 6, 5], 'color': (102, 51, 0)},   # Right
      {'verts': [0, 3, 7, 4], 'color': (102, 51, 0)}    # Left
  ]
- width: Width of the window (for projection scaling)
- height: Height of the window (for projection scaling)
