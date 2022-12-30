# Three ants sit on the verticies of a triangle
# What are the chances of the ants colliding if
# they each start walking in a random direction

# Answer here is to note that only way to avoid
# a collision is for them all to walk in the 
# same direciton either clockwise or anti-cw
# this is LLL or RRR. The other options of
# RRL, RLR, RLL, LRL, LLR, LRR will collide
# at LR. Thus 6/8 options will collide

# Increase this to n sides and note still only
# RRRR, LLLL & RRRRR, LLLLL etc... collide so
# only every 2 non collide and the remainder
# 2^n - 2 do collide thus for n sides the odds
# of collision is ((2^n) - 2)/n