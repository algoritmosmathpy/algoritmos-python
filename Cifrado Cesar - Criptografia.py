L='ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Longitud y el Abecedario a utilizar [Ordenado]
X=str(input('Cadena a Cifrar: ')).upper() #Pedimos la Cadena a Cifrar
C=int(input('Clave Numerica: ')) #Pedimos la Clave Numerica a utilizar
Texto_cifrado='' #Aqui estara el resultado final
  
for letra in X: #Recorremos letra a letra la cadena a cifrar
    if letra == " ":
        Texto_cifrado += " "
    else: 
        Operacion=L.find(letra)+C #Buscamos la posiciin en el abecedario y le sumamos la clave
        Modulada=int(Operacion)%26 #Le aplicamos mod26 en caso de que sobrepase ese rango
        Texto_cifrado= Texto_cifrado+str(L[Modulada]) #con la nueva posicion, la buscamos en el abecedario y guardamos
  
print(Texto_cifrado) #Texto cifrado final 