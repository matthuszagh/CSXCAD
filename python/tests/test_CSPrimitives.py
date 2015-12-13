# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:49:46 2015

@author: thorsten
"""

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np

from pyCSXCAD import ParameterObjects
from pyCSXCAD import CSProperties
from pyCSXCAD import CSPrimitives

pset = ParameterObjects.ParameterSet()
metal = CSProperties.CSPropMetal(pset)

# TEST BOX
box = CSPrimitives.CSPrimBox(pset, metal)
start = np.array([0,10,0])
box.SetStart(start)
assert (box.GetStart()==np.array([0,10,0])).all()

stop = np.array([10,0,10])
box.SetStop(stop)
assert (box.GetStop()==stop).all()

assert box.GetID()==0
assert box.GetType()==1
assert box.GetTypeName()=='Box'

assert box.GetPriority()==0
box.SetPriority(10)
assert box.GetPriority()==10

print(box.GetBoundBox())

# TEST Cylinder
cyl = CSPrimitives.CSPrimCylinder(pset, metal)
cyl.SetStart(start)
assert (cyl.GetStart()==start).all()

cyl.SetStop(stop)
assert (cyl.GetStop()==stop).all()

assert cyl.GetID()==1
assert cyl.GetType()==5
assert cyl.GetTypeName()=='Cylinder'

assert cyl.GetPriority()==0

cyl.SetRadius(5)
assert cyl.GetRadius()==5.0

print(cyl.GetBoundBox())

# TEST Cylinder-Shell
cyl_shell = CSPrimitives.CSPrimCylindricalShell(pset, metal)
cyl_shell.SetStart(start)
assert (cyl_shell.GetStart()==start).all()

cyl_shell.SetStop(stop)
assert (cyl_shell.GetStop()==stop).all()

assert cyl_shell.GetID()==2
assert cyl_shell.GetType()==6
assert cyl_shell.GetTypeName()=='CylindricalShell'

assert cyl_shell.GetPriority()==0

cyl_shell.SetRadius(5)
assert cyl_shell.GetRadius()==5.0

cyl_shell.SetShellWidth(1.5)
assert cyl_shell.GetShellWidth()==1.5

print(cyl_shell.GetBoundBox())

# TEST Sphere
sphere = CSPrimitives.CSPrimSphere(pset, metal)
center = np.array([1.1,2.2,3.3])
sphere.SetCenter(center)
assert (sphere.GetCenter()==center).all()

assert sphere.GetID()==3
assert sphere.GetType()==3
assert sphere.GetTypeName()=='Sphere'

assert sphere.GetPriority()==0

sphere.SetRadius(5)
assert sphere.GetRadius()==5.0

print(sphere.GetBoundBox())

# TEST Sphere-Shell
sphere_shell = CSPrimitives.CSPrimSphericalShell(pset, metal)
sphere_shell.SetCenter(center)
assert (sphere_shell.GetCenter()==center).all()

assert sphere_shell.GetID()==4
assert sphere_shell.GetType()==4
assert sphere_shell.GetTypeName()=='SphericalShell'

assert sphere_shell.GetPriority()==0

sphere_shell.SetRadius(5)
assert sphere_shell.GetRadius()==5.0

sphere_shell.SetShellWidth(1.5)
assert sphere_shell.GetShellWidth()==1.5

print(sphere_shell.GetBoundBox())

# TEST Point
point = CSPrimitives.CSPrimPoint(pset, metal)
point.SetCoord(start)
assert (point.GetCoord()==start).all()

assert point.GetID()==5
assert point.GetType()==0
assert point.GetTypeName()=='Point'

print(point.GetBoundBox())

# Test polygon
poly = CSPrimitives.CSPrimPolygon(pset, metal)
x0 = np.array([0, 0, 1, 1])
x1 = np.array([0, 1, 1, 0])
poly.SetCoords(x0, x1)
o0, o1 = poly.GetCoords()
assert (o0==x0).all()
assert (o1==x1).all()

assert poly.GetQtyCoords()==4
assert poly.GetNormDir()==0
poly.SetNormDir('y')
assert poly.GetNormDir()==1
poly.SetNormDir(2)
assert poly.GetNormDir()==2

poly.SetElevation(0.123)
assert poly.GetElevation()==0.123

print(poly.GetBoundBox())

# Test Lin-Polygon
linpoly = CSPrimitives.CSPrimLinPoly(pset, metal)
linpoly.SetCoords(x0, x1)
o0, o1 = linpoly.GetCoords()
assert (o0==x0).all()
assert (o1==x1).all()

assert linpoly.GetQtyCoords()==4
assert linpoly.GetNormDir()==0
linpoly.SetNormDir('y')
assert linpoly.GetNormDir()==1
linpoly.SetNormDir(2)
assert linpoly.GetNormDir()==2

linpoly.SetElevation(0.123)
assert linpoly.GetElevation()==0.123

linpoly.SetLength(11.23)
assert linpoly.GetLength()==11.23

print(linpoly.GetBoundBox())

# Test Rot-Polygon
rotpoly = CSPrimitives.CSPrimRotPoly(pset, metal)
x0 = np.array([0, 0, 1, 1]) + 1.5
x1 = np.array([0, 1, 1, 0]) + 2.5
rotpoly.SetCoords(x0, x1)
o0, o1 = rotpoly.GetCoords()
assert (o0==x0).all()
assert (o1==x1).all()

assert rotpoly.GetQtyCoords()==4
assert rotpoly.GetNormDir()==0
rotpoly.SetNormDir('y')
assert rotpoly.GetNormDir()==1
rotpoly.SetNormDir(0)
assert rotpoly.GetNormDir()==0

rotpoly.SetRotAxisDir('z')
assert rotpoly.GetRotAxisDir()==2

rotpoly.SetAngle(0, 2*np.pi)
print(rotpoly.GetAngle())

print(rotpoly.GetBoundBox())

# Test Curve
curve = CSPrimitives.CSPrimCurve(pset, metal)
x = np.array([0, 0, 1, 1]) + 1.5
y = np.array([0, 1, 1, 0]) + 2.5
z = np.array([0, 1, 3, 4])
curve.SetPoints(x, y, z)

assert (curve.GetPoint(0)==np.array([1.5,2.5,0])).all()
assert curve.GetNumberOfPoints()==4

curve.AddPoint([10, 10, 10.5])
assert curve.GetNumberOfPoints()==5

print(curve.GetBoundBox())

curve.ClearPoints()
assert curve.GetNumberOfPoints()==0

# Test Wire
wire = CSPrimitives.CSPrimWire(pset, metal)
x = np.array([0, 0, 1, 1]) - 1.5
y = np.array([0, 1, 1, 0]) - 2.5
z = np.array([0, 1, 3, 4])
wire.SetPoints(x, y, z)

assert (wire.GetPoint(0)==np.array([-1.5,-2.5,0])).all()
assert wire.GetNumberOfPoints()==4

wire.AddPoint([10, -10, 10.5])
assert wire.GetNumberOfPoints()==5

wire.SetWireRadius(1.5)
assert wire.GetWireRadius()==1.5

print(wire.GetBoundBox())

# Test CSPrimPolyhedron
ph = CSPrimitives.CSPrimPolyhedron(pset, metal)
assert ph.GetNumVertices()==0
assert ph.GetNumFaces()==0

ph.AddVertex(0,0,0)
ph.AddVertex(0,1,0)
ph.AddVertex(1,0,0)
assert ph.GetNumVertices()==3
assert (ph.GetVertex(0)==np.array([0,0,0])).all()

ph.AddFace([0,1,2])
assert ph.GetNumFaces()==1
assert (ph.GetFace(0)==np.array([0,1,2])).all()

print(ph.GetBoundBox())

## Test CSPrimPolyhedronReader
phr = CSPrimitives.CSPrimPolyhedronReader(pset, metal)
phr.SetFilename('sphere.stl')
assert phr.ReadFile()
print(phr.GetNumVertices())
print(phr.GetNumFaces())
print(phr.GetBoundBox())

print("metal.GetQtyPrimitives()", metal.GetQtyPrimitives())

print("all passed")
