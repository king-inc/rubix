from Classes.Cube import Cube
from Classes.Face import Face
from Classes.Node import Node
import random

ROW = 3

def CreateCube():
    faces = [0,0,0,0,0,0]
    rubiks_cube = Cube(faces)
    for i in range(6):
        face = Face([[0,0,0],
                    [0,0,0],
                    [0,0,0]], rubiks_cube.all_colors[i])
        
        color_pos = rubiks_cube.ChangeFront(rubiks_cube.all_colors[i])
        #print("post change: ", color_pos)
        for j in range(ROW):
            if j == 0:
                #vertical then horizontal for corners
                face.nodes[j][0] = Node([color_pos["front"], color_pos["top"], color_pos["left"]],2)
                face.nodes[j][1] = Node([color_pos["front"], color_pos["top"]], 1)
                face.nodes[j][2] = Node([color_pos["front"], color_pos["top"], color_pos["right"]], 2)
            elif j == 1:
                face.nodes[j][0] = Node([color_pos["front"], color_pos["left"]],1)
                face.nodes[j][1] = Node([color_pos["front"]], 0)
                face.nodes[j][2] = Node([color_pos["front"], color_pos["right"]], 1)
            elif j == 2:
                #vertical then horizontal for corners
                face.nodes[j][0] = Node([color_pos["front"], color_pos["bottom"], color_pos["left"]],2)
                face.nodes[j][1] = Node([color_pos["front"], color_pos["bottom"]], 1)
                face.nodes[j][2] = Node([color_pos["front"], color_pos["bottom"], color_pos["right"]], 2)
        faces[i] = face
        #print(rubiks_cube.faces[i].GetColor())
        #rubiks_cube.PrintCube()
    rubiks_cube = Cube(faces)
    return rubiks_cube


def ScatterCube(cube, scatter):
    operations = [cube.RotateLU,
               cube.RotateLD,
               cube.RotateRU,
               cube.RotateRD,
               cube.RotateUL,
               cube.RotateUR,
               cube.RotateDL,
               cube.RotateDR,
               cube.RotateFaceL,
               cube.RotateFaceR]
    for i in range(scatter):
        choice_operation = random.choice(operations)
        choice_face = random.choice(list(cube.color_pos.keys()))
        choice_operation(choice_face)
        print(choice_operation,choice_face)
        cube.PrintCube()
    return cube
