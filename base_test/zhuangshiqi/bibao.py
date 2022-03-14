# coding:utf8

def print_msg():
    msg = "Tm closure" 
    def printer():
        print(msg)
    return printer 

closure = print_msg() 
closure() 

#============================================================================


