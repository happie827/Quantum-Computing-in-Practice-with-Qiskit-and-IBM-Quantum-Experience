#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, updated Jan 2025

@author: hassi
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer.primitives import Sampler
from qiskit.visualization import plot_distribution

from IPython.display import display

print("Ch 4: Upside down quantum coin toss")
print("-----------------------------------")


qc = QuantumCircuit(1, 1)
initial_vector = [0.+0.j, 1.+0.j]
qc.initialize(initial_vector,0)

#qc.x(0)
qc.h(0)
qc.measure(0, 0)

print(qc)
#display(qc.draw())

# Run the simple quantum circuit on local Sampler 
job = Sampler().run([qc])
quasi_dists = job.result().quasi_dists
counts = quasi_dists[0].binary_probabilities()

#Plot the results
display(plot_distribution(counts))

print(counts)