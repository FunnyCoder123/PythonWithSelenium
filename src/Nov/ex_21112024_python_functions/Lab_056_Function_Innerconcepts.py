def outer_function():
    var1 = 30
    print(var1)
    def inner_function():
        var2 = 40
        print(var2)

    def inner_function2():
        print(var1)

    inner_function()
    inner_function2()
outer_function()
