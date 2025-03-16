def modify_value(x):
    x = 10
    print("Within function:", x)

# Immutable object (integer)
x = 5
print("Original:", x)
modify_value(x)
print("After function:", x)