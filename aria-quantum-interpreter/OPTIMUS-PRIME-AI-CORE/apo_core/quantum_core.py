"""
Quantum Core: Qiskit/Cirq Quantum Circuit Builder/Executor
Copyright (c) 2025 Paul Morales, Alpha Pi Omega Corp (alphapiomega.com)
"""

try:
    from qiskit import QuantumCircuit, Aer, execute
    QISKIT_AVAILABLE = True
except ImportError:
    QISKIT_AVAILABLE = False

class QuantumCore:
    def create_bell_circuit(self):
        if not QISKIT_AVAILABLE:
            return None
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])
        return qc

    def execute_circuit(self, circuit, shots=1024):
        if not QISKIT_AVAILABLE or circuit is None:
            return {"error": "Qiskit not available or circuit invalid"}
        backend = Aer.get_backend('qasm_simulator')
        job = execute(circuit, backend, shots=shots)
        result = job.result()
        counts = result.get_counts()
        return {"counts": counts}
