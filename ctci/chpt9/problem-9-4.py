# Duplicate URLs

# Can use a distributed Bloom filter whereby websites 
# are hashed to a URL and duplicates are checked in 
# real time as URLs are added. Only 'probably yes'
# duplicates are checked thouroughly

# Empty Bloom fliter
# [0|0|0|0|0|0|0|0|0|0]

# Website #1 hash

# Added to filter
# [1|0|0|1|1|0|0|0|0|0]

# Website #2 hash
# [0|0|0|1|0|0|1|0|0|1]
# Added to filter
# [1|0|0|1|1|0|1|0|0|1]

# Check website 1 hash against filter will see that 
# All elements of the hash are in the fitler 
# [1|0|0|1|1|0|0|0|0|0]
# [1|0|0|1|1|0|1|0|0|1]
# Thus is 'probably yes' a member 

# Whereas say Website 3 hash 
# [0|0|0|1|0|1|1|0|0|0]
# Not all elements are in filter
# [1|0|0|1|1|0|1|0|0|1]
# Thus is definitely not a member

# However website 4 hash 
# [1|0|0|1|0|0|1|0|0|1]
# Has all memebers in the filter
# [1|0|0|1|1|0|1|0|0|1]
# But wasn't actually added to it hence it is
# probably yes.

# Can also implement a secondary check where if there
# is a hash collision the content of the URLs can be
# requested and compared for equality.

# Want to avoid hashing one-hit wonder URLs. 