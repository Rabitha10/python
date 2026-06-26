# *1. Default Arguments*
# *Task*: Write `greet(name, greeting="Hello")`  
# *It should*: Print `"{greeting}, {name}!"`  
# *Test these calls*:  
# - `greet("Arjun")` → `Hello, Arjun!`
# - `greet("Maya", "Hi")` → `Hi, Maya!`
# - `greet(name="Sara", greeting="Hey")` → `Hey, Sara!`


def greet(name,greeting="hello"):
    print(f"{greeting},{name}")

greet("arjun")
greet("Maya", "Hi")
greet(name="Sara", greeting="Hey")



# *2. Keyword-Only Arguments*
# *Task*: Write `total_cost(price, _, tax=0.18, tip=0)`  
# *It should*: Return `price + price_tax + tip`  
# *Question*: Why does `total_cost(100, 0.2)` give an error?  
# *Test*: `total_cost(100, tip=10)` should return `128.0`


def total_cost(price,*,tax=0.18,tip=0):
    return(price+price*tax)+tip
print(total_cost(100, tip=10))

# *3. Positional-Only Arguments*
# *Task*: Write `divide(a, b, /)` for Python 3.8+  
# *It should*: Return `a / b`  
# *Question*: What happens if you try `divide(a=10, b=2)`?

def divide(a,b,/):
    return(a/b)
print(divide(10,2))

# *4. _args - Variable Positional*
# *Task*: Write `multiply_all(_nums)`  
# *It should*: Return product of all numbers. Return `1` if no args given.  
# *Test*:  
# - `multiply_all(2, 3, 4)` → `24`
# - `multiply_all()` → `1`

def multiply_all(*nums):
    result = 1
    for num in nums:
        result *= num
    return result
print(multiply_all(2, 3, 4))
# print(multiply_all())

# *5. *kwargs - Variable Keyword*_
# *Task*: Write `build_sentence(__words)`  
# *It should*: Join all values from kwargs with spaces. Order doesn’t matter.  
# *Test*: `build_sentence(a="Python", b="is", c="fun")` → `"Python is fun"` or similar

def build_sentance(**words):
      return " ".join(words.values())
print(build_sentance(a="Python", b="is", c="fun"))

# *6. All Types Combined*
# *Task*: Write `order_pizza(size, _toppings, crust="thin", *_extras)`  
# *It should*: Return a dict like:  
# `{"size": size, "toppings": tuple_of_toppings, "crust": crust, "extras": extras_dict}`  
# *Test*: `order_pizza("Large", "mushrooms", "onions", cheese="extra", delivery=True)`

def order_pizza(size,*toppings,crust="thin",**extras):
     return {"size": size, "toppings": toppings, "crust": crust, "extras": extras}
print(order_pizza("Large", "mushrooms", "onions", cheese="extra", delivery=True))


# chess bord black print o white print 

def chessboard():
    for row in range(8):
        for col in range(8):
            print((row + col) % 2, end=" ")
        print()

chessboard()