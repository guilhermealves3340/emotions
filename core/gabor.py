

import numpy as np
from skimage.filters import gabor_kernel
import cv2


class KernelParams:
    def __init__(self, wavelength, orientation):
        self.wavelength = wavelength
        self.orientation = orientation

    def __hash__(self):
        return hash((self.wavelength, self.orientation))

    def __eq__(self, other):
        return (self.wavelength, self.orientation) == \
               (other.wavelength, other.orientation)

    def __ne__(self, other):
        return not(self == other)


class GaborBank:
    def __init__(self, w = [4, 7, 10, 13],
                       o = [i for i in np.arange(0, np.pi, np.pi / 8)]):
        self._wavelengths = w
        self._orientations = o
        self._kernels = {}
        for wavelength in self._wavelengths:
            for orientation in self._orientations:
                frequency = 1 / wavelength
                kernel = gabor_kernel(frequency, orientation)
                par = KernelParams(wavelength, orientation)
                self._kernels[par] = kernel

    def filter(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        responses = []
        for wavelength in self._wavelengths:
            for orientation in self._orientations:
                frequency = 1 / wavelength
                par = KernelParams(wavelength, orientation)
                kernel = self._kernels[par]
                real = cv2.filter2D(image, cv2.CV_32F, kernel.real)
                imag = cv2.filter2D(image, cv2.CV_32F, kernel.imag)
                mag = cv2.magnitude(real, imag)
                cv2.normalize(mag, mag, -1, 1, cv2.NORM_MINMAX)
                responses.append(mag)
        return np.array(responses)