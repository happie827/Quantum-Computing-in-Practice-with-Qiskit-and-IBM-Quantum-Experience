#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, updated Feb 2025

@author: hassi
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer.primitives import Sampler
from qiskit.visualization import plot_distribution

IPYTHON = False
if IPYTHON:
    from IPython.display import display
else : 
    import matplotlib
    matplotlib.use('TkAgg')  #sudo apt install python3-tk # 또는 'Qt5Agg'도 가능 #
    import matplotlib.pyplot as plt
    def display(job):
        fig = job
        plt.show()


print("Ch 4: Quantum coin tosses")
print("-------------------------")

q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q, c)

qc.x(0)
qc.h(q[0])
qc.measure(q, c)

if IPYTHON:
    display(qc.draw('mpl'))
else:
    fig = qc.draw('mpl')
    plt.show()


# Run the simple quantum circuit on local Sampler 
job = Sampler().run([qc])
quasi_dists = job.result().quasi_dists
counts = quasi_dists[0].binary_probabilities()

#Plot the results
display(plot_distribution(counts))

print("\nSampler: ", counts)


# Alternatively run on Aersimulator        
from qiskit import transpile
from qiskit_aer import AerSimulator

# Transpile for simulator
simulator = AerSimulator(shots=2048)
circ = transpile(qc, simulator)

# Run and get counts
result = simulator.run(circ).result()
counts = result.get_counts(circ)

display(plot_distribution(counts))
print("\nAerSimulator counts: ", counts)


