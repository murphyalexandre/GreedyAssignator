'''
Created on 2012-07-31

@author: Alexandre Murphy-Gonthier <murphyalexandre@gmail.com>
'''

class Machine(object):
    '''
    classdocs
    '''

    def __init__(self, idMachine, cases):
        '''
        Constructor
        '''
        self.idMachine = idMachine;
        self.cases = cases;
        
    def __str__(self):
        return "Virtual Machine: id={0} cases={1}".format(self.idMachine, self.cases)
    
    def toJSON(self):
        return {"id":self.idMachine, "cases":self.cases}
        