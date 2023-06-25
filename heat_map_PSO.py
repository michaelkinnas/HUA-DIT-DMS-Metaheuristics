import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("/home/mike/HUA/DecissionMakingSystems/results_PSO.csv")

# x = np.array(data['population'].values)
# y = np.array(data['max_iteration'].values)
# z = np.array(data['satisfaction'].values)

x = list(data['population'].values)
y = list(data['max_iteration'].values)
z = list(data['satisfaction'].values)

z1=[]
for i in range(0, len(z), 10):
    total = 0    
    for j in range(i, i+10):
        total += z[j]
    z1.append(total/10)  


x = [x for x in range(50,1050, 50)]
y = [x for x in range(50,1050, 50)]
y.reverse()
z1_2d = []
for i in range(20):   
    mazema = []
    for j in range(i*20, i*20+20):
        mazema.append(z1[j])
    
    z1_2d.append(mazema)


z1_2d.reverse()


fig, ax = plt.subplots()
im = ax.imshow(z1_2d)
print(len(z1_2d))

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(x)), labels=x)
ax.set_yticks(np.arange(len(y)), labels=y)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")



z1_2d = np.array(z1_2d)

# Loop over data dimensions and create text annotations.
for i in range(len(y)):
    for j in range(len(x)):
        text = ax.text(j, i, z1_2d[i, j], ha="center", va="center")

ax.set_xlabel('Population (step of 50)')
ax.set_ylabel('Iteration (step of 50)')
ax.set_title("Level of user satisfaction for given PSO parameter combinations (average for 10 iterations)")
fig.tight_layout()
plt.show()