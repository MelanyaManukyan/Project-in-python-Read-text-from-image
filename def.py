def a():
    def b():
        print("b locals:", locals())
        print(sum)
        # global var # xorhurd chi trvum ogtagorcel
        # var = "hi"
    var = "name var"
    return b()

a()