#break statement
#Stops the loop immediately when a condition is met.
# Example of break: stop when number = 5

for i in range(1, 11):
    if i == 5:
        print("Breaking at", i)
        break
    print(i)

#continue
#Skip the current iteration and moves to the next one.
# Example of continue: skip when number = 5

for i in range(1, 11):
    if i == 5:
        continue
    print(i)
