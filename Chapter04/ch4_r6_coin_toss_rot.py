#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, updated Jan 2025

@author: hassi
"""
IPYTHON = False
if IPYTHON:
    from IPython.display import display
else : 
    import matplotlib
    matplotlib.use('TkAgg')  #sudo apt install python3-tk # 또는 'Qt5Agg'도 가능 #
    import matplotlib.pyplot as plt
    def display(job):
        plt.show()


from qiskit import QuantumCircuit, transpile
from qiskit_aer.primitives import Sampler
from qiskit.visualization import plot_distribution, plot_bloch_multivector
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

from math import pi

# Function that returns the state vector (Psi) for the circuit
def get_psi(circuit, title):
    show_bloch=True
    if show_bloch:
        psi = Statevector(circuit)
        print(title)

        # fig = psi.draw(output = 'latex')
        # display(fig)
        # fig = circuit.draw('mpl')
        # display(fig)
        fig = plot_bloch_multivector(psi)
        display(fig)        

        # if IPYTHON:
        #     display(psi.draw(output = 'latex'))
        #     display(circuit.draw('mpl'))
        #     display(plot_bloch_multivector(psi)) 
        # else:
        #     fig = psi.draw(output = 'latex')
        #     plt.show()
        #     fig = circuit.draw('mpl')
        #     plt.show()
        #     fig = plot_bloch_multivector(psi)
        #     plt.show()
        
        

print("Ch 4: More Cheating quantum coin toss")
print("-------------------------------------")

qc = QuantumCircuit(1, 1)
# get_psi(qc, 'Qubit in ground state |0>')
        
qc.h(0)
# get_psi(qc, 'Qubit in super position')

qc.ry(pi/8,0)
# get_psi(qc, 'Qubit pi/8 radians closer to |1>') 
qc.measure(0, 0)

fig = qc.draw('mpl')
display(fig)


# Run the simple quantum circuit on local Sampler 
job = Sampler().run([qc])
quasi_dists = job.result().quasi_dists
counts = quasi_dists[0].binary_probabilities()

#Plot the results
print("\nSampler: ", counts)

fig = plot_distribution(counts)
display(fig)



# Transpile for simulator
simulator = AerSimulator()
circ = transpile(qc, simulator)

# Run and get counts
result = simulator.run(circ).result()
counts = result.get_counts(circ)

fig = plot_distribution(counts)
display(fig)
print("\nAerSimulator counts: ", counts)
