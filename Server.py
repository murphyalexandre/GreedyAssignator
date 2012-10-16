'''
Created on 2012-07-31

@author: Alexandre Murphy-Gonthier <murphyalexandre@gmail.com>
'''

from __future__ import division

class Server(object):
    '''
    classdocs
    '''

    def __init__(self, idServer, cases):
        '''
        Constructor
        '''
        self.idServer = idServer
        self.cases = cases
        self.casesUsed = 0
        self.usage = 0.0
        self.machines = []
        
    def addVM(self, machine):
        if(not machine.cases == 0 and self.cases >= self.casesUsed+machine.cases):
            self.machines.append(machine)
            self.casesUsed += machine.cases
            self.usage = self.casesUsed / self.cases
        
    def __str__(self):
        string = ""
        string += "Server: id={0}, cases={1}, usage={2}".format(self.idServer, self.cases, self.usage)
        if len(self.machines) > 0: string += " has these machines {"
        for m in self.machines :
            string += "{0}, ".format(str(m))
        if len(self.machines) > 0: string += "}"
        
        return string
    
    def toJSON(self):
        dictionary = {"id":self.idServer, "cases":self.cases, "pourcentageUtilisation":self.usage}
        machineList = []
        for machine in self.machines:
            machineList.append(machine.toJSON())
        dictionary['machinesVirtuelles'] = machineList
        return {"id":self.idServer, "cases":self.cases, "pourcentageUtilisation":self.usage, "machinesVirtuelles": machineList}
        