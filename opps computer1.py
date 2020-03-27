##  so we can create more object as we want


class computer():
    def config(self):
        print("i5,16gb,1TB")


com1 = computer()
com2 = computer()

computer.config(com1)  ##here i put the com1 inplace of self and it give the outut first
computer.config(com2)

com1.config()  # it take like an argument and so we get more out put
com2.config()

# a=5
# a.bit_length(a)   # i put this for checking of bit length (ctrl+click curser after bit.
