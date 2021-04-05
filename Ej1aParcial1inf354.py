    
import csv

with open(r'C:\Universidad\Septimo\354\datasetVentasJuegos.csv', newline='') as f:
    reader = csv.reader(f)
    datos = list(reader)

sumn=0 
sume=0 
sumj=0 
sumo=0 
sumg=0

for i in range(1,len(datos)):
    sumn+=float(datos[i][6])
    sume+=float(datos[i][7])
    sumj+=float(datos[i][8])
    sumo+=float(datos[i][9])
    sumg+=float(datos[i][10])

mdna=round(sumn*1000000/(len(datos)-1),2)
mdeu=round(sume*1000000/(len(datos)-1),2)
mdjp=round(sumj*1000000/(len(datos)-1),2)
mdot=round(sumo*1000000/(len(datos)-1),2)
mdgl=round(sumg*1000000/(len(datos)-1),2)
print("Medias\nVentas norte américa:",
      mdna,'\n'
      "Ventas europa:",
      mdeu,'\n'
      "Ventas japón:",
      mdjp,'\n'
      "Ventas resto del mundo:",
      mdot,'\n'
      "Ventas globales:",
      mdgl,'\n\n'
      )
#se resta 1 para descontar la primera columna de titulo
#desviacion
dvna = 0; dveu = 0; dvjp = 0; dvot = 0; dvgl = 0;

for i in range(1,len(datos)):
    dvna=dvna+(((float(datos[i][6])*1000000)-mdna)**2)
    dveu=dveu+(((float(datos[i][7])*1000000)-mdeu)**2)
    dvjp=dvjp+(((float(datos[i][8])*1000000)-mdjp)**2)
    dvot=dvot+(((float(datos[i][9])*1000000)-mdot)**2)
    dvgl=dvgl+(((float(datos[i][10])*1000000)-mdgl)**2)

    
dvna=(dvna/(len(datos)-1))**1/2; dveu=(dveu/(len(datos)-1))**1/2;
dvjp=(dvjp/(len(datos)-1))**1/2; dvot=(dvot/(len(datos)-1))**1/2;
dvgl=(dvgl/(len(datos)-1))**1/2;

print("Desviacion estandar\n"
      "Ventas norte america: ",round(dvna,2),'\n' 
      "Ventas europa: ",round(dveu,2), '\n'
      "Ventas japón: ",round(dvjp,2), '\n'
      "Ventas resto del mundo: ",round(dvot,2), '\n'
      "Ventas globales: ",round(dvgl,2),'\n\n')

#modas
lnom = []; lpla = []; lyea = []; lgen = []; lvna = [];
lveu = []; lvjp = []; lvot = []; lvgl = []; lpub = []


for i in range(1,len(datos)):
    lnom.append(datos[i][1]); lpla.append(datos[i][2])
    lyea.append(datos[i][3]); lgen.append(datos[i][4])
    lpub.append(datos[i][5]); lvna.append(datos[i][6]);
    lveu.append(datos[i][7]); lvjp.append(datos[i][8]);
    lvot.append(datos[i][9]); lvgl.append(datos[i][10])
    
    
lnom.sort(); lpla.sort(); lyea.sort(); lgen.sort()
lvna.sort(); lveu.sort(); lvjp.sort(); lvot.sort()
lvgl.sort(); lpub.sort()

rep=0; rep1=0; rep2=0; rep3=0; rep4=0; 
rep5=0; rep6=0; rep7=0; rep8=0; rep9=0; 

actual=''; actual1=''; actual2=''; actual3=''; actual4=''
actual5=''; actual6=''; actual7=''; actual8=''; actual9='' 

mayor=0; mayor1=0; mayor2=0; mayor3=0; mayor4=0;
mayor5=0; mayor6=0; mayor7=0; mayor8=0; mayor9=0;

moda=''; moda1=''; moda2=''; moda3=''; moda4='';
moda5=''; moda6=''; moda7=''; moda8=''; moda9='';

for i in range(1,len(lnom)):
    if lnom[i] != actual:
        actual = lnom[i]
        rep = lnom.count(actual)
        if rep >= mayor:
            mayor=rep
            moda=actual
            
    if lpla[i] != actual1:
        actual1 = lpla[i]
        rep1 = lpla.count(actual1)
        if rep1 >= mayor1:
            mayor1=rep1
            moda1=actual1
    
    if lyea[i] != actual2:
        actual2 = lyea[i]
        rep2 = lyea.count(actual2)
        if rep2 >= mayor2:
            mayor2=rep2
            moda2=actual2
            
    if lgen[i] != actual3:
        actual3 = lgen[i]
        rep3 = lgen.count(actual3)
        if rep3 >= mayor3:
            mayor3=rep3
            moda3=actual3
    
    if lpub[i] != actual4:
        actual4 = lpub[i]
        rep4 = lpub.count(actual4)
        if rep4 >= mayor4:
            mayor4=rep4
            moda4=actual4
            
    if lvna[i] != actual5:
        actual5 = lvna[i]
        rep5 = lvna.count(actual5)
        if rep5 >= mayor5:
            mayor5=rep5
            moda5=actual5
    
    if lveu[i] != actual6:
        actual6 = lveu[i]
        rep6 = lveu.count(actual6)
        if rep6 >= mayor6:
            mayor6=rep6
            moda6=actual6
            
    if lvjp[i] != actual7:
        actual7 = lvjp[i]
        rep7 = lvjp.count(actual7)
        if rep7 >= mayor7:
            mayor7=rep7
            moda7=actual7 
    
    if lvot[i] != actual8:
        actual8 = lvot[i]
        rep8 = lvot.count(actual8)
        if rep8 >= mayor8:
            mayor8=rep8
            moda8=actual8
            
    if lvgl[i] != actual9:
        actual9 = lvgl[i]
        rep9 = lvgl.count(actual9)
        if rep9 >= mayor9:
            mayor9=rep9
            moda9=actual9
             
    
        
print('Modas\nmoda nombres:',moda,'Conteo:', mayor,'\n'
      'moda plataformas:',moda1,'Conteo:', mayor1,'\n'
      'moda años:',moda2,'Conteo:', mayor2,'\n'
      'moda generos:',moda3,'Conteo:', mayor3,'\n'
      'moda editoras:',moda4,'Conteo:', mayor4,'\n'
      'moda ventas NA:',moda5,'Conteo:', mayor5,'\n'
      'moda ventas EU:',moda6,'Conteo:', mayor6,'\n'
      'moda ventas JP:',moda7,'Conteo:', mayor7,'\n'
      'moda ventas resto del mundo:',moda8,'Conteo:', mayor8,'\n'
      'moda ventas globales:',moda9,'Conteo:', mayor9,'\n'
      )   
