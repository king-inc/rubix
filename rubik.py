from Classes.HelperFunctions import *

rubiks_cube = CreateCube()
rubiks_cube.PrintCube()
rubiks_cube = ScatterCube(rubiks_cube, 10)
#back = rubiks_cube.GetFaceFromPos("back")
#front = rubiks_cube.GetFaceFromPos("front")
#print(rubiks_cube.faces[back].GetColor()) 
#print(rubiks_cube.faces[front].GetColor())
#print(rubiks_cube.faces[back].GetNodes()[0][0].GetColors()[0])
#print(rubiks_cube.faces[front].GetNodes()[0][0].GetColors()[0])
            
            
        