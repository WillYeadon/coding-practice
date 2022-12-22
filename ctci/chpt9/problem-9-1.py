# Stock data system design

# Want FTP server to deliver clients 
# [open, close, high, low] of a stock
# Can make this more complex & include querying
# but would need a database probs SQL based
# to achieve this; rollback, backups & security 
# are pretty standard features that could just
# be used w/ a SQL implementation. 

# Disadvantages to mention: SQL admin could be
# given by accident affecting security and
# clients may perform very inefficient queries
# that would be costly server side.