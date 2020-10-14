import epyc
import epydemic
from epydemic import CompartmentedModel
import networkx

class SIR(CompartmentedModel):

    # the possible dynamics states of a node for SIR dynamics
    SUSCEPTIBLE = 'S'
    INFECTED = 'I'
    REMOVED = 'R'

    # the model parameters
    P_INFECTED = 'pInfected'
    P_INFECT = 'pInfect'
    P_REMOVE = 'pRemove'

    # the edges at which dynamics can occur
    SI = 'SI'

    def build( self, params ):
        pInfected = params[self.P_INFECTED]
        pInfect = params[self.P_INFECT]
        pRemove = params[self.P_REMOVE]

        self.addCompartment(self.INFECTED, pInfected)
        self.addCompartment(self.REMOVED, 0.0)
        self.addCompartment(self.SUSCEPTIBLE, 1 - pInfected)

        self.trackNodesInCompartment(self.INFECTED)
        self.trackEdgesBetweenCompartments(self.SUSCEPTIBLE, self.INFECTED, name=self.SI)

        self.addEventPerElement(self.SI, pInfect, self.infect)
        self.addEventPerElement(self.INFECTED, pRemove, self.remove)

    def infect( self, t, e ):
        (n, m) = e
        self.changeCompartment(n, self.INFECTED)
        self.markOccupied(e, t)

    def remove( self, t, n ):
        self.changeCompartment(n, self.REMOVED)

# parameters
param = dict()
param[SIR.P_INFECT] = 0.2     # infection probability
param[SIR.P_REMOVE] = 0.5     # removal probability
param[SIR.P_INFECTED] = 0.01  # initial seeding probability

# create the network
N = 10000                 # order (number of nodes) of the network
kmean = 5                 # mean node degree
phi = (kmean + 0.0) / N   # probability of attachment between two nodes chosen at random
g = networkx.erdos_renyi_graph(N, phi)

# create a model and a dynamics to run it
m = SIR()                               # the model (process) to simulate
e = epydemic.StochasticDynamics(m, g)   # use stochastic (Gillespie) dynamics

# set the parameters we want and run the simulation
rc = e.set(param).run()

print(rc[epyc.Experiment.RESULTS])