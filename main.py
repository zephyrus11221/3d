from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

parse_file( 'script', edges, transform, screen, color )

'''
#drawing
for i in range(16):
    add_sphere(edges, 0, 0, 0, 150, .1/(i+1))
    matrix_mult(make_rotX(math.pi/4), edges)
    matrix_mult(make_rotY(math.pi/4), edges)
    matrix_mult(make_translate(250, 250, 0), edges)
    color = [(i*32)%255, 50+i*11, 200-i*11]
    draw_lines(edges, screen, color)
    edges = []

for i in range(10):
    add_torus(edges, 0, 0, 0, 50, 225, .1/(i+1))
    matrix_mult(make_rotX(3*math.pi/4), edges)
    matrix_mult(make_rotY(math.pi/4), edges)
    matrix_mult(make_translate(250, 250, 0), edges)
    color = [(i*i*5+50)%255, (250-i*20)%255, (100+i*i*i)*255]
    draw_lines(edges, screen, color)
    edges = []

display(screen)
'''
