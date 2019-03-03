from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    g = [x.strip() for x in f.readlines()]
    
    index = 0
    while index < len(g):
        if g[index] == "line":
            index+= 1
            sp = g[index].split()
            add_edge(points, int(sp[0]), int(sp[1]), int(sp[2]), int(sp[3]), int(sp[4]), int(sp[5]))
        elif g[index] == "ident":
            ident(transform)
        elif g[index] == "scale":
            index+= 1
            sp = g[index].split()
            scale = make_scale(int(sp[0]), int(sp[1]), int(sp[2]))
            matrix_mult(scale, transform)
        elif g[index] == "move":
            index+= 1
            sp = g[index].split()
            translate = make_translate(int(sp[0]), int(sp[1]), int(sp[2]))
            matrix_mult(translate, transform)
        elif g[index] == "rotate":
            index+= 1
            sp = g[index].split()
            axis, theta = sp[0], int(sp[1])
            rotate = make_rotZ(theta) if axis == 'z' else make_rotY(theta) if axis == 'y' else make_rotX(theta)
            matrix_mult(rotate, transform)
        elif g[index] == "apply":
            matrix_mult(transform, points)
            for col_ind in range(len(points)):
                points[col_ind] = [int(x) for x in points[col_ind]]
        elif g[index] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif g[index] == "save":
            clear_screen(screen)
            draw_lines(points, screen, color)
            index+= 1
            save_ppm( screen, g[index])
            save_extension( screen, g[index])
        index+= 1
    
    f.close()
    return
