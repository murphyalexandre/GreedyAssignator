'''
Created on 2012-07-31

@author: Alexandre Murphy-Gonthier <murphyalexandre@gmail.com>

This is a subproblem of the knapsack problem. Maybe a combination of the bin packing and knapsack. 
We use an approach of assigning bigger machines to bigger servers and assigning machines to servers
that are below the usage threshold that we have set to other servers.
'''

from Machine import *
from Server import *
import operator

def greedy(s, v):
    # Sort server list
    s.sort(key=operator.attrgetter("cases"), reverse=True)
    
    # Sort machine list
    v.sort(key=operator.attrgetter("cases"), reverse=True)
    
    thresholdRange = 0.1
    threshold = thresholdRange
    sId = 0
    
    # Until there's no machine left
    while v :
        currentServer = s[sId]
        currentMachine = v.pop(0)
        
        # If we have space on this server
        if currentServer.usage <= threshold-thresholdRange :
            # Add machine
            currentServer.addVM(currentMachine)
            
            # Update threshold if necessary
            if currentServer.usage > threshold :
                threshold = currentServer.usage
            
            # Change server if above a threshold
            if currentServer.usage > threshold-thresholdRange:
                # Update id
                sId = sId+1
                if sId >= len(s): sId = 0
                
def printResults(s):
    for server in s:
        print str(server)
        
def printJSON(s):
    serverList = []
    for server in s:
        serverList.append(server.toJSON())
    print {"serveurs":serverList}
        
def main():
    data = {"serveurs":[{"id":"serveur1","cases":4},{"id":"serveur2","cases":6}],"machineVirtuelles":[{"id":"VM1","cases":1},{"id":"VM2","cases":4},{"id":"VM3","cases":2}]}
    
    # Better test
    #data = {"serveurs":[{"id":"serveur1","cases":6},{"id":"serveur2","cases":7},{"id":"serveur3","cases":5},{"id":"serveur4","cases":12}],"machineVirtuelles":[{"id":"VM1","cases":1},{"id":"VM2","cases":4},{"id":"VM3","cases":2},{"id":"VM4","cases":5},{"id":"VM5","cases":1},{"id":"VM6","cases":3},{"id":"VM7","cases":2},{"id":"VM8","cases":7}]}
    
    # Parse input data
    # This could be parsed using JSON
    inputServeurs = data.get("serveurs")
    inputVM = data.get("machineVirtuelles")
    
    # Create server objects
    servers = []
    for s in inputServeurs :
        servers.append(Server(s.get("id"), s.get("cases")))
        
    # Create VM objects
    vms = []
    for v in inputVM :
        vms.append(Machine(v.get("id"), v.get("cases"))) 
        
    # REMINDER: Python uses parameters by reference, need to make copies
    # if we call more than one algorithm
    greedy(servers, vms)
    
    #printResults(servers)
    printJSON(servers)

if __name__ == '__main__':
    main()
    