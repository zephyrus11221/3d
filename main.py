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

#parse_file( 'script', edges, transform, screen, color )
'''
add_sphere(edges, 0, 0, 0, 150, .01)
draw_lines(edges, screen, color)
for i in range(7):
    matrix_mult(make_rotX(math.pi/7), edges)
    color = [i*20, i*20, i*20]
    draw_lines(edges, screen, color)
'''
for i in range(3):
    add_sphere(edges, 250, 250, 0, 150, .1/(i+1))
    print i*20
    color = [75+i*20, 75+i*20, 75+i*20]
    draw_lines(edges, screen, color)
    edges = []

display(screen)
