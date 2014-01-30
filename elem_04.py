while(True):
    try:
        raw_n = raw_input("give me a positive number n, I'll give you sum of 1 to n. ")
        n = int(raw_n)
        if n <= 0:
            print "Oops! That was not a positive number. Try again..."
        else:
            break
    except ValueError:
        print "Oops! That was no valid number. Try again..."

print "Your input is", raw_n, ". ",
print "The sum of 1 to", raw_n, "is", sum(range(1,n+1)),". "
