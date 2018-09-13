# Create the base parameter vector and the time-(dummy)temparature grid to evaluate respiration rate over

using NBInclude
nbinclude("../MBAM.ipynb")
nbinclude("BK_functions.ipynb")

using Iterators
Time = linspace(0,40,40)
Temp = [1.0]

x_grid = Array(Any, (length(Temp)*length(Time),))
iterind = 0;
for j1 in product(Temp, Time)
    iterind += 1;
    x_grid[iterind] = collect(j1)
end

# Base parameter set
phi0 = [0.504, 0.394,0.027, 0.5, 0.00613];
#phi0 = [0.504, 0.394, 0.027, 0.00613];
#phi0 = [0.504]