# A. Get 1 shot @ p
# B. Get 3 shots @ p but need to make 2/3

# first game A is just p. Second game B is the cumulative chance
# of getting all three shots in (p^3) plus getting two in (p^2)
# and not getting one in (1-p). You can do this three ways
# xxo, xox and oxx. Therefore, you should pick B when:
#
#   p^3 + 3*p^2*(1-p) > p
#
# -> 3p^2 - 2p^3 > p
# -> 3p - 2p^2 > 1
# -> -2p^2 + 3p - 1 > 0
# quadratic with solutions at 1 or 1/2 so (2p - 1)(p - 1)
# -> (2p - 1)(p - 1) > 0 when 0.5 < p < 1

# Pick game B if p > 0.5