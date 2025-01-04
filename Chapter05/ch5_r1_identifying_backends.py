#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020
Updated Aug 2021, March 2023

@author: hassi
"""

from qiskit import QuantumCircuit, execute
from qiskit_ibm_provider import IBMProvider
from qiskit.tools.monitor import job_monitor

print("Ch 5: Identifying backends")
print("--------------------------")

print("Getting provider...")
if not IBMProvider.active_account:
    print("Loading account")
    IBMProvider.load_account()
provider = IBMProvider()

print("\nAvailable backends:")
print(provider.backends(operational=True, simulator=False))


select_backend=input("Type in the name of a backend: ")
backend = provider.get_backend(select_backend)
print("\nSelected backend:", backend.name)

# Create a quantum circuit to test
qc = QuantumCircuit(2,2)

qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])

print("\nQuantum circuit:")
print(qc)

job = execute(qc, backend, shots=1000)
job_monitor(job)

result = job.result()
counts = result.get_counts(qc)

print("\nResults:", counts)

print("\nAvailable simulator backends:")
print(provider.backends(operational=True, simulator=True))

backend = provider.get_backend('ibmq_qasm_simulator')
job = execute(qc, backend, shots=1000)
job_monitor(job)

result = job.result()
counts = result.get_counts(qc)

print("\nSimulator results:", counts) 





