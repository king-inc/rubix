ROW = 3
import random

class Node:
    def __init__(self, _colors, _node_type):
        self.colors = _colors
        self.node_type = _node_type

    def GetColors(self):
        return self.colors
    def GetType(self):
        return self.node_type

class Face: 
    def __init__(self, nodes, color):
        self.nodes = nodes
        self.color = color

    def GetNodes(self):
        return self.nodes
    def SetNodes(self, nodes):
        self.nodes = nodes
    def GetColor(self):
        return self.color
    def GetLineNodes(self, line):
        nodes = []
        if line == "L":
            for i in range(ROW):
                nodes.append(self.nodes[i][0])
        elif line == "R":
            for i in range(ROW):
                nodes.append(self.nodes[i][2])
        elif line == "U":
            nodes = self.nodes[0]
        elif line == "D":
            nodes = self.nodes[2]
        return nodes

    def ChangeLine(self,nodes, line):
        if line == "L":
            for i in range(ROW):
                self.nodes[i][0] = nodes[i]
        elif line == "R":
            for i in range(ROW):
                self.nodes[i][2] = nodes[i]
        elif line == "U":
            self.nodes[0] = nodes
        elif line == "D":
            self.nodes[2] = nodes
        
    def RotateFace(self,direction):
        if direction == "L":
            self.nodes[0][0], self.nodes[0][1], self.nodes[0][2],self.nodes[1][2], self.nodes[2][2], self.nodes[2][0],self.nodes[2][1], self.nodes[1][0] = self.nodes[2][0], self.nodes[1][0], self.nodes[0][0],self.nodes[0][1],self.nodes[0][2],self.nodes[2][2],self.nodes[1][2],self.nodes[2][1]
        elif direction == "R":
            self.nodes[0][0], self.nodes[0][1], self.nodes[0][2],self.nodes[1][2], self.nodes[2][2], self.nodes[2][0],self.nodes[2][1], self.nodes[1][0] = self.nodes[0][2],self.nodes[1][2],self.nodes[2][2],self.nodes[2][1],self.nodes[2][0],self.nodes[0][0],self.nodes[1][0],self.nodes[0][1]

