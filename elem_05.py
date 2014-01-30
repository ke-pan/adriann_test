while(True):
    try:
        raw_n = raw_input("give me a positive number n, I'll give you sum of multiples of 3 or 5 from 1 to n. ")
        n = int(raw_n)
        if n <= 0:
            print "Oops! That was not a positive number. Try again..."
        else:
            break
    except ValueError:
        print "Oops! That was no valid number. Try again..."

s = sum(range(0,n+1,3)) + sum(range(0,n+1,5)) - sum(range(0,n+1,15))
print "Your input is", raw_n, ". ",
print "The sum of 1 to", raw_n, "is", s, ". "
