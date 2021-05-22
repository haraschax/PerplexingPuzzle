from helpers import Piece
import copy
import numpy as np

all_pieces = {}
all_pieces[2] = []
all_pieces[2].append(Piece(np.array([[0,1,0,1,0],
                                  [0,0,1,1,0],
                                  [0,0,1,0,0],
                                  [1,0,1,1,0]], dtype=bool), holes=False))
all_pieces[2].append(Piece(np.array([[1,1,1,1,1],
                                  [0,1,1,0,1],
                                  [0,0,1,1,0],
                                  [0,0,1,0,0]], dtype=bool), holes=True))
all_pieces[2].append(Piece(np.array([[0,1,1,0,1],
                                  [0,0,1,0,0],
                                  [0,1,0,1,0],
                                  [0,1,1,1,0]], dtype=bool), holes=True))
all_pieces[2].append(Piece(np.array([[1,0,1,1,0],
                                  [0,0,1,0,0],
                                  [0,1,1,0,0],
                                  [1,1,1,1,1]], dtype=bool), holes=False))


all_pieces[3] = []
all_pieces[3].append(Piece(np.array([[0,1,1,0,1],
                             [0,0,1,1,1],
                             [0,1,1,0,0],
                             [1,0,0,1,0]], dtype=bool), holes=True))
all_pieces[3].append(Piece(np.array([[1,1,1,1,1],
                             [0,1,0,0,1],
                             [0,0,1,0,0],
                             [1,0,0,0,1]], dtype=bool), holes=False))
all_pieces[3].append(Piece(np.array([[0,1,1,0,1],
                             [0,0,1,1,0],
                             [1,1,1,1,1],
                             [0,1,0,1,0]], dtype=bool), holes=True))
all_pieces[3].append(Piece(np.array([[0,0,1,1,0],
                             [1,1,1,0,0],
                             [0,1,1,0,0],
                             [1,0,1,1,0]], dtype=bool), holes=False))
all_pieces[3].append(Piece(np.array([[0,1,1,0,0],
                             [1,1,1,1,0],
                             [1,0,1,1,0],
                             [0,0,1,0,0]], dtype=bool), holes=True))


all_pieces[4] = []
all_pieces[4].append(Piece(np.array([[1,0,1,1,0],
                            [0,0,1,0,0],
                            [0,0,1,1,0],
                            [1,1,0,0,0]], dtype=bool), holes=False))
all_pieces[4].append(Piece(np.array([[0,1,0,1,0],
                            [0,1,1,0,1],
                            [0,1,1,0,0],
                            [1,0,0,0,1]], dtype=bool), holes=True))
all_pieces[4].append(Piece(np.array([[0,1,1,0,0],
                            [0,1,1,0,0],
                            [0,0,1,1,1],
                            [1,0,0,0,1]], dtype=bool), holes=False))
all_pieces[4].append(Piece(np.array([[1,0,0,0,1],
                            [0,0,0,1,1],
                            [0,0,1,1,0],
                            [1,1,1,0,0]], dtype=bool), holes=True))
all_pieces[4].append(Piece(np.array([[0,1,1,1,0],
                            [1,1,0,0,1],
                            [0,0,1,1,0],
                            [1,1,1,1,1]], dtype=bool), holes=False))
all_pieces[4].append(Piece(np.array([[1,1,1,0,0],
                            [1,1,0,1,0],
                            [1,1,1,0,0],
                            [0,0,1,0,0]], dtype=bool), holes=True))
all_pieces[4].append(Piece(np.array([[0,1,0,1,0],
                            [0,1,0,0,1],
                            [0,1,0,1,0],
                            [0,1,0,1,1]], dtype=bool), holes=False))

all_pieces[5] = []
all_pieces[5].append(Piece(np.array([[1,1,1,0,0],
                                     [0,0,1,1,0],
                                     [0,1,0,1,0],
                                     [0,1,0,1,0]], dtype=bool), holes=True))
