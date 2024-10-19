from Classes.Node import Node

ROW = 3

class Face: 
    def __init__(self, nodes: Node, color):
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
