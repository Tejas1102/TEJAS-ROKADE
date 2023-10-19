import numpy as np
import matplotlib.pyplot as plt

# Parameters
k = 0.1  # BOD removal rate constant
inflow_BOD = 100  # Initial BOD in the influent
time = np.arange(0, 10, 0.1)  # Time from 0 to 10 days

# Initialize lists to store BOD values at different time points
effluent_BOD = []

# Simulate BOD removal over time
for t in time:
    removal = k * inflow_BOD
    outflow_BOD = inflow_BOD - removal
    effluent_BOD.append(outflow_BOD)
    inflow_BOD = outflow_BOD  # Update the influent BOD for the next time step

# Plot the results
plt.plot(time, effluent_BOD)
plt.xlabel('Time (days)')
plt.ylabel('Effluent BOD')
plt.title('Effluent BOD over Time')
plt.grid(True)
plt.show()
