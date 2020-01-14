import numpy as np

def gradient_descent(x,y):

    # Straight line equation: y=mx+b
    # First initialization of m and b
    m_curr = b_curr = 0

    # how many times i want to update my parameters
    iterations = 10000
    n = len(x)

    # how much longer step i should take if i want to go to the global minimum
    learning_rate = 0.08

    for i in range(iterations):
        
        #basic hypothesis
        y_predicted = m_curr * x + b_curr
        #determining the cost function -> Mean Squared Error
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        # Partial Derivative of cost function
        # we are doing the derivative of cost function, because every step we go through the cost function.
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        # our new point after the previous jump step
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        #print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))

    return m_curr, b_curr

# Training input
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

m,b = gradient_descent(x,y)

# Test data
x_test = np.array([44,33,0])
y_test = []

for i in x_test:
    ans = m*i+b
    y_test.append(ans)

print(y_test)