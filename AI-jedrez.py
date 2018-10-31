import chess
import chess.svg
from IPython.display import SVG

board = chess.Board()

board

board.push_san("e4")

board

SVG(chess.svg.board(board=board))
