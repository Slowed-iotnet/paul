#Paul Gonzales & Jimenes Olivas
ham = 100     #Se establece el precio de las hamburguesas
pizza = 150   #Se establece el precio de las pizzas
Ensalada = 70 #Se establece el precio de las ensaladas
soda = 25     #Se establece el precio de las sodas
agua = 15     #Se establece el precio de las aguas

while True:
    print("""[Menu]
Hamburguesa - $100
Pizza - $150
Ensalada - $70
Soda - $25
Agua natural - $15""") #Se imprime en la pantalla el menu

    QHamb = int(input("\nCuantas hamburguesas consumio » ")) #Se toma el dato de las hamburguesas consumidas
    cuentaham = ham * QHamb #Se crea una nueva variable en la cual estamos multiplicando el precio por las hamburguesas que consumieron

    QPizz = int(input("\nCuantas pizzas consumio » ")) #Se toma el dato de las pizzas consumidas
    cuentapiz = pizza * QPizz #Se crea una nueva variable en la cual estamos multiplicando el precio por las pizzas que consumieron

    QEnsa = int(input("\nCuantas ensaladas consumio » ")) #Se toma el dato de las ensaladas consumidas
    cuentaensa = Ensalada * QEnsa #Se crea una nueva variable en la cual estamos multiplicando el precio por las ensaladas que consumieron

    QSoda = int(input("\nCuantas sodas consumio » ")) #Se toma el dato de las sodas consumidas
    cuentasoda = soda * QSoda #Se crea una nueva variable en la cual estamos multiplicando el precio por las sodas que consumieron

    QAgua = int(input("\nCuantas aguas consumio » ")) #Se toma el dato de las aguas consumidas
    cuentaagua = agua * QAgua #Se crea una nueva variable en la cual estamos multiplicando el precio por las aguas que consumieron

    total = cuentaham + cuentapiz + cuentaensa + cuentasoda + cuentaagua #Se suman todos los datos anteriormente tomados y se guardan en una variable
    propina = 10 * total/100 #Se saca el 10% de la cuenta para ponerla como propina sugerida

    print(f"""\n[Cuenta]
Hamburgesa x{QHamb} = ${cuentaham}
Pizza x{QPizz} = ${cuentapiz}
Ensalada x{QEnsa} = ${cuentaensa}
Soda x{QSoda} = ${cuentasoda}
Agua x{QAgua} = ${cuentaagua}
\nTotal a pagar = ${total}\n\n[No obligatorio]\nPropina Sugerida {propina} """) #Se imprime la cuenta
    input()
    print(" ")
    print(" ")
    print(" ")