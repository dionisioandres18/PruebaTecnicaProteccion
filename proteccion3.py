import cv2
from reportlab.lib.pagesizes import A4,landscape
from reportlab.pdfgen import canvas

#Cargar imagen
archi="11.jpg"
imagen=cv2.imread(archi)

#Conocer tamaño
(alto,ancho,canales)=imagen.shape
print ('Ancho={},Alto={}'.format(ancho,alto))

if (ancho==alto):
    print('La imagen es cuadrada')
    if((ancho>796)or(alto>1123)):
        r=ancho/alto
        print('Relacion Imagen:',r)
        ancho_d=796
        alto_d=int(ancho_d/r)
        c = canvas.Canvas("proteccion.pdf", pagesize=(796,1123))
        c.drawImage(archi,0,0,ancho_d,alto_d)
        print('Ancho nuevo= ',ancho_d,'Alto nuevo',alto_d)
        print('Relacion Imagen:',ancho_d/alto_d)
        c.showPage()
        c.save()
    else:
        c = canvas.Canvas("proteccion.pdf", pagesize=(796,1123))
        c.drawImage(archi,0,0)
        c.showPage()
        c.save()
        
if (ancho<alto):
    print('La imagen tiene orientacion vertical')
    print('La página tiene orientacion vertical')
    if (alto>1123)and(ancho<796):
        r=ancho/alto
        print(r)
        alto_d=1123
        ancho_d=int(alto_d*r)
        c = canvas.Canvas("proteccion.pdf", pagesize=(796,1123))
        c.drawImage(archi,0,0,ancho_d,alto_d)
        print('Ancho nuevo= ',ancho_d,'Alto nuevo',alto_d)
        print('Relacion Imagen:',ancho_d/alto_d)
        c.showPage()
        c.save()
        
    elif (alto>1123)and (ancho>796):
        r=ancho/alto
        print('Relacion Imagen:',r)
        ancho_d=796
        alto_d=int(ancho_d/r)
        c = canvas.Canvas("proteccion.pdf", pagesize=(796,1123))
        c.drawImage(archi,0,0,ancho_d,alto_d)
        print('Ancho nuevo= ',ancho_d,'Alto nuevo',alto_d)
        print('Relacion Imagen:',ancho_d/alto_d)
        c.showPage()
        c.save()

    elif (alto<=1123) and (ancho<=796):
        c = canvas.Canvas("proteccion.pdf", pagesize=(796,1123))
        c.drawImage(archi,0,0)
        c.showPage()
        c.save()
    
if (ancho>alto):
    print('La imagen tiene orientacion horizaontal')
    print('La página tiene orientacion horizontal')
    if (ancho>1123)and(alto<796):
        r=ancho/alto
        print('Relacion Imagen:',r)
        ancho_d=1123
        alto_d=int(ancho_d/r)
        c = canvas.Canvas("proteccion.pdf", pagesize=(1123,796))
        c.drawImage(archi,0,0,ancho_d,alto_d)
        print('Ancho nuevo= ',ancho_d,'Alto nuevo',alto_d)
        print('Relacion Imagen:',ancho_d/alto_d)
        c.showPage()
        c.save()
        
    elif (ancho>1123)and (alto>796):
        r=ancho/alto
        print('Relacion Imagen:',r)
        ancho_d=1123
        alto_d=int(ancho_d/r)
        c = canvas.Canvas("proteccion.pdf", pagesize=(1123,796))
        c.drawImage(archi,0,0,ancho_d,alto_d)
        print('Ancho nuevo= ',ancho_d,'Alto nuevo',alto_d)
        print('Relacion Imagen:',ancho_d/alto_d)
        c.showPage()
        c.save()

    elif (alto<=1123) and (ancho<=796):
        c = canvas.Canvas("proteccion.pdf", pagesize=(1123,796))
        c.drawImage(archi,0,0)
        c.showPage()
        c.save()



