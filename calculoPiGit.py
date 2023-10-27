import numpy as np
from timeit import default_timer as timer

def inside(p):
    """
    Generate a random point and check if the point is within the circle with radius=1.

    Returns:
        (bool) whether the generated point is within the circle area
    """
    x, y = np.random.random(), np.random.random()
    return x*x + y*y < 1

def estimate_pi(num_samples):
    """
    Estimate the value of Pi by means of repeated sampling. Benchmark the repeated sampling time cost.

    Params:
        num_sampes (int): the number of sample points to generate

    Returns:
        (float) estimated value of Pi
    """
    print("Executing Spark job...")
    start = timer()
    dots = list(filter(inside,list(range(num_samples)))) 
    count = len(dots)
    end = timer()
    print("Spark job ended. Total time elapsed: %s" % (end-start))
    return(4.0 * count / num_samples)

estimate_pi(5000000)
