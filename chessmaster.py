#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08, Chessmaster"""


class ChessPiece(object):
    """The pieces on a chess board.

    Args:
        position (string): where the piece is or moving to

    Attributes:
        position (string): where the piece is or moving to

    Functions:
        
    """
    
    import time
	
    prefix = ''
	
    def __init__(self, position):
        self.moves = []

        if self.is_legal_move(position) is False:
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            print "prefix: " + self.prefix + " position: " + self.position

    def algebraic_to_numeric(self, tile):
        """Converts a string coordinate to a tuple.

        Args:
            tile (string): String coordinates of the chess piece
        """
        if len(tile) is not 2:
            return None
        x = tile[0]
        y = int(tile[1])
        y -= 1

        if x not in 'abcdefg':
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

        if self.algebraic_to_numeric(position) is None:
            return False
        else:
            return True

    def move(self, position):
        """Makes a tuple with old position, new one, and time

        Args:
            position (string): String coordinates of the chess piece
        """
        if self.is_legal_move(position):
            oldposition = self.position
            self.position = position
            timestamp = self.time.time()
            the_tup = (oldposition, position, timestamp)
            self.moves.append(the_tup)
            return the_tup
        else:
            return False

piece = ChessPiece('a1')
print piece
print piece.position
print piece.moves
print piece.algebraic_to_numeric('e7')
print piece.algebraic_to_numeric('j9')
print piece.move('j9')
print piece.move('e7')
print piece.position
print piece.moves
print piece.move('b2')
print piece.moves