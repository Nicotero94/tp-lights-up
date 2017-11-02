import unittest
import usuario

class UsuarioTest(unittest.TestCase):

    def testSaludarDeberiaDevolverHola(self):

        #Arrange
        saludoEsperado = "Hola"

        #Act
        saludoRecibido = usuario.saludar()

        #Assert
        self.assertEquals(saludoEsperado,saludoRecibido)