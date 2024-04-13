import os

class Director:
    __builder = None
    
    def setBuilder(self, builder):
        self.__builder = builder
	    
    def getPlane(self):
        plane = Plane()

        landingGear = self.__builder.getLandingGear()
        plane.setLandingGear(landingGear)

        i = 0
        while i < 2:
            turbines = self.__builder.getTurbines()
            plane.attachTurbines(turbines)
            i += 1

        j = 0
        while j < 2:
            wings = self.__builder.getWings()
            plane.attachWings(wings)
            j += 1

        body = self.__builder.getBody()
        plane.setBody(body)

        return plane


class Plane:
    def __init__(self):
        self.__wings = list()
        self.__turbines = list()
        self.__landingGear = None
        self.__body = None

    def attachWings(self, wings):
        self.__wings.append(wings)

    def attachTurbines(self, turbines):
        self.__turbines.append(turbines)

    def setLandingGear(self, landingGear):
        self.__landingGear = landingGear

    def setBody(self, body):
        self.__body = body

    def specification(self):
        print ("Forma del tren de aterrizaje: %s" % (self.__landingGear.shape))
        print ("Tamaño de alas: %d\'" % (self.__wings[0].size))
        print ("Span de alas: %d\'" % (self.__wings[0].span))
        print ("Tamaño de las turbinas: %d\'" % (self.__turbines[0].size))
        print ("Caballos de fuerza de turbinas: %d\'" % (self.__turbines[0].horsepower))
        print ("Forma del cuerpo: %s" % (self.__body.shape))
        print ("Material del cuerpo: %s" % (self.__body.material))
        print ("Longitud del cuerpo: %s" % (self.__body.length))

class Builder:
    def getLandingGear(self): pass
    def getTurbines(self): pass
    def getWings(self): pass
    def getBody(self): pass

class PlaneBuilder(Builder):
    
    def getLandingGear(self):
        gear = LandingGear()
        gear.shape = "Retractiles"
        return gear
    
    def getTurbines(self):
        turb = Turbine()
        turb.horsepower = 10000
        turb.size = 22 
        return turb
    
    def getWings(self):
        wing = Wings()
        wing.span = 60
        wing.size = 22  
        return wing
    
    def getBody(self):
        body = Body()
        body.shape = "Cilíndrico"
        body.material = "Aluminio"
        body.length = 60  # en metros
        return body


class LandingGear:
    shape = None

class Turbine:
    horsepower = None
    size = None

class Wings:
    span = None
    size = None

class Body:
    shape = None
    material = None
    length = None

def main():

    planeBuilder = PlaneBuilder() # initializing the class
    director = Director() 
    director.setBuilder(planeBuilder)
    plane = director.getPlane()
    plane.specification()
    print ("\n\n")

if __name__ == "__main__":
    os.system("cls")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")

    main()