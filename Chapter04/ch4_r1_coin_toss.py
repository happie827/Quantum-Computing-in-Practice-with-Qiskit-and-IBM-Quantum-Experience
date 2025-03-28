#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, updated Feb 2025

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

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


print("Ch 4: Quantum coin toss")
print("-----------------------")

q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.measure(q, c)

print(qc) #display(qc.draw('text'))

#Show the circuit
fig = qc.draw('mpl')
display(fig)


#####################################
# Run the simple quantum circuit on local Sampler 
#####################################
from qiskit_aer.primitives import Sampler
from qiskit.visualization import plot_distribution

job = Sampler().run([qc])
quasi_dists = job.result().quasi_dists
counts = quasi_dists[0].binary_probabilities()

#Plot the results
print("\nSampler: ", counts)
display(plot_distribution(counts))

# #####################################
# # Alternatively run on Aersimulator
# #####################################        
from qiskit import transpile
from qiskit_aer import AerSimulator

# Transpile for simulator
simulator = AerSimulator()
circ = transpile(qc, simulator)

# Run and get counts
result = simulator.run(circ).result()
counts = result.get_counts(circ)

print("\nAerSimulator counts: ", counts)
display(plot_distribution(counts))


