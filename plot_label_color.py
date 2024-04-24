import matplotlib.pyplot as plt
# plt.plot([1,2,3,4],[2,3,4,5],"r") #-- here 'r' is the color represent of red line.
# plt.plot([1,2,3,4],[2,3,4,5],"r+") #-- here 'r' is the color red and '+' indicates marker, 
# it means it will now mark the points instead of line .
# THIS ("r+") IS called formate argument.
# More: linewidth(), linesize()
# EX:
# plt.plot([1,2,3,4],[2,3,4,5],"r" , linewidth=20)

# plt.plot([1,2,3,4],[2,3,4,5],color= "blue", linewidth=5)

# plt.plot([1,2,3,4],[2,3,4,5],color= "blue", linewidth=5)
# plt.plot([1,2,3,4],[3,5,9,11],color= "red", linewidth=2)
# Instead of writting 2 plot -- we can pass in one plot like below:
plt.plot([1,2,3,4],[3,4,5,6],"r", [2,3,4,5],[4,7,9,11],"b")
plt.plot([1,2,3,4],[3,4,5,6],"r", [2,3,4,5],[4,7,9,11],"bo") #-- 'bo' here 'o' for dot style
plt.plot([1,2,3,4],[3,4,5,6],"r", [2,3,4,5],[1,7,3,8],"ro") #-- 'ro'  for dot style
plt.xlabel("X - exis")
plt.ylabel("Y - exis")
plt.title("My first demo Plot")

plt.show()
