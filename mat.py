import matplotlib.pyplot as graph
import numpy as np

#draw a line in a diagram from (position  (1,4) top position (4,7))
x = np.array([1,2,3,4])
y = np.array([4,5,6,7])

graph.plot(x,y, marker = 'o', ms=20)
font1 = {'family':'serif','color':'green','size':20}
graph.xlabel("x-units", fontdict = font1)
graph.ylabel("y-units", fontdict = font1)
graph.show()

graph.plot(x,y, marker = '*', linewidth = '10')
graph.show()

graph.plot(x,y, marker = ',')
graph.show()

graph.plot(x,y, marker = 'P')
graph.show()

graph.plot(x,y, marker = 'D')
graph.grid()
graph.show()

graph.plot(x,y, marker = 'H')
graph.show()

graph.plot(x,y, marker = '^')
graph.show()

graph.plot(x,y, marker = '2')
graph.show()


#draw a line in diagram using two points

y = np.array([1,20,11,2,9,13,18])
graph.plot(y,'o-r')
graph.grid()
graph.show()

graph.plot(y,'o:r')
graph.show()

graph.plot(y,'o--r')
graph.show()

graph.plot(y,'o-.r')
graph.show()

graph.plot(y,'b')
graph.grid()
graph.show()


x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])

graph.title("Two Graph in One", loc = 'left')
graph.xlabel("x-units", fontdict = font1)
graph.ylabel("y-units")
graph.grid(axis='y')
graph.plot(x1,y1,x2,y2)
graph.show()


x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])

graph.subplot(1,2,1)
graph.plot(x1,y1)
graph.title('Plot-1')

x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])

graph.subplot(1,2,2)
graph.plot(x2,y2)
graph.title('Plot-2')

graph.suptitle('Sub-Plot')
graph.show()


x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])

graph.subplot(2,1,1)
graph.plot(x1,y1)
graph.title('Plot-1')

x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])

graph.subplot(2,1,2)
graph.plot(x2,y2)
graph.title('Plot-2')

graph.suptitle('Sub-Plot')
graph.show()



x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
graph.subplot(2,3,1)
graph.plot(x1,y1)

x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])
graph.subplot(2,3,2)
graph.plot(x2,y2)

x3 = np.array([0,1,2,3])
y3 = np.array([5,11,3,13])
graph.subplot(2,3,3)
graph.plot(x3,y3)

x4 = np.array([0,1,2,3])
y4 = np.array([3,8,1,10])
graph.subplot(2,3,4)
graph.plot(x4,y4)

x5 = np.array([0,1,2,3])
y5 = np.array([6,2,7,11])
graph.subplot(2,3,5)
graph.plot(x5,y5)

x6 = np.array([0,1,2,3])
y6 = np.array([5,11,3,13])
graph.subplot(2,3,6)
graph.plot(x6,y6)

graph.show()

#pie chart
y = np.array([1,20,11,2,9,13])
mylabels = ["Maths","English","Engg. Pysics","Engg. Chemistry","BEE", "Mechanics"]
graph.pie(y,labels = mylabels)
graph.show()

x = np.array([66,88, 95, 75, 90])
mylabels = ["BEE", "Maths-1", "Physics", "Chemistry", "Mechanics"]
myexplode = np.array([0,0,0.1,0,0])
graph.pie(x,labels = mylabels, startangle=90, explode = myexplode, shadow=0.2)
graph.show()

# Data for semesters
sem1x = np.array(['m1','p1','c1','bee','mech'])
sem1y = np.array([73, 75, 67, 56, 70])

sem2x = np.array(['m2','p2','c2','cp','eg'])
sem2y = np.array([75, 60, 63, 66, 75])

sem3x = np.array(['m3','pcpf','poc','dbms','dsa'])
sem3y = np.array([90, 69, 54, 74, 75])

# Data for overall pointers
pointerx = np.array(['sem1','sem2','sem3'])
pointery = np.array([8.67, 8.83, 8.7])

# Create subplots
graph.figure(figsize=(12, 8))
# Subplot 4
graph.subplot(2, 3, 2)
graph.bar(pointerx, pointery, color = 'purple')
graph.title('Overall Pointer')

# Subplot 1
graph.subplot(2, 3, 4)
graph.bar(sem1x, sem1y)
graph.title('Semester 1')

# Subplot 2
graph.subplot(2, 3, 5)
graph.bar(sem2x, sem2y)
graph.title('Semester 2')

# Subplot 3
graph.subplot(2, 3, 6)
graph.bar(sem3x, sem3y)
graph.title('Semester 3')




# Adjust layout
graph.tight_layout()

# Display the plot
graph.show()