import pygame
from vars import *
from piececlass import piece

# pieces of player white/0
pawn_1_white = piece(0, [1, 7])
pawn_2_white = piece(0, [2, 7])
pawn_3_white = piece(0, [3, 7])
pawn_4_white = piece(0, [4, 7])
pawn_5_white = piece(0, [5, 7])
pawn_6_white = piece(0, [6, 7])
pawn_7_white = piece(0, [7, 7])
pawn_8_white = piece(0, [8, 7])

rook_left_white = piece(0, [1, 8])
rook_right_white = piece(0, [8, 8])

knight_left_white = piece(0, [2, 8])
knight_right_white = piece(0, [7, 8])

bishop_left_white = piece(0, [3, 8])
bishop_right_white = piece(0, [6, 8])

queen_white = piece(0, [4, 8])
king_white = piece(0, [5, 8])


# pieces of player black/1
pawn_1_black = piece(1, [1, 2])
pawn_2_black = piece(1, [2, 2])
pawn_3_black = piece(1, [3, 2])
pawn_4_black = piece(1, [4, 2])
pawn_5_black = piece(1, [5, 2])
pawn_6_black = piece(1, [6, 2])
pawn_7_black = piece(1, [7, 2])
pawn_8_black = piece(1, [8, 2])

rook_left_black = piece(1, [1, 1])
rook_right_black = piece(1, [8, 1])

knight_left_black = piece(1, [2, 1])
knight_right_black = piece(1, [7, 1])

bishop_left_black = piece(1, [3, 1])
bishop_right_black = piece(1, [6, 1])

queen_black = piece(1, [4, 1])
king_black = piece(1, [5, 1])


pieces = [pawn_1_black, pawn_2_black, pawn_3_black, pawn_4_black, pawn_5_black, pawn_6_black, pawn_7_black, pawn_8_black, rook_left_black, rook_right_black, bishop_left_black, bishop_right_black, knight_left_black, knight_right_black, queen_black, king_black, pawn_1_white, pawn_2_white, pawn_3_white, pawn_4_white, pawn_5_white, pawn_6_white, pawn_7_white, pawn_8_white, rook_left_white, rook_right_white, bishop_left_white, bishop_right_white, knight_left_white, knight_right_white, queen_white, king_white]
