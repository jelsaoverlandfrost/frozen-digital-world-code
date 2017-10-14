import math
def approx_ode(h,t0,y0,tn):
######### h - step size
######### t0 - initial t value (at step 0)
######### y0 - initial y value (at step 0)
######### tn - t value at step n

######### Add you code below this line
######### Return your answer correct to 3 decimal places
    y = float(y0)
    t = float(t0)
    while t < tn - 0.09:
        y += h * (1.0 / 2.0 * f(t, y) + 1.0 / 2.0 * f(t + h, y) + h * f(t, y))
        t += h
    return round(y,3)


######### Ignore code below this line ######################################

def f(t, y):
    return 4 - t + 2 * y

print approx_ode(0.1, 0, 1, 5)