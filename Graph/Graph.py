'''
Created on May 12, 2020

@author: basudeb
'''

class Graph:
    def __init__(self, temp):
        self.n = temp
        self.ver = [str(0) for _ in range(self.n)]
        self.adjacency_list = [[str(0) for _ in range(self.n+1)] for _ in range(self.n+1)]
    
    def Create_graph(self):
        print("Enter the name of the vertices: ")
        i = 0
        for i in range(0,self.n):
            self.ver[i] = str(input())
        i = 0
        e = input("Enter the total to  of edges: ")
        for i in range(self.n):
            self.adjacency_list[0][i+1] = self.ver[i]
            self.adjacency_list[i+1][0] = self.ver[i]
        
        for i in range(int(e)):
            u, v = input("Enter the end vertices: ").split(" ")
            self.Add_edges(u, v)
        self.Show_Adjacency_list()

    def Add_edges(self, u, v):
        flag1 = False
        flag2 = False
        for j in range(self.n):
            if(self.ver[j] == u):
                index1 = j+1
                flag1 = True
            if(self.ver[j] == v):
                index2 = j+1
                flag2 = True
        if(flag1 and flag2):
            self.adjacency_list[index1][index2] = str(1)
            self.adjacency_list[index2][index1] = str(1)
    
    def Show_Adjacency_list(self):
        print("\n".join(['\t'.join([item for item in row]) for row in self.adjacency_list]))