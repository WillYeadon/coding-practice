# 19 bottles w/ 1g pills and 1 bottle w/ 1.1g
# Using an exact scale once find which bottle has the heavy pills

#####################################

# Soln is to number the bottles 1 through 20 then take
# 1 pill out of #1, 2 pills out of #2 etc...
# Sum of int 1 -> n = (n * (n + 1) / 2) so 20 * 21 * 0.5 = 210
# The value on the scale above 210 identifies the heavy bottle
# 211.1 would mean bottle #11, 210.7 would mean bottle #7 etc ...