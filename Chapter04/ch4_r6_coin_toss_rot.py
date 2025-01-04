#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, updated Jan 2025 <-Pending

@author: hassi
"""

from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from qiskit.visualization import plot_distribution

from IPython.display import display

from math import pi

# Function that returns the state vector (Psi) for the circuit
def get_psi(circuit, title):
    show_bloch=True
    if show_bloch:
        from qiskit.visualization import plot_bloch_multivector
        backend = Aer.get_backend('statevector_simulator') 
        result = execute(circuit, backend).result()
        psi = result.get_statevector(circuit)
        print(title)
        display(qc.draw('mpl'))
        display(plot_bloch_multivector(psi)) 


print("Ch 4: More Cheating quantum coin toss")
print("-------------------------------------")

qc = QuantumCircuit(1, 1)

get_psi(qc, title='Qubit in ground state |0>')
qc.h(0)
get_psi(qc, title='Qubit in super position')
qc.ry(pi/8,0)
get_psi(qc, title='Qubit pi/8 radians closer to |1>') 
qc.measure(0, 0)

display(qc.draw('mpl'))

# Run the simple quantum circuit on local Sampler 
job = Sampler().run([qc])
quasi_dists = job.result().quasi_dists
counts = quasi_dists[0].binary_probabilities()

#Plot the results
display(plot_distribution(counts))

print(counts)