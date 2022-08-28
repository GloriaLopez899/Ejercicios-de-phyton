precio = input("Inserte el precio del producto: ")
print ("euros: ", precio[:precio.find(".")], "Centimos: ",precio[precio.find(".")+1:] )
