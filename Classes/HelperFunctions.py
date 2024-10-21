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
    moves = []
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
        moves.append((choice_operation,choice_face))
        print(choice_operation,choice_face)
    
    cube.PrintCube()
    return cube, moves


def SolveWithSetMoves(cube, moves):
    correct_cube = CreateCube()
    for entry in moves:
        if entry[0] == cube.RotateLU:
            print(cube.RotateLD)
            cube.RotateLD(entry[1])
        elif entry[0] == cube.RotateLD:
            print(cube.RotateLU)
            cube.RotateLU(entry[1])
        elif entry[0] == cube.RotateRD:
            print(cube.RotateRU)
            cube.RotateRU(entry[1])
        elif entry[0] == cube.RotateRU:
            print(cube.RotateRD)
            cube.RotateRD(entry[1])
        elif entry[0] == cube.RotateUL:
            print(cube.RotateUR)
            cube.RotateUR(entry[1])
        elif entry[0] == cube.RotateUR:
            print(cube.RotateUL)
            cube.RotateUL(entry[1])
        elif entry[0] == cube.RotateDL:
            print(cube.RotateDR)
            cube.RotateDR(entry[1])
        elif entry[0] == cube.RotateDR:
            print(cube.RotateDL)
            cube.RotateDL(entry[1])
        elif entry[0] == cube.RotateFaceL:
            print(cube.RotateFaceR)
            cube.RotateFaceR(entry[1])
        elif entry[0] == cube.RotateFaceR:
            print(cube.RotateFaceL)
            cube.RotateFaceL(entry[1])
    cube.PrintCube()
    print(cube == correct_cube)

def SolveCubeRandom(cube):
    correct_cube = CreateCube()
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
    correct = False
    num_of_operations = 0
    while not correct:
        if cube == correct_cube:
            correct = True
        else:
            choice_operation = random.choice(operations)
            choice_face = random.choice(list(cube.color_pos.keys()))
            choice_operation(choice_face)
            #print(choice_operation,choice_face)
            num_of_operations += 1
    cube.PrintCube()
    print(num_of_operations)
    return cube

def SuneSolver(cube):
    correct_cube = CreateCube()
    operations  = [cube.RotateRU,
                   cube.RotateUL,
                   cube.RotateRD,
                   cube.RotateUL,
                   cube.RotateRU,
                   cube.RotateUL,
                   cube.RotateUL,
                   cube.RotateRD]
    curr_op = 0
    num_of_operations = 0
    while cube != correct_cube:
        print(operations[curr_op])
        operations[curr_op]("front")
        curr_op+=1
        num_of_operations += 1
        if curr_op >= len(operations):
            curr_op = 0
    
    cube.PrintCube()
