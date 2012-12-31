# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
 
  """
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
 
 
   #variable for whether or not goal has been reached
  reachedGoal=False
  exploredAll=False
  
  startState=problem.getStartState()
  
  exploredStatesDictionary=util.Counter()
  exploredStatesDictionary[0] = problem.getStartState()
  frontierDictionary=util.Counter()
  frontierList=problem.getSuccessors(problem.getStartState())
  #hash table for list of vertices as key
  vectorDictionary={}
  
  
 
  #create stack to hold the frontier states
  frontierQueue=util.Stack()
  #queue to hold list of actions
  #actionsQueue=util.Queue()
  actionsQueue=[]
  
  
  #push the frontier states onto the stack
  for i in frontierList:
   fNode=i
   frontierQueue.push(fNode)
   
  for i in frontierList:
    actionsThisFar=copy.deepcopy(actionsQueue)
    successor = str(i[0])
    vectorDictionary[successor]=actionsThisFar
    
  
  #key variable, key to exploredStatesDictionary
  seenAlready=1
  while reachedGoal==False:
   
   
   #get next state to explore, the first state from the stack
   #also save the action required to get to that point
   tempState=frontierQueue.pop()
   nextState=tempState[0]
   nextAction=tempState[1]
   
   #save the explored state
   exploredStatesDictionary[seenAlready] = nextState
   #save the action taken
   actionsQueue.append(nextAction)
   
   
   seenAlready = seenAlready+1
   
  
   #next state becomes current state
   if (exploredAll == True):
    inc=0
    otherInc=0
    
    
    
    reset = str(tempState[0])
    
    newActionsList = vectorDictionary[reset]
    newActionsList.append(tempState[1])
    
    #empty the old action list
    actionsQueue=copy.deepcopy(newActionsList)
   
   
   currentState=nextState
  
   #check if it is goal
   if (problem.isGoalState(currentState)):
    reachedGoal=True
	
   else:
    #the current state is not the goal
    #acquire the new frontier
    
    
    frontierList=problem.getSuccessors(currentState)
    for i in frontierList:
     actionsThisFar=copy.deepcopy(actionsQueue)
     successor = str(i[0])
     vectorDictionary[successor]=actionsThisFar
    		
    
    first = frontierList[0]
  
    #push the unexplored frontier states onto the queue
    
    explored=False
 
    counter=0
    
    
    
    for i in frontierList:
    
     #counter to keep track of iterations 
     explored=False
     exploredAll = False
     for k in exploredStatesDictionary:
      stateCo=exploredStatesDictionary[k]
      
      if ((i[0] == stateCo)): 
       
       explored = True
       counter = counter+1
       
       if(counter == ((len(frontierList)))):
        exploredAll = True
        
       
      elif ((explored == False) and (k == ((len(exploredStatesDictionary)))-1)):
        fNode = i
        frontierQueue.push(fNode)
       
    
  

  "*** YOUR CODE HERE ***"
  
  return actionsQueue
  
  util.raiseNotDefined()

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  
  #variable for whether or not goal has been reached
  reachedGoal=False
  exploredAll=False
  
  startState=problem.getStartState()
  
  #hash table to hold the explored states
  exploredStatesDictionary={}
  exploredStatesDictionary[0] = problem.getStartState() #insert the start state
  #hash table to hold the frontier
  frontierDictionary=util.Counter()
  frontierList=problem.getSuccessors(problem.getStartState()) #list to hold the successors
  """hash table for list of vertices as key
  	 holds cooridinates of each state as a key to the actions needed to reach that state
  """
  vectorDictionary={} 
  
 
  #create stack to hold the frontier states
  frontierQueue=util.Queue()
  
  #list of actions
  actionsQueue=[]
  #list to hold nodes that have been explored
  addedNodes = []
  
  
  #push the frontier states onto the stack
  for i in frontierList:
   fNode=i
   frontierQueue.push(fNode)
   addedNodes.append(fNode[0])
   
  
   
  for i in frontierList:
    actionsThisFar=copy.deepcopy(actionsQueue)
    successor = str(i[0])
    
    vectorDictionary[successor]=actionsThisFar
  
  #key variable, key to exploredStatesDictionary
  seenAlready=1
  iteration =0 
  
  "===============================entering the main while loop===================================="
  while reachedGoal==False:
    
   
   iteration= iteration + 1
   
   
   for i in addedNodes:
     
     popped=addedNodes.pop()
     exploredStatesDictionary[seenAlready] = popped
     seenAlready = seenAlready + 1
     
   
   tempState=frontierQueue.pop()
   
   
   nextState=tempState[0]
   
   nextAction=tempState[1]
   #save the explored state
   
   
   reset = str(tempState[0])
   
   "set a variable to the list of actions present in the dict where the key is tempState[0]"
   newActionsList = vectorDictionary[reset]
   "add the additional action required to take the path to the coordinates of nextState/tempState"
   newActionsList.append(nextAction)
   
   
   "set the running actionsQueue to the newly created list of actions"
   actionsQueue=copy.deepcopy(newActionsList)
   
   
   #length=len(actionsQueue)
   #if (length==19):
   
    #fgthe
   
   
   currentState=nextState
  
   "=======================goal state check============================"
   if (problem.isGoalState(currentState)):
    reachedGoal=True
	
   else:
    #the current state is not the goal
    #acquire the new frontier

    
    "acquiring the new frontier listbased on the current state"
    frontierList=problem.getSuccessors(currentState)
  
    
    
    for i in frontierList:
     explored=False
     counter = 0
 
     
     for k in exploredStatesDictionary:
       
      stateCo=exploredStatesDictionary[k]
  
      
      if ((i[0] == stateCo)): 
       
       explored = True
       counter = counter+1
       
       """
       if(counter == ((len(frontierList)))):
        exploredAll = True
       """
       
      elif ((explored == False) and (k == ((len(exploredStatesDictionary))-1))):
       
       """
       Should we insert a copy of the frontier node into the vector dictionary if we've already seen
       it? Where do we check that?
       """
       
       actionsThisFar=copy.deepcopy(actionsQueue)
       successor = str(i[0])
       
       """
       insert vector from frontier into the dictionary as a key to the actionsThis far which
       is a deep copy of the current actions queue at this point
       """
       vectorDictionary[successor]=actionsThisFar
       
      
    

       fNode = i
       
        
       frontierQueue.push(fNode)
      
       addedNodes.append(fNode[0])
       
        
      
        
  
    
  

  "*** YOUR CODE HERE ***"
  
  
  return actionsQueue
  
  
  util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  "*** YOUR CODE HERE ***"
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
 
 
   #variable for whether or not goal has been reached
  reachedGoal=False
  exploredAll=False
  previousCost = 0;
  
  startState=problem.getStartState()
  
  exploredStatesDictionary=util.Counter()
  exploredStatesDictionary[0] = problem.getStartState()
  frontierDictionary=util.Counter()
  frontierList=problem.getSuccessors(problem.getStartState())
  #hash table for list of vertices as key
  vectorDictionary={}
  
 
  #create stack to hold the frontier states
  frontierQueue=util.PriorityQueue()
  #queue to hold list of actions
  #actionsQueue=util.Queue()
  actionsQueue=[]
  
  addedNodes=[]
  """
  #push the frontier states onto the stack
  for i in frontierList:
   fNode=i
   frontierQueue.push(fNode,actionsQueue)
   """
   
  for i in frontierList:
    actionsThisFar=copy.deepcopy(actionsQueue)
    successor = str(i[0])
    vectorDictionary[successor]=actionsThisFar
   
  
  
  #push the frontier states onto the stack
  for i in frontierList:
    fNode=i
    frontierQueue.push(fNode,i[2])
    addedNodes.append(fNode[0])
  
  #key variable, key to exploredStatesDictionary
  seenAlready=1
  while reachedGoal==False:
    for i in addedNodes:
     
      popped=addedNodes.pop()
      exploredStatesDictionary[seenAlready] = popped
      seenAlready = seenAlready + 1
   

   
    #get next state to explore, the first state from the stack
    #also save the action required to get to that point
    tempState=frontierQueue.pop()
    previousCost = tempState[2]
    nextState=tempState[0]
  
    nextAction=tempState[1]
    
    #save the explored state
    exploredStatesDictionary[seenAlready] = nextState
    #save the action taken
    #actionsQueue.append(nextAction)
   
   
    seenAlready = seenAlready+1
    
  
    #next state becomes current state
   

    
    reset = str(tempState[0])

    
    newActionsList = vectorDictionary[reset]
    newActionsList.append(tempState[1])
   
  
    #empty the old action list
   
    actionsQueue=copy.deepcopy(newActionsList)
   
  
    currentState=nextState
  
    #check if it is goal
    
  	
    if (problem.isGoalState(currentState)):
      reachedGoal=True
	
    else:
      #the current state is not the goal
      #acquire the new frontier
    
    
      frontierList=problem.getSuccessors(currentState)
      for i in frontierList:
        explored=False
        counter=0
        for k in exploredStatesDictionary:
          stateCo=exploredStatesDictionary[k]
          
          if ((i[0] == stateCo)): 
           
            explored = True
            counter = counter+1
       
          elif ((explored == False) and (k == ((len(exploredStatesDictionary)))-1)):
              
      
            actionsThisFar=copy.deepcopy(actionsQueue)
            successor = str(i[0])
            vectorDictionary[successor]=actionsThisFar
            fNode = i
            newCost = i[2] + previousCost
            fNode=list(fNode)
            #update
            fNode[2]=newCost
            #back to tuple
            fNode=tuple(fNode)
            frontierQueue.push(fNode, newCost)
            addedNodes.append(fNode[0])
  
  
  
  "*** YOUR CODE HERE ***"
 
  length = len(actionsQueue)
  return actionsQueue
  
  
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0
  
  """
  copy and paste of manhattenHeuristic
  xy1 = position
  xy2 = problem.goal
  return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])
  """
  
def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  
 
 
   #variable for whether or not goal has been reached
    #variable for whether or not goal has been reached
  reachedGoal=False
  exploredAll=False
  previousCost = 0;
  
  startState=problem.getStartState()
  
  exploredStatesDictionary=util.Counter()
  exploredStatesDictionary[0] = problem.getStartState()
  frontierDictionary=util.Counter()
  frontierList=problem.getSuccessors(problem.getStartState())
  #hash table for list of vertices as key
  vectorDictionary={}
  

  
 
  #create stack to hold the frontier states
  frontierQueue=util.PriorityQueue()
  #queue to hold list of actions
  actionsQueue=[]
  
  addedNodes=[]
  """
  #push the frontier states onto the stack
  for i in frontierList:
   fNode=i
   frontierQueue.push(fNode,actionsQueue)
   """
   
  for i in frontierList:
    actionsThisFar=copy.deepcopy(actionsQueue)
    successor = str(i[0])
    vectorDictionary[successor]=actionsThisFar
   
  
  
  #push the frontier states onto the stack
  for i in frontierList:
    fNode=i
    frontierQueue.push(fNode,i[2])
    addedNodes.append(fNode[0])
  
  #key variable, key to exploredStatesDictionary
  seenAlready=1
  while reachedGoal==False:
    for i in addedNodes:
     
      popped=addedNodes.pop()
      exploredStatesDictionary[seenAlready] = popped
      seenAlready = seenAlready + 1
   

   
    #get next state to explore, the first state from the stack
    #also save the action required to get to that point
    tempState=frontierQueue.pop()
    previousCost = tempState[2]
    nextState=tempState[0]
  
    nextAction=tempState[1]
    
    #save the explored state
    exploredStatesDictionary[seenAlready] = nextState
    
    seenAlready = seenAlready+1

  
    #next state becomes current state
   

    #badNode = frontierQueue.pop()
    #firstNode = frontierQueue.pop()
    reset = str(tempState[0])

    #problem
    newActionsList = vectorDictionary[reset]
    newActionsList.append(tempState[1])
   
  
    #empty the old action list
   
    actionsQueue=copy.deepcopy(newActionsList)
   
  
    currentState=nextState
  
    #check if it is goal
    
  	
    if (problem.isGoalState(currentState)):
      reachedGoal=True
	
    else:
      #the current state is not the goal
      #acquire the new frontier
    
    
      frontierList=problem.getSuccessors(currentState)
      for i in frontierList:
        explored=False
        counter=0
        for k in exploredStatesDictionary:
          stateCo=exploredStatesDictionary[k]
         
          if ((i[0] == stateCo)): 
           
            explored = True
            counter = counter+1
       
          elif ((explored == False) and (k == ((len(exploredStatesDictionary)))-1)):
              
      
            actionsThisFar=copy.deepcopy(actionsQueue)
            successor = str(i[0])
            vectorDictionary[successor]=actionsThisFar
            fNode = i
            hCost=heuristic(i[0],problem)
            newCost = i[2] + previousCost + hCost
            fNode=list(fNode)
            #update
            fNode[2]=newCost
            #back to tuple
            fNode=tuple(fNode)
            frontierQueue.push(fNode, newCost)
            addedNodes.append(fNode[0])

  
  
  
  "*** YOUR CODE HERE ***"
  length = len(actionsQueue)
  return actionsQueue
  
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
