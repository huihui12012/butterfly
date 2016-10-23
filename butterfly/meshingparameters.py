# coding=utf-8
"""Butterfly Meshing Parameters.

Collection of meshing parameters for blockMesh and snappyHexMesh.
"""
from .grading import SimpleGrading
from copy import deepcopy


class MeshingParameters(object):
    """Meshing parameters.

    Attributes:
        cellSizeXYZ: Cell size in (x, y, z) as a tuple (default: length / 5).
        grading: A simpleGrading (default: simpleGrading(1, 1, 1)).
        locationInMesh: A tuple for the location of the mesh to be kept.
        globRefineLevel: A tuple of (min, max) values for global refinment.
    """

    def __init__(self, cellSizeXYZ=None, grading=None, locationInMesh=None,
                 globRefineLevel=None):
        """Init meshing parameters."""
        self.cellSizeXYZ = None if not cellSizeXYZ else tuple(cellSizeXYZ)
        self.grading = grading
        self.locationInMesh = locationInMesh
        self.globRefineLevel = None if not globRefineLevel else tuple(globRefineLevel)

    @property
    def grading(self):
        """A simpleGrading (default: simpleGrading(1, 1, 1))."""
        return self.__grading

    @grading.setter
    def grading(self, g):
        self.__grading = g if g else SimpleGrading()

        assert hasattr(self.grading, 'isSimpleGrading'), \
            'grading input ({}) is not a valid simpleGrading.'.format(g)

    def duplicate(self):
        """Return a copy of this object."""
        return deepcopy(self)

    def ToString(self):
        """Overwrite .NET ToString method."""
        return self.__repr__()

    def __repr__(self):
        """Meshing parameters representation."""
        return "MeshingParameters::{}".format(
            '::'.join((str(i).replace('\n', '').replace('\t', ' ')
                       for i in (self.cellSizeXYZ, self.grading) if i))
        )