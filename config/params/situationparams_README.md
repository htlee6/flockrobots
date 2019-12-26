# Situation Parameters

The instructions of the `situationparams_default.json` is as following. 

1. NumberOfAgents\
    Type: `int`\
    The number of agents simulated in the flock.
    
2. LengthOfSimulation\
    Type: `float` \
    Time length of simulated experiment. 
    
3. InitPosition\
    Type: `float`\
    Initial positions in 3 dims, X, Y, Z respectively.

    1. InitX
    2. InitY
    3. InitZ

4. deltaT\
    Type: `float`\
    Accuracy of the Euler method, which is known as, 
    $$v(t+\triangle t)=v(t)+a(t)\times\triangle t$$
5. DangerousRadius\
   Type: `float`\
   If distance between two agents is less than the DangerousRadius, then they are both in a 'danger status'. 
6. LengthToStore\
   Type: `float`\
   Length to store in memory (s), Larger stored length means faster running, but more allocated memory
7. StartOfSteadyState\
Type:`int`\
Start of steady state. 
   