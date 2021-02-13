import graphics.threeD_Graphics.cuboid as cb
from graphics.threeD_Graphics.sphere import sphere_circum as sp
from graphics.threeD_Graphics.sphere import sphere_area
from graphics import reactangle
from graphics import circle as cr

r=int(input("Enter the radius of circle :"))
cr.cir_area(r)
cr.cir_perimeter(r)

l=int(input("Enter the Length of Reactangle : "))
b=int(input("Enter the Breadth of Reactangle : "))
reactangle.rect_area(l,b)
reactangle.rect_perimeter(l,b)


s=int(input("Enter the radius of Sphere : "))
sp(s)
sphere_area(s)




lc=int(input("Enter the Length  of Cuboid : "))
wc=int(input("Enter the Width  of Cuboid : "))
hc=int(input("Enter the Height  of Cuboid : "))
cb.cuboid_area(lc,wc,hc)
cb.cuboid_perimeter(lc,wc,hc)
