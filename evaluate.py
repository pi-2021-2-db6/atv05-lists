"""
Testes automaticos de corretude.

NAO EDITAR ESTE ARQTUIVO.
"""

import unittest
import os

import solutions

class AllTests(unittest.TestCase):        
    
    def test_conta_unicos(self):
        path = os.path.join("data", "conta_unicos.csv")
        message = "\nResultado fora do esperado:\n Entrada: %s \n Esperado: %s \n Obtido: %s"
        border_cases = [[0, []], [1, [0]], [2, [1, 3]], [1, [2, 2, 2, 2, 2, 2]]]
        
        for case in border_cases:
            act = solutions.conta_unicos(case[1])
            self.assertEqual(case[0], act, message % (case[1], case[0], act))
        with open(path, "r") as file:
            for case in file:
                data = [int(x) for x in case.split()]
                size = data.pop(0)
                inp = []
                for i in range(size):
                    inp.append(data.pop(0))
                exp = data.pop(0)
                act = solutions.conta_unicos(inp)
                self.assertEqual(exp, act, message % (inp, exp, act))
                
    def test_matriz_diagonal(self):
        path = os.path.join("data", "matriz_diagonal.csv")
        message = "\nResultado fora do esperado:\n Entrada: %s \n Esperado: %s \n Obtido: %s"
        border_cases = [ [[], False], 
                         [[[1]], True], 
                         [[[1]], True], 
                         [[[0]], False],
                         [[[0,1], [1, 0]], False],
                         [[[1,1], [1,1]], False],
                         [[[0,0], [0,0]], False],
                         [[[1, 0, 0], [0, 1, 0]], False],
                         [[[1, 0]], False] ]
        
        for case in border_cases:
            act = solutions.matriz_diagonal(case[0])
            self.assertEqual(case[1], act, message % (case[0], case[1], act))
        
        with open(path, "r") as file:
            for case in file:
                data = case.split()
                l = int(data.pop(0))
                inp = []
                
                for i in range(l):
                    inp.append([])
                    for j in range(l):
                        inp[i].append(int(data.pop(0)))
                        
                exp = data.pop(0)
                exp = True if exp == "True" else False
                act = solutions.matriz_diagonal(inp)
                
                self.assertEqual(exp, act, message % (inp, exp, act))
            
if __name__ == "__main__":
    unittest.main()