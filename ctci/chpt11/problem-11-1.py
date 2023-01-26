# unsigned int i;
# for (i = 100; i >= 0; i--)
#    printf("%d\n", i);

# You're going to end up with an off by one error as
# the int is unsigned and so can never be < 0 thus
# the condition i >= 0 will always be true and the 
# loop will execute indefinitely.

# Should also use %u instead of %d