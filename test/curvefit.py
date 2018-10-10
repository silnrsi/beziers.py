import unittest
from beziers.utils.curvefitter import CurveFit
from beziers.path import BezierPath
from beziers.point import Point

class CurveFitterMethods(unittest.TestCase):
  def test_cf1(self):
    nodes = [
      Point(122,102), Point(35,200), Point(228,145), Point(190,46)
    ]
    t = CurveFit._leftTangent(nodes)
    self.assertAlmostEqual(t.x, -0.663890062102)
    self.assertAlmostEqual(t.y,0.747830184896)
    t = CurveFit._rightTangent(nodes)
    self.assertAlmostEqual(t.x,-0.3583470773350791)
    self.assertAlmostEqual(t.y, -0.9335884383203376)

  def test_cf2(self):
    nodes = [
      Point(100,50),
      Point(50,150),
      Point(100,220),
      Point(200,200),
      Point(250,80),
      Point(220,50)
    ]
    path = BezierPath.fromPoints(nodes)
    segs = path.asSegments()
    self.assertEqual(len(segs),2)
    self.assertEqual(segs[0].start, Point(100.0, 50.0))
    self.assertAlmostEqual(segs[0][1].x, 83.333333333)
    self.assertAlmostEqual(segs[0][1].y, 83.333333333)
    self.assertEqual(segs[0].end, Point(50.0, 150.0))
    self.assertAlmostEqual(segs[1][1].x, 50)
    self.assertAlmostEqual(segs[1][1].y, 302.43214862720026)
    self.assertEqual(segs[1].end, Point(220.0, 50.0))
    # import matplotlib.pyplot as plt
    # fig, ax = plt.subplots()
    # path.plot(ax)
    # plt.show()
