ROW = 3

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
    def Rotate(self,nodes, direction):
        if direction == "L":
            for i in range(ROW):
                self.nodes[i][0] = nodes[i]
        elif direction == "R":
            for i in range(ROW):
                self.nodes[i][2] = nodes[i]
        elif direction == "U":
            self.nodes[0] = nodes
        elif direction == "D":
            self.nodes[2] = nodes
        elif direction == "RotL":
            pass
            #self.nodes[0][0], self.nodes[0][1], self.nodes[0][2],self.nodes[1][2], self.nodes[2][2], self.nodes[2][0],self.nodes[2][1], self.nodes[1][0] = 

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
    def ChangeFront(self, color):
        for key in self.color_pos:
            if self.color_pos[key] == color:
                if key == "top":
                    self.color_pos["front"],self.color_pos["back"],self.color_pos["top"],self.color_pos["bottom"] = self.color_pos["top"],self.color_pos["bottom"],self.color_pos["front"],self.color_pos["back"]
                elif key == "bottom":
                    self.color_pos["front"],self.color_pos["back"],self.color_pos["top"],self.color_pos["bottom"] = self.color_pos["bottom"],self.color_pos["top"],self.color_pos["back"],self.color_pos["front"]
                elif key == "left":
                    self.color_pos["front"],self.color_pos["back"],self.color_pos["left"],self.color_pos["right"] = self.color_pos["left"],self.color_pos["right"],self.color_pos["front"],self.color_pos["back"]
                elif key == "right":
                    self.color_pos["front"],self.color_pos["back"],self.color_pos["left"],self.color_pos["right"] = self.color_pos["right"],self.color_pos["left"],self.color_pos["back"],self.color_pos["front"]
                elif key == "back":
                    self.color_pos["front"],self.color_pos["back"],self.color_pos["left"],self.color_pos["right"] = self.color_pos["back"],self.color_pos["front"],self.color_pos["right"],self.color_pos["left"]
                break
            
    def GetFaceFromPos(self,pos):
        for key,value in self.color_pos:
            if key == pos:
                for i in range(len(self.faces)):
                    if value == self.faces[i].GetColor():
                        return i
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

    def RotateLU(self, color):
        self.ChangeFront(color)
        FRONT = self.GetFaceFromPos("front")
        TOP = self.GetFaceFromPos("top")
        BOTTOM = self.GetFaceFromPos("bottom")
        LEFT = self.GetFaceFromPos("left")
        RIGHT = self.GetFaceFromPos("right")

        for i in range(ROW):
            self.faces[FRONT].GetNodes()[i][0], #the intent was to rotate the same way i change front 

def CreateCube():
    faces = []
    rubiks_cube = Cube([0,0,0,0,0,0])
    for i in range(6):
        face = Face([[0,0,0],
                    [0,0,0],
                    [0,0,0]], rubiks_cube.all_colors[i])
        if i>0:
            rubiks_cube.ChangeFront(rubiks_cube.all_colors[i])
        for j in range(ROW):
            if j == 0:
                #vertical then horizontal for corners
                face.nodes[j][0] = Node([rubiks_cube.color_pos["front"], rubiks_cube.color_pos["top"], rubiks_cube.color_pos["left"]],2)
                face.nodes[j][1] = Node([rubiks_cube.color_pos["front"], rubiks_cube.color_pos["top"]], 1)
                face.nodes[j][2] = Node([rubiks_cube.color_pos["front"], rubiks_cube.color_pos["top"], rubiks_cube.color_pos["right"]], 2)
            elif j == 1:
                face.nodes[j][0] = Node([rubiks_cube.color_pos["front"], rubiks_cube.color_pos["left"]],1)
                face.nodes[j][1] = Node([rubiks_cube.color_pos["front"]], 0)
                face.nodes[j][2] = Node([rubiks_cube.color_pos["front"], rubiks_cube.color_pos["right"]], 1)
            elif j == 2:
                #vertical then horizontal for corners
                face.nodes[j][0] = Node([rubiks_cube.color_pos["front"], rubiks_cube.color_pos["bottom"], rubiks_cube.color_pos["left"]],2)
                face.nodes[j][1] = Node([rubiks_cube.color_pos["front"], rubiks_cube.color_pos["bottom"]], 1)
                face.nodes[j][2] = Node([rubiks_cube.color_pos["front"], rubiks_cube.color_pos["bottom"], rubiks_cube.color_pos["right"]], 2)
        faces.append(face)
    rubik = Cube(faces)
    return rubik

rubiks_cube = CreateCube()
rubiks_cube.PrintCube()
print(rubiks_cube.faces[5].GetNodes()[0][0].GetColors()[0]) 
        
            
            
        