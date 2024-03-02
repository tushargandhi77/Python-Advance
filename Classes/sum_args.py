# class sum:
#     def s(self,**args):
#         sm = 0
#         for x in args:
#             sm += x
#         print(args)
#         print(sm)


class Sum_args:
    def __init__(self,*args) -> None:
        s = 0
        for x in args:
            s += x
        print(args)
        print(s)

x = Sum_args(1,23,4,53,3)           
        


