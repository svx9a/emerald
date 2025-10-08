cd /d "%USERPROFILE%\Desktop\quantum_dominance"
echo from qiskit import QuantumCircuit > command_centre.py
echo from qiskit_aer import Aer >> command_centre.py
echo import datetime >> command_centre.py
echo import os >> command_centre.py
echo. >> command_centre.py
echo class QuantumCommandCentre: >> command_centre.py
echo     def __init__(self): >> command_centre.py
echo         self.location = r"C:\Users\Administrator\Desktop\quantum_dominance" >> command_centre.py
echo         self.status = "ACTIVE" >> command_centre.py
echo         self.quantum_power = "MAXIMUM" >> command_centre.py
echo. >> command_centre.py
echo     def demon_spell(self, qubits=4): >> command_centre.py
echo         qc = QuantumCircuit(qubits) >> command_centre.py
echo         qc.h(0) >> command_centre.py
echo         for i in range(qubits-1): >> command_centre.py
echo             qc.cx(i, i+1) >> command_centre.py
echo         qc.x(0) >> command_centre.py
echo         qc.z(qubits-1) >> command_centre.py
echo         qc.measure_all() >> command_centre.py
echo         return qc >> command_centre.py
echo. >> command_centre.py
echo     def execute_spell(self, qc, shots=1024): >> command_centre.py
echo         return Aer.get_backend('qasm_simulator').run(qc, shots=shots).result().get_counts() >> command_centre.py
echo. >> command_centre.py
echo     def status_report(self): >> command_centre.py
echo         print("🚀 QUANTUM COMMAND CENTRE STATUS") >> command_centre.py
echo         print("📍 Location:", self.location) >> command_centre.py
echo         print("⚡ Status:", self.status) >> command_centre.py
echo         print("💀 Quantum Power:", self.quantum_power) >> command_centre.py
echo         print("⏰ Online since:", datetime.datetime.now()) >> command_centre.py
echo. >> command_centre.py
echo centre = QuantumCommandCentre() >> command_centre.py
echo centre.status_report() >> command_centre.py
echo print() >> command_centre.py
echo print("🎯 Testing demon spell...") >> command_centre.py
echo qc = centre.demon_spell(5) >> command_centre.py
echo results = centre.execute_spell(qc, 2048) >> command_centre.py
echo print("📊 Spell Results:", results) >> command_centre.py
echo print() >> command_centre.py
echo print("🌌 QUANTUM COMMAND CENTRE: OPERATIONAL") >> command_centre.py