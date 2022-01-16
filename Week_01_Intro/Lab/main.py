# You can use this main file to run your code

S = np.array([
    [90,0,95],
    [0,96,0],
    [95,0,-50]]) 

plt.figure()
model = mohr()
R_maj, R_min, R_mid = model.plot_mohr3d(S2)
print(R_maj, R_min, R_mid)
plt.show()
