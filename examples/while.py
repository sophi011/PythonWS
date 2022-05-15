def main():
   print("Contagem de 1 a 10")
   chegouNo10 = False
   contador = 1
   while not chegouNo10: #Le-se "enquanto nao chegou no 10"
       if contador == 10:
           chegouNo10 = True 
       print(contador)
       contador += 1
   print()
main()
