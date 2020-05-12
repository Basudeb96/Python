'''
Created on May 12, 2020

@author: basudeb
'''
import Graph as G

def main():
    n = int(input("Enter the no. of vertices: "))
    g = G.Graph(n)
    g.Create_graph()
    u, v = input("Enter the end vertices").split(" ")
    g.Add_edges(u, v)
    
if __name__ == "__main__":
    main()