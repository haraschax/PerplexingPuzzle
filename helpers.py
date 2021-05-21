import numpy as np

MARGIN = 7
NOTCH_SIZE = 5
IMG_SIZE = NOTCH_SIZE * (5 + 8) + 2*MARGIN


def draw_notch(img, i, notch):
  img[MARGIN, MARGIN + NOTCH_SIZE*(2 + i*2): MARGIN + NOTCH_SIZE*(3 + i*2)] = 0
  img[MARGIN -notch*NOTCH_SIZE, MARGIN + NOTCH_SIZE*(2 + i*2): MARGIN + NOTCH_SIZE*(3 + i*2) + 1] = 1
  if notch == 1:
    img[MARGIN - NOTCH_SIZE+1: MARGIN +1, MARGIN + NOTCH_SIZE*(2 + i*2)] = 1
    img[MARGIN - NOTCH_SIZE+1: MARGIN +1, MARGIN + NOTCH_SIZE*(3 + i*2)] = 1
  elif notch == -1:
    img[MARGIN: MARGIN + NOTCH_SIZE+1, MARGIN + NOTCH_SIZE*(2 + i*2)] = 1
    img[MARGIN: MARGIN + NOTCH_SIZE+1, MARGIN + NOTCH_SIZE*(3 + i*2)] = 1

def draw_side(img, sidx, notches):
  img = np.rot90(img, sidx)
  img[MARGIN, MARGIN:-MARGIN] = 1
  for nidx, notch in enumerate(notches):
    draw_notch(img, nidx, notch)
  img = np.rot90(img, -sidx)
  return img


class Piece(object):
  def __init__(self, sides, holes):
    assert len(sides.shape) == 2
    assert sides.shape[0] == 4
    assert sides.shape[1] == 5
    self.holes = holes
    self.sides = sides

  def draw(self):
    img = np.zeros((IMG_SIZE, IMG_SIZE), dtype=bool)
    signed_sides = np.zeros(self.sides.shape, dtype=int)
    if self.holes:
      signed_sides[self.sides] = -1
    else:
      signed_sides[self.sides] = 1
    for sidx, side in enumerate(signed_sides):
      img = draw_side(img, sidx, side)
    return img

  def check_right(self, piece):
    if piece is None:
      return True
    else:
      return (self.sides[1] == piece.sides[3,::-1]).all() and self.holes != piece.holes

  def check_down(self, piece):
    if piece is None:
      return True
    else:
      return (self.sides[2] == piece.sides[0,::-1]).all() and self.holes != piece.holes

  #def rotate(self, k=1):
  #  self.sides = np.roll(self.sides, k, axis=0)

  def rotate(self):
    temp = np.copy(self.sides[3])
    self.sides[1:4] = self.sides[0:3]
    self.sides[0] = temp

  def flip(self):
    self.sides = self.sides[:,::-1]
    backup = np.copy(self.sides[1])
    self.sides[1] = self.sides[3]
    self.sides[3] = backup

def draw_grid(grid):
  n = len(grid)
  rows = []
  for i in range(n):
    rows.append(np.hstack([x.draw() if x is not None else np.zeros((IMG_SIZE, IMG_SIZE), dtype=bool) for x in grid[i]]))
  return np.vstack(rows)

def check_grid(grid):
  n = len(grid)
  for i in range(n):
    for j in range(n):
      if grid[i,j] is None:
        continue
      if j < n-1 and not grid[i, j].check_right(grid[i, j+1]):
        return False
      if i < n-1 and not grid[i, j].check_down(grid[i+1, j]):
        return False
  return True
