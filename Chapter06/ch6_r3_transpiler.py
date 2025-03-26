#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020
Verified March 2023, updated Feb 2025

@author: hassi
"""

#!/usr/bin/env python
# coding: utf-8

print("Loading Qiskit...")
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

#Optional: When running in an iPhyton environment
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


from qiskit_ibm_runtime import EstimatorV2 as Estimator

#################################################################
# Use the instance
################################################################# 

import os
from qiskit_ibm_runtime import QiskitRuntimeService
service = QiskitRuntimeService(channel="ibm_quantum", 
                                token=os.environ['IQP_API_TOKEN'])
backend = service.least_busy(simulator=False, operational=True)

# # Construct the Estimator instance.
# estimator = Estimator(mode=backend)
# estimator.options.resilience_level = 1
# estimator.options.default_shots = 5000

#################################################################
# Use the following code instead if you want to run on a simulator:
################################################################# 

# from qiskit_ibm_runtime.fake_provider import FakeAlmadenV2
# backend = FakeAlmadenV2()
# estimator = Estimator(backend)

print("Backend: ", backend.name)

#################### original
# Set service and select backend
# service = QiskitRuntimeService()
# service.backends()
# backend = service.least_busy(operational=True, simulator=False)
# print("Backend: ", backend.name)

# Uncomment to set the backend to a simulator
#backend = provider.get_backend('ibmq_qasm_simulator')

print("Ch 6: Transpiling circuits")
print("--------------------------")

# Print the basis gates and coupling map for the selected backend
print("Basis gates for:", backend)
print(backend.configuration().basis_gates)
print("Coupling map for:", backend)
print(backend.configuration().coupling_map)

def build_circuit(choice):
    # Create the circuit 
    qc = QuantumCircuit(5,5)
    
    if choice=="1":
        # Simple X
        qc.x(0)
    elif choice=="2":
        # Add H
        qc.x(0)
        qc.h(0)
    elif choice=="3":
        # H + Barrier
        qc.x(0)
        qc.barrier(0)
        qc.h(0)
    elif choice=="4":
        # Controlled Y (CY)
        qc.cy(0,1)
    elif choice=="5":    
        # Non-conforming CX
        qc.cx(0,4)
    else:
        # Multi qubit circuit
        qc.h(0)
        qc.h(3)
        qc.cx(0,4)
        qc.cswap(3,1,2)

    # Show measurement targets
    #qc.barrier([0,1,2,3,4])
    #qc.measure([0,1,2,3,4],[0,1,2,3,4])

    return(qc)



def main(): 
    choice="1"
    while choice !="0": 
        choice=input("Pick a circuit: \n1. Simple X\n2. Add H\n3. H + Barrier\n4. Controlled-Y\n5. Non-conforming CX\n6. Multi-gate\n")
        qc=build_circuit(choice) 
        # Create the transpiled circuit
        trans_qc = generate_preset_pass_manager(backend=backend, optimization_level=3).run(qc)
        
        # Print the original and transpiled circuits
        print("Circuit:")
        display(qc.draw())
        display(qc.draw("mpl"))
        print("Transpiled circuit:")
        display(trans_qc.draw("mpl", idle_wires=False))
        
        # Print the original and transpiled circuit depths
        print("Circuit depth:")
        print("---------------")
        print("Circuit:", qc.depth())
        print("Transpiled circuit:", trans_qc.depth())
        
        # Print the original and transpiled circuit sizes
        print("\nCircuit size:")
        print("---------------")
        print("Circuit:", qc.size())
        print("Transpiled circuit:", trans_qc.size())

if __name__ == '__main__':
    main()