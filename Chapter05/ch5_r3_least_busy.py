#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020
Updated March 2023

@author: hassi
"""

from qiskit_ibm_provider import IBMProvider
from qiskit.providers.ibmq import least_busy

print("Ch 5: Least busy backend")
print("------------------------")

print("Getting provider...")
if not IBMProvider.active_account:
    print("Loading account")
    IBMProvider.load_account()
provider = IBMProvider()

# Finding the least busy backend
backend = least_busy(provider.backends(operational=True, simulator=False))
print("Least busy backend:", backend.name)

filtered_backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits = 5 and not x.configuration().simulator and x.status().operational==True))

print("\nLeast busy backend with more than one qubit:", filtered_backend.name)

from qiskit.tools.monitor import backend_overview
print("\nAll backends overview:\n")
backend_overview()  ## Throws error aise QiskitError("No backends available.")
