# numeros-primos-Emagperez
# numeros-primos-Emagperez
Nombre: Emanuel Perez Gianolini
Legajo: 60117
DNI: 42.795.175


El Codigo de numero primos define primero una funcion que tiene dos argumentos, uno value que es el numero que vamos a ver si es primo y n que esta establecido en 2, que es el divisor para verificar si value es divisible por el.
Despues se inicia un bucle while que se ejecutara siempre que value sea mayor o igual a 1.
Dentro del bucle se verificia si n es mayor o igual que value. Si es asi, esto significa que hemos probado todos los posibles divisores de value y no hemos encontrado ninguno por lo que value es primo. En este caso retorna True
Si n no es mayor o igual a value, se verifica si value es divisible por n. si el resto de la division no es cero, significa que value no es divisible por n, por lo que llamamos devuelta a la funcion incrementando a n en 1 para probar el siguiente posible divisor
Si value es divisible por n, entonces value no es primo por lo que devuelve false
