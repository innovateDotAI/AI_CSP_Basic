# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 23:08:58 2021

@author: Admin
"""
def nextNodeToallocate(allocation,constrain_node_dict):
    allocation_temp = constrain_node_dict
    for val in allocation:
        if allocation[val] != 'Empty':
            try:
                allocation_temp.pop(val)
            except:
                pass
    max_constrained_node = max(allocation_temp, key=allocation_temp.get)
    # Check if multipal value selected as max
    return max_constrained_node

def Constraint_dict(state_variable,problem_graph):
    #Allocat higest constrained node first
    nodeConstrain = dict()
    for i in state_variable:
        constrain = 0
        for j in problem_graph:
            if j[0] == i and len(j) == 2:
                constrain+=1
        nodeConstrain[i] = constrain
    return nodeConstrain

def constraintValidation(allocation,problem_graph):
    for i in problem_graph:
        #Neighbour node must not have same colour
        if len(i) >1 and allocation[i[0]] != 'Empty':
            if allocation[i[0]] == allocation[i[1]]:
                return False
    return True
    
def allocationNode(node,domain,allocation,problem_graph):
    for i in domain:
        allocation[node] = i
        consReturn = constraintValidation(allocation,problem_graph)
        if consReturn is True:
            return True,allocation
    return False, allocation


if __name__=="__main__":
    problem_graph = [['F'],['O','A'],['O','B'],['O','C'],['O','D'],['O','E'],['A','O'],['B','O'],['C','O'],['D','O'],['E','O'],['A','B'],['B','C'],['C','D'],['D','E'],['E','D'],['D','C'],['C','B'],['B','A']]
    state_variable = ['A','B','C','D','E','O','F']
    domain = ['Red','Yellow','Green']
    allocation_dict = dict.fromkeys(state_variable, "Empty")
    # Constraint= No two adjisent state have same colour.
    #allocation_dict = allocation_initial
    constrain_node_dict = Constraint_dict(state_variable,problem_graph)
    allocation_return = True
            
    while allocation_return is True:
        node = nextNodeToallocate(allocation_dict, constrain_node_dict)
        allocation_return, allocation_dict = allocationNode(node, domain, allocation_dict, problem_graph)
        # Goal Test by minimize count value
        count = len(state_variable)
        for val in allocation_dict:
            if allocation_dict[val] != 'Empty':
                count-=1
        if count == 0:
            print(allocation_dict)
            break
        else:
            pass
    
    
    