class Cube:
    
    def __init__(self, faces):
        self.faces = faces
        self.all_colors = ["red","blue","yellow","green","white","orange"]
        self.color_pos = {"front":"red",
                        "back":"orange",
                        "top":"blue",
                        "bottom":"green",
                        "left":"yellow",
                        "right":"white"}
        self.FRONT = self.GetFaceFromPos("front")
        self.BACK = self.GetFaceFromPos("back")
        self.TOP = self.GetFaceFromPos("top")
        self.BOTTOM = self.GetFaceFromPos("bottom")
        self.LEFT = self.GetFaceFromPos("left")
        self.RIGHT = self.GetFaceFromPos("right")
        
    def SetFaces(self, faces):
        self.faces = faces
    def ChangeFront(self, color):
        output = self.color_pos.copy()
        for key in self.color_pos:
            if self.color_pos[key] == color:
                #print(key)
                #print("pre change: ",self.color_pos)
                if key == "front":
                    return output
                if key == "bottom":
                    output["front"],output["back"],output["top"],output["bottom"] = output["bottom"],output["top"],output["front"],output["back"]
                    left = self.GetFaceFromPos("left")
                    right = self.GetFaceFromPos("right")
                    if left != False:
                        self.faces[left].RotateFace("R")
                    if right != False:
                        self.faces[right].RotateFace("L")
                elif key == "top":
                    output["front"],output["back"],output["top"],output["bottom"] = output["top"],output["bottom"],output["back"],output["front"]
                    left = self.GetFaceFromPos("left")
                    right = self.GetFaceFromPos("right")
                    if left != False:
                        self.faces[left].RotateFace("L")
                    if right != False:
                        self.faces[right].RotateFace("R")
                elif key == "right":
                    output["front"],output["back"],output["left"],output["right"] = output["right"],output["left"],output["front"],output["back"]
                    top = self.GetFaceFromPos("top")
                    bottom = self.GetFaceFromPos("bottom")
                    if top != False:
                        self.faces[top].RotateFace("L")
                    if bottom != False:
                        self.faces[bottom].RotateFace("R")
                elif key == "left":
                    output["front"],output["back"],output["left"],output["right"] = output["left"],output["right"],output["back"],output["front"]
                    top = self.GetFaceFromPos("top")
                    bottom = self.GetFaceFromPos("bottom")
                    if top != False:
                        self.faces[top].RotateFace("R")
                    if bottom != False:
                        self.faces[bottom].RotateFace("L")
                elif key == "back":
                    output["front"],output["back"],output["top"],output["bottom"] = output["back"],output["front"],output["bottom"],output["top"]
                    left = self.GetFaceFromPos("left")
                    right = self.GetFaceFromPos("right")
                    if left != False:
                        self.faces[left].RotateFace("L")
                        self.faces[left].RotateFace("L")
                    if right != False:
                        self.faces[right].RotateFace("R")
                        self.faces[right].RotateFace("R")
                break
        return output
            
    def GetFaceFromPos(self,pos):
        for key in self.color_pos:
            if key == pos:
                for i in range(len(self.faces)):
                    if self.faces[i] != 0 and self.color_pos[key] == self.faces[i].GetColor():
                        return i
                return False
    def PrintCube(self):
        print_pos = {}
        curr_face = 0
        for key in self.color_pos:
            #find the right face
            for i in range(len(self.faces)):
                if self.faces[i].GetColor() == self.color_pos[key]:
                    curr_face = i
            face_string = []
            for i in range(ROW):
                face_string.append(self.faces[curr_face].GetNodes()[i][0].GetColors()[0] + " | " + self.faces[curr_face].GetNodes()[i][1].GetColors()[0] + " | " + self.faces[curr_face].GetNodes()[i][2].GetColors()[0])
                if i<2:
                    face_string.append("--- + --- + ---")
            print_pos.update({key:face_string})

        output = []
        first_line = ""
        sec_line = ""
        third_line = ""
        #j is elements in self.color_pos key
        for j in range(5):
            if j<1:
                first_line += print_pos["back"][j] + " | " + print_pos["top"][j]
                sec_line += print_pos["left"][j] + " | " + print_pos["front"][j] + " | " + print_pos["right"][j]
                third_line += "                 " + " | " + print_pos["bottom"][j] + " | "
            else:
                first_line += "\n" + print_pos["back"][j] + " | " + print_pos["top"][j]
                sec_line += "\n" +print_pos["left"][j] + " | " + print_pos["front"][j] + " | " + print_pos["right"][j]
                third_line += "\n                 " + " | " + print_pos["bottom"][j] + " | "
        output = [first_line,sec_line,third_line]
        output_str = ""
        for i in range(len(output)):
            if i < 1:
                output_str += output[i]
            else:
                output_str += "\n" +output[i]
            if i<2:
                output_str += "\n--- + --- + --- + --- + --- + --- + --- + --- + ---"
        print(output_str)

    def RotateLU(self, key):
        #key is the face to be turned
        if key =="front" or key =="back" or key =="top" or key=="bottom":
            front_line = self.faces[self.FRONT].GetLineNodes("L")
            top_line = self.faces[self.TOP].GetLineNodes("L")
            bottom_line = self.faces[self.BOTTOM].GetLineNodes("L")
            back_line = self.faces[self.BACK].GetLineNodes("L")

            self.faces[self.FRONT].ChangeLine(bottom_line, "L")
            self.faces[self.TOP].ChangeLine(front_line, "L")
            self.faces[self.BACK].ChangeLine(top_line, "L")
            self.faces[self.BOTTOM].ChangeLine(back_line,"L")

            self.faces[self.LEFT].RotateFace("R")
        
        elif key=="left":
            top_line = self.faces[self.TOP].GetLineNodes("U")
            bottom_line = self.faces[self.BOTTOM].GetLineNodes("D")
            left_line = self.faces[self.LEFT].GetLineNodes("L")
            right_line = self.faces[self.RIGHT].GetLineNodes("R")

            self.faces[self.LEFT].ChangeLine(bottom_line, "L")
            self.faces[self.TOP].ChangeLine(left_line, "U")
            self.faces[self.RIGHT].ChangeLine(top_line, "R")
            self.faces[self.BOTTOM].ChangeLine(right_line,"D")

            self.faces[self.BACK].RotateFace("R")
        
        elif key=="right":
            top_line = self.faces[self.TOP].GetLineNodes("D")
            bottom_line = self.faces[self.BOTTOM].GetLineNodes("U")
            left_line = self.faces[self.LEFT].GetLineNodes("R")
            right_line = self.faces[self.RIGHT].GetLineNodes("L")

            self.faces[self.RIGHT].ChangeLine(bottom_line, "L")
            self.faces[self.TOP].ChangeLine(right_line, "D")
            self.faces[self.LEFT].ChangeLine(top_line, "R")
            self.faces[self.BOTTOM].ChangeLine(left_line,"U")

            self.faces[self.FRONT].RotateFace("R")

    def RotateLD(self, key):
        if key =="front" or key =="back" or key =="top" or key=="bottom":
            front_line = self.faces[self.FRONT].GetLineNodes("L")
            top_line = self.faces[self.TOP].GetLineNodes("L")
            bottom_line = self.faces[self.BOTTOM].GetLineNodes("L")
            back_line = self.faces[self.BACK].GetLineNodes("L")

            self.faces[self.FRONT].ChangeLine(top_line, "L")
            self.faces[self.TOP].ChangeLine(back_line, "L")
            self.faces[self.BACK].ChangeLine(bottom_line, "L")
            self.faces[self.BOTTOM].ChangeLine(front_line,"L")

            self.faces[self.LEFT].RotateFace("L")
        
        elif key=="left":
            top_line = self.faces[self.TOP].GetLineNodes("U")
            bottom_line = self.faces[self.BOTTOM].GetLineNodes("D")
            left_line = self.faces[self.LEFT].GetLineNodes("L")
            right_line = self.faces[self.RIGHT].GetLineNodes("R")

            self.faces[self.LEFT].ChangeLine(top_line, "L")
            self.faces[self.TOP].ChangeLine(right_line, "U")
            self.faces[self.RIGHT].ChangeLine(bottom_line, "R")
            self.faces[self.BOTTOM].ChangeLine(left_line,"D")

            self.faces[self.BACK].RotateFace("L")
        
        elif key=="right":
            top_line = self.faces[self.TOP].GetLineNodes("D")
            bottom_line = self.faces[self.BOTTOM].GetLineNodes("U")
            left_line = self.faces[self.LEFT].GetLineNodes("R")
            right_line = self.faces[self.RIGHT].GetLineNodes("L")

            self.faces[self.RIGHT].ChangeLine(top_line, "L")
            self.faces[self.TOP].ChangeLine(left_line, "D")
            self.faces[self.LEFT].ChangeLine(bottom_line, "R")
            self.faces[self.BOTTOM].ChangeLine(right_line,"U")

            self.faces[self.FRONT].RotateFace("R")
        
    def RotateRU(self, key):
        if key =="front" or key =="back" or key =="top" or key=="bottom":
            front_line = self.faces[self.FRONT].GetLineNodes("R")
            top_line = self.faces[self.TOP].GetLineNodes("R")
            bottom_line = self.faces[self.BOTTOM].GetLineNodes("R")
            back_line = self.faces[self.BACK].GetLineNodes("R")

            self.faces[self.FRONT].ChangeLine(bottom_line, "R")
            self.faces[self.TOP].ChangeLine(front_line, "R")
            self.faces[self.BACK].ChangeLine(top_line, "R")
            self.faces[self.BOTTOM].ChangeLine(back_line,"R")

            self.faces[self.RIGHT].RotateFace("R")
        
        elif key=="left":
            self.RotateLD("right")
        
        elif key=="right":
            self.RotateLD("left")

    def RotateRD(self, key):
        if key =="front" or key =="back" or key =="top" or key=="bottom":
            front_line = self.faces[self.FRONT].GetLineNodes("R")
            top_line = self.faces[self.TOP].GetLineNodes("R")
            bottom_line = self.faces[self.BOTTOM].GetLineNodes("R")
            back_line = self.faces[self.BACK].GetLineNodes("R")

            self.faces[self.FRONT].ChangeLine(top_line, "R")
            self.faces[self.TOP].ChangeLine(back_line, "R")
            self.faces[self.BACK].ChangeLine(bottom_line, "R")
            self.faces[self.BOTTOM].ChangeLine(front_line,"R")

            self.faces[self.RIGHT].RotateFace("L")
        
        elif key=="left":
            self.RotateLU("right")
        
        elif key=="right":
            self.RotateLU("left")

    def RotateUL(self, key):
        #key is the face to be turned
        if key =="front" or key =="back" or key =="left" or key=="right":
            front_line = self.faces[self.FRONT].GetLineNodes("U")
            left_line = self.faces[self.LEFT].GetLineNodes("U")
            right_line = self.faces[self.RIGHT].GetLineNodes("U")
            back_line = self.faces[self.BACK].GetLineNodes("D")

            self.faces[self.FRONT].ChangeLine(right_line, "U")
            self.faces[self.LEFT].ChangeLine(front_line, "U")
            self.faces[self.BACK].ChangeLine(left_line, "D")
            self.faces[self.RIGHT].ChangeLine(back_line,"U")

            self.faces[self.TOP].RotateFace("L")
        
        elif key=="top":
            self.RotateLU("left")
        elif key=="bottom":
            self.RotateLU("right")

    def RotateUR(self, key):
        #key is the face to be turned
        if key =="front" or key =="back" or key =="left" or key=="right":
            front_line = self.faces[self.FRONT].GetLineNodes("U")
            left_line = self.faces[self.LEFT].GetLineNodes("U")
            right_line = self.faces[self.RIGHT].GetLineNodes("U")
            back_line = self.faces[self.BACK].GetLineNodes("D")

            self.faces[self.FRONT].ChangeLine(left_line, "U")
            self.faces[self.LEFT].ChangeLine(back_line, "U")
            self.faces[self.BACK].ChangeLine(right_line, "D")
            self.faces[self.RIGHT].ChangeLine(front_line,"U")

            self.faces[self.TOP].RotateFace("R")
        
        elif key=="top":
            self.RotateLD("left")
        elif key=="bottom":
            self.RotateLD("right")
    
    def RotateDL(self, key):
        #key is the face to be turned
        if key =="front" or key =="back" or key =="left" or key=="right":
            front_line = self.faces[self.FRONT].GetLineNodes("D")
            left_line = self.faces[self.LEFT].GetLineNodes("D")
            right_line = self.faces[self.RIGHT].GetLineNodes("D")
            back_line = self.faces[self.BACK].GetLineNodes("U")

            self.faces[self.FRONT].ChangeLine(right_line, "D")
            self.faces[self.LEFT].ChangeLine(front_line, "D")
            self.faces[self.BACK].ChangeLine(left_line, "U")
            self.faces[self.RIGHT].ChangeLine(back_line,"D")

            self.faces[self.BOTTOM].RotateFace("L")
        
        elif key=="top" or key=="bottom":
            self.RotateLD("right")
        elif key=="bottom":
            self.RotateLD("left")

    def RotateDR(self, key):
        #key is the face to be turned
        if key =="front" or key =="back" or key =="left" or key=="right":
            front_line = self.faces[self.FRONT].GetLineNodes("D")
            left_line = self.faces[self.LEFT].GetLineNodes("D")
            right_line = self.faces[self.RIGHT].GetLineNodes("D")
            back_line = self.faces[self.BACK].GetLineNodes("U")

            self.faces[self.FRONT].ChangeLine(left_line, "D")
            self.faces[self.LEFT].ChangeLine(back_line, "D")
            self.faces[self.BACK].ChangeLine(right_line, "U")
            self.faces[self.RIGHT].ChangeLine(front_line,"D")

            self.faces[self.BOTTOM].RotateFace("R")
        
        elif key=="top":
            self.RotateLU("right")
        elif key=="bottom":
            self.RotateLU("left")

    def RotateFaceL(self, key):
        if key=="front":
            self.RotateLU("right")
        elif key== "back":
            self.RotateLU("left")
        elif key=="left":
            self.RotateLU("front")
        elif key=="right":
            self.RotateRU("front")
        elif key=="top":
            self.RotateUL("front")
        elif key=="bottom":
            self.RotateDL("front")

    def RotateFaceR(self, key):
        if key=="front":
            self.RotateLD("right")
        elif key== "back":
            self.RotateLD("left")
        elif key=="left":
            self.RotateLD("front")
        elif key=="right":
            self.RotateRD("front")
        elif key=="top":
            self.RotateUR("front")
        elif key=="bottom":
            self.RotateDR("front")

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

rubiks_cube = CreateCube()
num_of_operations = 10
operations = [rubiks_cube.RotateLU,
               rubiks_cube.RotateLD,
               rubiks_cube.RotateRU,
               rubiks_cube.RotateRD,
               rubiks_cube.RotateUL,
               rubiks_cube.RotateUR,
               rubiks_cube.RotateDL,
               rubiks_cube.RotateDR,
               rubiks_cube.RotateFaceL,
               rubiks_cube.RotateFaceR]
for i in range(num_of_operations):
    choice_operation = random.choice(operations)
    choice_face = random.choice(list(rubiks_cube.color_pos.keys()))
    choice_operation(choice_face)
    print(choice_operation,choice_face)
    rubiks_cube.PrintCube()


rubiks_cube.PrintCube()
#back = rubiks_cube.GetFaceFromPos("back")
#front = rubiks_cube.GetFaceFromPos("front")
#print(rubiks_cube.faces[back].GetColor()) 
#print(rubiks_cube.faces[front].GetColor())
#print(rubiks_cube.faces[back].GetNodes()[0][0].GetColors()[0])
#print(rubiks_cube.faces[front].GetNodes()[0][0].GetColors()[0])
            
            
        