all_pieces[5].append(Piece(np.array([[0,1,0,1,0],
                                     [0,0,1,1,1],
                                     [1,0,0,0,1],
                                     [0,1,1,0,1]], dtype=bool), holes=False))
all_pieces[5].append(Piece(np.array([[0,0,1,0,0],
                                     [1,0,1,1,0],
                                     [1,0,1,1,0],
                                     [1,1,0,1,0]], dtype=bool), holes=True))
all_pieces[5].append(Piece(np.array([[0,0,1,1,1],
                                     [1,1,1,0,0],
                                     [0,1,0,1,1],
                                     [1,1,0,1,1]], dtype=bool), holes=False))
all_pieces[5].append(Piece(np.array([[1,0,0,0,1],
                                     [0,1,1,0,1],
                                     [0,1,1,1,0],
                                     [1,1,0,1,0]], dtype=bool), holes=True))
all_pieces[5].append(Piece(np.array([[0,1,1,0,1],
                                     [0,1,1,1,0],
                                     [0,0,1,1,1],
                                     [0,1,1,0,1]], dtype=bool), holes=False))
all_pieces[5].append(Piece(np.array([[0,1,1,0,0],
                                     [0,1,0,0,0],
                                     [1,1,1,1,1],
                                     [0,0,1,1,0]], dtype=bool), holes=True))
all_pieces[5].append(Piece(np.array([[0,1,0,1,0],
                                     [0,0,1,1,1],
                                     [0,1,0,1,1],
                                     [0,1,1,1,1]], dtype=bool), holes=False))
all_pieces[5].append(Piece(np.array([[0,1,1,0,0],
                                     [1,1,0,0,0],
                                     [0,0,1,1,0],
                                     [0,0,0,1,0]], dtype=bool), holes=False))

all_pieces[6] = []
all_pieces[6].append(Piece(np.array([[0,1,0,1,0],
                                     [0,0,1,0,0],
                                     [0,0,1,0,0],
                                     [1,1,0,0,0]], dtype=bool), holes=False))
all_pieces[6].append(Piece(np.array([[0,0,1,1,0],
                                     [0,0,1,1,0],
                                     [0,1,0,1,0],
                                     [0,1,1,0,1]], dtype=bool), holes=True))
all_pieces[6].append(Piece(np.array([[0,0,1,0,0],
                                     [0,1,1,0,1],
                                     [0,0,1,1,0],
                                     [0,1,0,1,1]], dtype=bool), holes=False))
all_pieces[6].append(Piece(np.array([[0,1,1,1,0],
                                     [0,1,1,0,0],
                                     [0,1,0,1,0],
                                     [1,0,0,1,0]], dtype=bool), holes=True))
all_pieces[6].append(Piece(np.array([[1,0,0,0,1],
                                     [1,1,1,0,0],
                                     [0,1,1,0,0],
                                     [0,1,1,0,1]], dtype=bool), holes=False))
all_pieces[6].append(Piece(np.array([[0,0,1,1,0],
                                     [1,0,0,1,1],
                                     [0,1,0,1,0],
                                     [0,0,1,1,0]], dtype=bool), holes=True))
all_pieces[6].append(Piece(np.array([[0,1,1,0,0],
                                     [1,0,1,1,0],
                                     [0,0,1,1,0],
                                     [0,1,0,1,0]], dtype=bool), holes=False))
all_pieces[6].append(Piece(np.array([[0,0,0,1,1],
                                     [0,0,1,1,0],
                                     [1,1,1,0,0],
                                     [0,1,1,0,0]], dtype=bool), holes=True))
all_pieces[6].append(Piece(np.array([[0,0,1,1,1],
                                     [0,1,1,0,0],
                                     [0,1,1,0,1],
                                     [0,1,0,1,0]], dtype=bool), holes=False))
