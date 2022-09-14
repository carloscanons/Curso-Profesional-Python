def is_impar(entero: int):
    x=0
    if entero ==2:
        print("Es primo")
    elif entero ==1:
        print("Número mayores a 1 por favor")
    else:
       for i in range(2,round(entero/2)):
          if entero%i==0:
              x+=1
       if x>0:
            return False
       else:
            return True

def run():
    entero=int(input("Escribe un número: "))
    is_impar(entero)

if __name__ =='__main__':
    run()




        

