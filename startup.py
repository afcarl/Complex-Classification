from numpy import *
from pylab import *

import util, datasets, mlGraphics, gd, runClassifier

# first check for GD
gd.gd(lambda x: x**2, lambda x:2*x, 10, 10, 0.2)
x, trajectory = gd.gd(lambda x: x**2, lambda x:2*x, 10, 100, 0.2)
#plot(trajectory)
#show()

# x, t = gd.gd(lambda x:linalg.norm(x)**2, lambda x: 2*x, array([10,5]), 100, 0.2)


# WU1 ##########

# for i in arange(5, 7, 0.1):
#  x, t = gd.gd(lambda x: x**2, lambda x:2*x, 10, 100, i)
#  if x > 1: print('diverges to x:', x, ', at step:', i);
#  else: print('converges to x:', x, ', at step:', i);

# WU 2 ##########
f = lambda x: sin(pi*x) + x**2/2
derF = lambda x: pi*cos(pi*x) + x
# x = linspace(-5, 5, 500)
# plot(x, f(x), 'b-')
# plot(-0.4538, f(-0.4538), 'r*') #plot the global min
# title('f(x) = sin(x*pi) + x^2/2')

x_global, t = gd.gd(f, derF, 0, 10, 0.2)
x_local, t = gd.gd(f, derF, 1, 10, 0.2)

##########

#For linear
import linear
h = linear.LinearClassifier({'lossFunction': linear.SquaredLoss(), 'lambda': 0, 'numIter': 100, 'stepSize': 0.5})


runClassifier.trainTestSet(h, datasets.TwoDAxisAligned)

X = datasets.TwoDAxisAligned.X
Y = datasets.TwoDAxisAligned.Y

#mlGraphics.plotLinearClassifier(h, X, Y)

h = linear.LinearClassifier({'lossFunction': linear.SquaredLoss(), 'lambda': 10, 'numIter': 100, 'stepSize': 0.5})
runClassifier.trainTestSet(h, datasets.TwoDAxisAligned)


h = linear.LinearClassifier({'lossFunction': linear.SquaredLoss(), 'lambda': 10, 'numIter': 100, 'stepSize': 0.5})
runClassifier.trainTestSet(h, datasets.TwoDDiagonal)

h = linear.LinearClassifier({'lossFunction': linear.HingeLoss(), 'lambda': 1, 'numIter': 100, 'stepSize': 0.5})
runClassifier.trainTestSet(h, datasets.TwoDDiagonal)

log = linear.LinearClassifier({'lossFunction': linear.LogisticLoss(), 'lambda': 1, 'numIter': 100, 'stepSize': 0.5})
runClassifier.trainTestSet(log, datasets.TwoDDiagonal)
        

        
