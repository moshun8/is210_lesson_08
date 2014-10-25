#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08, Chessmaster"""


class ChessPiece(object):
    """The pieces on a chess board.

    Args:
        position:

    Attributes:
        position:
    """
    
    import time
	
    prefix = ''
	
    def __init__(self, position, moves):
		self.position = position
		self.moves = []

        if self.is_legal_move(self, position) = False:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))

    def algebraic_to_numeric(self, tile):
        """Converts a string coordinate to a tuple.

        Args:
            tile (string): String coordinates of the chess piece
        """
        if len(tile) is not 2:
            return None
        x = tile[0].lower
        y = int(tile[1])
        y -= 1

        if x is not 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h':
            return None
        if 0 > y > 7:
            return None

        if x == 'a':
            x = 0
            return (x, y);
        if x == 'b':
            x = 1
            return (x, y);
        if x == 'c':
            x = 2
            return (x, y);
        if x == 'd':
            x = 3
            return (x, y);
        if x == 'e':
            x = 4
            return (x, y);
        if x == 'f':
            x = 5
            return (x, y);
        if x == 'g':
            x = 6
            return (x, y);
        if x == 'h':
            x = 7
            return (x, y);

    def is_legal_move(self, position):
        """Checks if a move is legal or not

        Args:
            position (string): String coordinates of the chess piece
        """

        if algebraic_to_numeric(position) is None:
            return False
        else:
            return True

    def move(self, position):
        if self.is_legal_move(position):
            oldposition = prefix.self.position
            newposition = prefix.position
            timestamp = time.Time()
            self.moves = [(oldposition, newposition, timestamp);]
        else:
            return False