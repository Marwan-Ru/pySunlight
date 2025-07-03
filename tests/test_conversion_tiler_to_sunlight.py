import unittest
import numpy as np

from src.Converters import TilerToSunlight
from src import pySunlight

class TestConversionTilerToSunlight(unittest.TestCase):
    def test_numpy_to_vec3(self):
        intarray = np.array([1, 2, 3])
        intvec3 = pySunlight.Vec3d(1, 2, 3)

        resultint = TilerToSunlight.convert_numpy_to_vec3(intarray)

        dvec3 = pySunlight.Vec3d(1.247, 2.4, 3.124534)

        resultd = TilerToSunlight.convert_numpy_to_vec3(np.array([1.247, 2.4, 3.124534]))

        self.assertTrue(intvec3 == resultint and dvec3 == resultd, "Wrong numpy to vec3 conversion")
        return True