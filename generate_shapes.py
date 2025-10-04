import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle, Polygon, Circle, Wedge, RegularPolygon
import numpy as np

# Helper: save and close
def save_and_close(fig, filename):
    fig.savefig(f"shapes/{filename}.png")
    plt.close(fig)

# ----------------- BASIC LINES & ANGLES -----------------
def draw_angle():
    fig, ax = plt.subplots()
    ax.plot([0, 2], [0, 0], 'b')
    ax.plot([0, 0], [0, 2], 'r')
    ax.set_xlim(-1, 2.5)
    ax.set_ylim(-1, 2.5)
    ax.set_aspect("equal")
    save_and_close(fig, "angle")

# ----------------- TRIANGLES -----------------
def draw_triangle():
    fig, ax = plt.subplots()
    tri = Polygon([[0,0],[2,0],[1,2]], closed=True, color="green")
    ax.add_patch(tri)
    ax.set_xlim(-1,3)
    ax.set_ylim(-1,3)
    ax.set_aspect("equal")
    save_and_close(fig, "triangle")

def draw_equilateral_triangle():
    fig, ax = plt.subplots()
    eq = RegularPolygon((0,0), numVertices=3, radius=1.5, orientation=np.pi/6, color="cyan")
    ax.add_patch(eq)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "equilateral_triangle")

def draw_isosceles_triangle():
    fig, ax = plt.subplots()
    tri = Polygon([[0,0],[2,0],[1,2]], closed=True, color="orange")
    ax.add_patch(tri)
    ax.set_xlim(-1,3)
    ax.set_ylim(-1,3)
    ax.set_aspect("equal")
    save_and_close(fig, "isosceles_triangle")

def draw_scalene_triangle():
    fig, ax = plt.subplots()
    tri = Polygon([[0,0],[3,0],[2,2]], closed=True, color="purple")
    ax.add_patch(tri)
    ax.set_xlim(-1,4)
    ax.set_ylim(-1,3)
    ax.set_aspect("equal")
    save_and_close(fig, "scalene_triangle")

def draw_right_triangle():
    fig, ax = plt.subplots()
    tri = Polygon([[0,0],[2,0],[0,2]], closed=True, color="red")
    ax.add_patch(tri)
    ax.set_xlim(-1,3)
    ax.set_ylim(-1,3)
    ax.set_aspect("equal")
    save_and_close(fig, "right_triangle")

# ----------------- QUADRILATERALS -----------------
def draw_square():
    fig, ax = plt.subplots()
    sq = Rectangle((-1,-1), 2, 2, color="red")
    ax.add_patch(sq)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "square")

def draw_rectangle():
    fig, ax = plt.subplots()
    rect = Rectangle((-2,-1), 4, 2, color="purple")
    ax.add_patch(rect)
    ax.set_xlim(-3,3)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "rectangle")

def draw_rhombus():
    fig, ax = plt.subplots()
    rhom = Polygon([[0,0],[2,1],[4,0],[2,-1]], closed=True, color="cyan")
    ax.add_patch(rhom)
    ax.set_xlim(-1,5)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "rhombus")

def draw_parallelogram():
    fig, ax = plt.subplots()
    para = Polygon([[0,0],[3,0],[4,2],[1,2]], closed=True, color="blue")
    ax.add_patch(para)
    ax.set_xlim(-1,5)
    ax.set_ylim(-1,3)
    ax.set_aspect("equal")
    save_and_close(fig, "parallelogram")

def draw_trapezium():
    fig, ax = plt.subplots()
    trap = Polygon([[0,0],[4,0],[3,2],[1,2]], closed=True, color="green")
    ax.add_patch(trap)
    ax.set_xlim(-1,5)
    ax.set_ylim(-1,3)
    ax.set_aspect("equal")
    save_and_close(fig, "trapezium")

def draw_kite():
    fig, ax = plt.subplots()
    kite = Polygon([[0,0],[2,2],[4,0],[2,-3]], closed=True, color="orange")
    ax.add_patch(kite)
    ax.set_xlim(-2,6)
    ax.set_ylim(-4,3)
    ax.set_aspect("equal")
    save_and_close(fig, "kite")

