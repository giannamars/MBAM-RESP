using NBInclude

CURDATAPOINT = 0
save_str = "test_"

for j11 = 1:100
           CURDATAPOINT = j11
           nbinclude("run_Simulations_reducedv063.ipynb")
           println(CURDATAPOINT)
       end

