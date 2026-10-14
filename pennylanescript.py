import pennylane as qp

if __name__ == "__main__":
    # Create a quantum device with 2 qubits
    dev = qp.device("default.qubit", wires=2)

    # Define a quantum circuit
    @qp.qnode(dev)
    def circuit(params):
        qp.RX(params[0], wires=0)
        qp.RY(params[1], wires=1)
        qp.CNOT(wires=[0, 1])
        return qp.expval(qp.PauliZ(0)), qp.expval(qp.PauliZ(1))

    # Set parameters for the circuit
    params = [0.5, 0.5]

    # Execute the circuit and get the results
    results = circuit(params)
    print("Results:", results)