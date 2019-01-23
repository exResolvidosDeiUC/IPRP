def gera_cadeia(lista):
   comp=0
   for n in range(len(lista)):
      comp+=lista[n][2]+1
   cadeia=comp*'x'
   for i in range(len(lista)):
      car=lista[i][0]
      pos=lista[i][1]
      rep=lista[i][2]
      for j in range(rep+1):
         cadeia= cadeia[:pos+j] + car + cadeia[pos+j+1:]
   return cadeia
      
print(gera_cadeia([('2',1,1),('a',10,0),('x',0,0),('d',3,2),(' ',6,0),('c',7,0),('b',8,1)]))