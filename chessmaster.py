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
        xvar = tile[0]
        yvar = int(tile[1])
        yvar -= 1

        if xvar not in 'abcdefgh':
            return None

        if 0 > yvar < 7:
            return None

        if xvar == 'a':
            xvar = 0
        elif xvar == 'b':
            xvar = 1
        elif xvar == 'c':
            xvar = 2
        elif xvar == 'd':
            xvar = 3
        elif xvar == 'e':
            xvar = 4
        elif xvar == 'f':
            xvar = 5
        elif xvar == 'g':
            xvar = 6
        elif xvar == 'h':
            xvar = 7
        else:
            return None

        return (xvar, yvar)

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


class Rook(ChessPiece):
    '''Makes a Rook piece'''
    prefix = 'R'

    def __init__(self, position):
        self.position = position

    def is_legal_move(self, position):
        '''Makes Rook moves straight
        Checking to see if the x or y coordinates are the same
        Args: position'''

        oldposition = self.algebraic_to_numeric(self.position)
        newposition = self.algebraic_to_numeric(position)

        if oldposition[0] == newposition[0] or oldposition[1] == newposition[1]:
            return True
        else:
            return False


class Bishop(ChessPiece):
    '''Makes a Bishop'''
    prefix = 'B'

    def __init__(self, position):
        self.position = position

    def is_legal_move(self, position):
        '''Makes Bishop move diagonally
        Checking to see if the x or y coordinates are the same
        Args: position'''
        oldpos = self.algebraic_to_numeric(self.position)
        newpos = self.algebraic_to_numeric(position)

        if oldpos[0] - newpos[0] == oldpos[1] - newpos[1]:
            return True
        elif oldpos[0] - newpos[0] == -(oldpos[1] - newpos[1]):
            return True
        else:
            return False


class King(ChessPiece):
    '''Makes a King, subclass to ChessPiece'''
    prefix = 'K'

    def __init__(self, position):
        self.position = position

    def is_legal_move(self, position):
        '''King can move in any direction but only 1 tile at a time'''
        oldposition = self.algebraic_to_numeric(self.position)
        newposition = self.algebraic_to_numeric(position)
        if (oldposition[0] - newposition[0]) != 1 or -1:
            return False
        elif (oldposition[1] - newposition[1]) != 1 or -1:
            return False
        else:
            return True


class ChessMatch(object):
    """The pieces on a chess board.

    Args:
        pieces (None): defaults that there are no pieces on the board

    Attributes:
        pieces (None):
    """

    def __init__(self, pieces=None):
        if pieces is None:
            self.reset()
        else:
            self.pieces = pieces
            self.log = []

    def reset(self):
        '''resets board to starting places'''
        self.log = []
        self.pieces = {
            'Ra1': Rook('a1'),
            'Rh1': Rook('h1'),
            'Ra8': Rook('a8'),
            'Rh8': Rook('h8'),
            'Bc1': Bishop('c1'),
            'Bf1': Bishop('f1'),
            'Bc8': Bishop('c8'),
            'Bf8': Bishop('f8'),
            'Ke1': King('e1'),
            'Ke8': King('e8'),
        }

    def move(self, fullnot, dest):
        '''moves piece to new position'''
        a_tup = self.pieces[fullnot].move(dest)
        if a_tup is False:
            return False
        else:
            self.log.append(a_tup)
            new_key = self.pieces[fullnot].prefix + dest
            self.pieces[new_fullnot] = self.pieces.pop(fullnot)
            return a_tup

    def __len__(self):
        return len(self.log)