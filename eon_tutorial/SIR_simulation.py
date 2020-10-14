import networkx as nx
import EoN
import matplotlib.pyplot as plt

N = 10**6 # number of individuals
kave = 5 # expected number of partners
print("Generating graph G with {} nodes".format(N))
G = nx.fast_gnp_random_graph(N, kave/(N-1)) # Erdos-Renyi graph

rho = 0.005 # initial fraction infected
tau = 0.3 # transmission rate
gamma = 1.0 # recovery rate

print("Doing event-based simulation")
t1, S1, I1, R1 = EoN.fast_SIR(G, tau, gamma, rho=rho)
# instead of rho, we could specify a list of nodes as initial_infecteds, or
# specify neither and a single random node would be chosen as the index case

print("Doing Gillespie simulation")
t2, S2, I2, R2 = EoN.Gillespie_SIR(G, tau, gamma, rho=rho)

print("Done with simulations, now plotting")
plt.plot(t1, I1, label = "fast_SIR")
plt.plot(t2, I2, label = "Gillespie_SIR")
plt.xlabel("$t$")
plt.ylabel("Number infected")
plt.legend()
# plt.show()
plt.savefig("/project/plots/epidemic.png")
