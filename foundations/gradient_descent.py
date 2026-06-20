class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:

        initial_minimizer = init # we initialize some value 
        for _ in range(iterations):
        # formula : 
        # thetaj := thetaj - alpha(delt(f(j))) where alpha is learning rate
        # given f(j)= j*j ; 
            derivative = 2*initial_minimizer
            initial_minimizer-=learning_rate*derivative
        return round(initial_minimizer,5)

        
     