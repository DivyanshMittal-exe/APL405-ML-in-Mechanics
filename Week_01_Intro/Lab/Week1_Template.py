
"""
Mohr circle in 3D.
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigvalsh
from matplotlib import rcParams
 
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

class mohr():
  def plot_mohr3d(self, S):
    """Plot 3D Mohr circles."""
    ''' This method "plot_mohr3d()" definition should evaluate the principal stress components from any arbitrary stress tensor(S).
        Then, calculate major, minor and intermediate radius of Mohr's circle.'''
    
    #-------Your Code-------- 
    
    # Write func to calculate Eigen values of the stress tensor in increasing order of magnitude i.e. Principal Stresses in this line.

    # R_maj =                #Major radius
    # cent_maj =             #Centre of the major circle
    
    #R_min =                 #Minor Radius
    #cent_min =              #Centre of the minor circle
    
    #R_mid =                 #Intermediate (Radius of circle which includes both major and minor circle)
    #cent_mid = 
    
    # Plot your FIGURE of Mohr circle

    eigVals = eigvalsh(S)
    # eigVals = np.sort(eigVals) 
    s1 = eigVals[2]
    s2 = eigVals[1]
    s3 = eigVals[0]
    
    # print(s1,s2,s3)

    r1 = (abs(s2-s3))/2
    r2 = (abs(s1-s3))/2
    r3 = (abs(s1-s2))/2
        
    R_list = [r1,r2,r3]
    
    R_list = np.sort(R_list)
    
    R_min = R_list[0]
    R_mid = R_list[1]
    R_maj = R_list[2]
    
    l1 = (s2+s3)/2
    l2 = (s1+s3)/2
    l3 = (s1+s2)/2

    # R_maj = (s2-s3)/2
    # R_min = (s1-s3)/2
    # R_mid = (s1-s2)/2
    
    # cent_maj = (s2+s3)/2
    # cent_min = (s1+s3)/2
    # cent_mid = (s1+s2)/2

    
    # circle1 = plt.Circle((cent_maj, 0), R_maj, fill = False)
    # circle2 = plt.Circle((cent_min, 0), R_min, fill = False)
    # circle3 = plt.Circle((cent_mid, 0), R_mid, fill = False)
    
    circle1 = plt.Circle((l1, 0), r1, fill = False)
    circle2 = plt.Circle((l2, 0), r2, fill = False)
    circle3 = plt.Circle((l3, 0), r3, fill = False)
    
    plt.style.use('ggplot')
    
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    
    plt.title("Mohr's Circle")
    plt.xlabel('\u03C3')
    plt.ylabel('\u03C4')  
    
    ax.set_xlim((-200, 200))
    ax.set_ylim((-200, 200))    
    
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)

    fig.savefig('Mohr.png')
    
    # print(R_maj)
    
    return R_maj,R_mid, R_min 