# ----------------- POLYGONS -----------------
def draw_regular_polygon(n, name):
    fig, ax = plt.subplots()
    poly = RegularPolygon((0,0), numVertices=n, radius=2, color="pink")
    ax.add_patch(poly)
    ax.set_xlim(-3,3)
    ax.set_ylim(-3,3)
    ax.set_aspect("equal")
    save_and_close(fig, f"{name}")

# ----------------- CIRCLES & CURVES -----------------
def draw_circle():
    fig, ax = plt.subplots()
    circ = Circle((0,0), 1.5, color="blue")
    ax.add_patch(circ)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "circle")

def draw_semicircle():
    fig, ax = plt.subplots()
    semi = Wedge((0,0), 1.5, 0, 180, color="orange")
    ax.add_patch(semi)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "semicircle")

def draw_quadrant():
    fig, ax = plt.subplots()
    quad = Wedge((0,0), 1.5, 0, 90, color="pink")
    ax.add_patch(quad)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "quadrant")

def draw_ellipse():
    fig, ax = plt.subplots()
    ellipse = Ellipse((0,0), 3, 1.5, color="yellow")
    ax.add_patch(ellipse)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "ellipse")

def draw_sector():
    fig, ax = plt.subplots()
    sec = Wedge((0,0), 1.5, 30, 120, color="green")
    ax.add_patch(sec)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "sector")

def draw_annulus():
    fig, ax = plt.subplots()
    ring = Wedge((0,0), 1.5, 0, 360, width=0.5, color="gray")
    ax.add_patch(ring)
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_aspect("equal")
    save_and_close(fig, "annulus")

# ----------------- 3D SHAPES (2D Sketches) -----------------
def draw_cube():
    fig, ax = plt.subplots()
    sq1 = Rectangle((0,0), 2, 2, fill=None, edgecolor="blue")
    sq2 = Rectangle((0.5,0.5), 2, 2, fill=None, edgecolor="red")
    ax.add_patch(sq1)
    ax.add_patch(sq2)
    ax.plot([0,0.5],[0,0.5],'k')
    ax.plot([2,2.5],[0,0.5],'k')
    ax.plot([0,0.5],[2,2.5],'k')
    ax.plot([2,2.5],[2,2.5],'k')
    ax.set_xlim(-1,4)
    ax.set_ylim(-1,4)
    ax.set_aspect("equal")
    save_and_close(fig, "cube")

def draw_cylinder():
    fig, ax = plt.subplots()
    top = Ellipse((0,2), 2, 0.5, fill=False)
    bottom = Ellipse((0,0), 2, 0.5, fill=False)
    ax.add_patch(top)
    ax.add_patch(bottom)
    ax.plot([-1, -1], [0,2], 'k')
    ax.plot([1, 1], [0,2], 'k')
    ax.set_xlim(-2,2)
    ax.set_ylim(-1,3)
    ax.set_aspect("equal")
    save_and_close(fig, "cylinder")

def draw_cone():
    fig, ax = plt.subplots()
    base = Ellipse((0,0), 2, 0.5, fill=False)
    ax.add_patch(base)
    ax.plot([0,-1],[2,0],'k')
    ax.plot([0,1],[2,0],'k')
    ax.set_xlim(-2,2)
    ax.set_ylim(-1,3)
    ax.set_aspect("equal")
    save_and_close(fig, "cone")

# ----------------- MAIN RUNNER -----------------
if __name__ == "__main__":
    draw_angle()
    draw_triangle()
    draw_equilateral_triangle()
    draw_isosceles_triangle()
    draw_scalene_triangle()
    draw_right_triangle()
    draw_square()
    draw_rectangle()
    draw_rhombus()
    draw_parallelogram()
    draw_trapezium()
    draw_kite()

    # Polygons
    for n, name in [(5,"pentagon"),(6,"hexagon"),(7,"heptagon"),(8,"octagon"),(9,"nonagon"),
                    (10,"decagon"),(12,"dodecagon")]:
        draw_regular_polygon(n, name)

    # Circles etc
    draw_circle()
    draw_semicircle()
    draw_quadrant()
    draw_ellipse()
    draw_sector()
    draw_annulus()

    # Solids
    draw_cube()
    draw_cylinder()
    draw_cone()

    print("✅ All shapes generated into 'shapes/' folder.")