all_pieces[6].append(Piece(np.array([[1,0,0,0,1],
                                     [0,1,1,0,1],
                                     [0,1,1,0,0],
                                     [1,1,1,0,0]], dtype=bool), holes=True))
all_pieces[6].append(Piece(np.array([[0,0,1,0,0],
                                     [1,1,0,1,1],
                                     [0,0,1,1,0],
                                     [0,0,1,1,1]], dtype=bool), holes=True))

all_pieces[7] = []
all_pieces[7].append(Piece(np.array([[1,1,1,1,1],
                                     [0,1,0,1,0],
                                     [0,1,1,1,0],
                                     [1,1,1,0,0]], dtype=bool), holes=True))
all_pieces[7].append(Piece(np.array([[0,0,1,0,0],
                                     [1,0,0,1,0],
                                     [0,1,0,1,0],
                                     [1,0,1,1,0]], dtype=bool), holes=True))
all_pieces[7].append(Piece(np.array([[0,1,1,0,1],
                                     [0,0,1,1,1],
                                     [0,0,1,1,1],
                                     [0,0,1,0,0]], dtype=bool), holes=True))
all_pieces[7].append(Piece(np.array([[0,0,0,1,0],
                                     [0,1,0,1,0],
                                     [1,1,0,1,1],
                                     [1,1,1,0,0]], dtype=bool), holes=False))
all_pieces[7].append(Piece(np.array([[1,1,1,0,0],
                                     [0,1,1,0,0],
                                     [1,0,1,1,0],
                                     [0,1,0,1,0]], dtype=bool), holes=True))
all_pieces[7].append(Piece(np.array([[0,1,1,1,0],
                                     [0,1,0,1,0],
                                     [0,1,1,0,0],
                                     [0,0,1,1,1]], dtype=bool), holes=False))
all_pieces[7].append(Piece(np.array([[1,0,1,1,0],
                                     [1,1,0,1,0],
                                     [0,1,1,0,0],
                                     [1,0,1,1,0]], dtype=bool), holes=True))
all_pieces[7].append(Piece(np.array([[0,1,1,0,0],
                                     [0,0,1,0,0],
                                     [0,1,1,0,0],
                                     [1,1,0,0,0]], dtype=bool), holes=False))
all_pieces[7].append(Piece(np.array([[0,0,0,1,1],
                                     [1,1,1,0,0],
                                     [0,0,1,1,0],
                                     [0,0,1,0,0]], dtype=bool), holes=True))
all_pieces[7].append(Piece(np.array([[0,1,1,0,1],
                                     [0,0,1,1,1],
                                     [0,0,1,0,0],
                                     [1,1,1,0,0]], dtype=bool), holes=False))
all_pieces[7].append(Piece(np.array([[0,1,1,1,0],
                                     [1,1,0,0,0],
                                     [1,1,1,0,0],
                                     [0,0,1,1,0]], dtype=bool), holes=True))
all_pieces[7].append(Piece(np.array([[0,0,1,1,1],
                                     [1,1,1,0,0],
                                     [0,0,1,0,0],
                                     [0,1,1,0,0]], dtype=bool), holes=False))
all_pieces[7].append(Piece(np.array([[0,0,1,0,0],
                                     [0,1,1,0,0],
                                     [0,0,1,1,1],
                                     [0,1,1,0,1]], dtype=bool), holes=False))



def get_unsolved_grid(size=2):
  if size < 2 or size > 7:
    raise NotImplementedError("Please enter a number between 2 and 7")
  base_grid = np.array(all_pieces[2]).reshape(2,2)
  for i in range(3, size+1):
    larger_grid = np.zeros((i,i), dtype=object)
    larger_grid[1:,:-1] = base_grid[:,:]
    larger_grid[0,:] = all_pieces[i][:i]
    larger_grid[1:,-1] = all_pieces[i][i:]
    base_grid = larger_grid
  return copy.deepcopy(base_grid)
