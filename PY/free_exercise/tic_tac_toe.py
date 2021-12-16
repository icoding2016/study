"""
A Tic-Tac-Toe game.

2 Players:  X and O
game board (N*N), 
the first to have M chesses in a line wins.  (N>=M)

The simplest (classic) version is a 3x3 board, M=3
e.g  a Tie game with X start first
X O X
X O X
O X O

"""

# from copy import deepcopy
import typing as t


class TicTacToe():
    def __init__(self,board_size:int=3, winning_size:int=3) -> None:
        self.board_size = board_size
        self.winning_size = winning_size
        self.ai_flag = 'O'
        self.ai_point = 1
        self.player_flag = 'X'
        self.player_point = -1
        self._resetBoard()

    def _resetBoard(self):
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]     # NxN board

    def _boardFull(self):
        for r in range(self.board_size):
            if '' in self.board[r]:
                return False
        return True

    def _findEmpties(self, board:list[list[str]]=None):
        empties = []
        if not board:
            board = self.board
        for y in range(self.board_size):
            for x in range(self.board_size):
                if not board[y][x]:
                    empties.append((x,y))
        return empties

    def checkWinner(self, board:list[list[str]]=None) -> t.Optional[str]:
        winner = None
        if not board:
            board = self.board
        for y in range(self.board_size):
            for x in range(self.board_size):
                checks = [board[y][x:x+self.winning_size+1], 
                          [board[y+j][x] for j in range(self.winning_size) if 0<=y+j<self.board_size],
                          [board[y+i][x-i] for i in range(self.board_size) if y+i<self.board_size and x-i>=0],
                          [board[y+i][x+i] for i in range(self.board_size) if y+i<self.board_size and x+i<self.board_size]
                         ]
                for chk in checks:
                    if len(chk)>=self.winning_size and chk[0] and all([chk[0]==c for c in chk[1:]]):
                        winner = chk[0]
                        break
        return winner

    def play(self, player_first:bool=True):
        self._resetBoard()
        ai_turn = not player_first
        while True:
            if ai_turn:
                x, y = self.aiInput()
                self.board[y][x] = self.ai_flag
                ai_turn = False
            else:
                x, y = self.playersInput()
                self.board[y][x] = self.player_flag
                ai_turn = True
            winner = self.checkWinner()
            self.showBoard()
            if winner == self.ai_flag:
                print(f"AI('{self.ai_flag}') win.")
                return
            elif winner == self.player_flag:
                print(f"Player('{self.player_flag}') win.")
                return
            elif self._boardFull():
                print("Tie.")
                return
            
    
    def playersInput(self):
        if self._boardFull():
            return None
        while True:
            player_input = input("Player(X)'s turn:'x,y':")
            player_input.replace(' ', '')
            x, y = (int(e) for e in player_input.split(','))
            try:
                if self.board[y][x]:
                    print(f"{x},{y} is already occupied")
                else:
                    return (x,y)
            except IndexError:
                print(f"index out of range. board {self.board_size}x{self.board_size}, index (0~{self.board_size-1})")

    def aiInput(self):
        if self._boardFull():
            return None
        print(f"AI('{self.ai_flag}')'s turn:")
        return self._optimalMove(ai=True)

    def _optimalMove(self, ai:bool, board:list[list[str]]=None) -> tuple[int]:
        """The optimal next move for ai or player.
           Assume AI win for maximum +, player win for minimum -.
           If ai, then try to find the maximum result from all the possible next move.
           else, try to find the minimum result from all the possible next move.
        """
        if self._boardFull():
            return None
        if not board:
            board = self.board                              
        empties = self._findEmpties(board)
        scores = {e:0 for e in empties}
        flag = self.ai_flag if ai else self.player_flag        
        for x,y in empties:
            board[y][x] = flag
            scores[(x,y)] = self._scoring(not ai, board)
            board[y][x] = ''
        if ai:
            move = max(scores, key=lambda mv:scores[mv])
        else:
            move = min(scores, key=lambda mv:scores[mv])
        return move

    def _scoring(self, ai_player:bool, board:list[list[str]]=None) -> tuple[int,int]:
        """Assess the the score of current board, if both players choose the optimal move in the following steps.
           return (result, score)
               result = ai_point if ai will win else player_point, 0 if tie. This is the main factor to make judgement
               score = the total of the results from the different branches of next step. 
                       Uses to find the best move when the results from different branches are the same.
        """
        if not board:
            board = self.board
        
        winner = self.checkWinner(board)
        if winner:
            return self.ai_point if winner==self.ai_flag else self.player_point

        # total_score = 0
        result = -1 if ai_player else 1
        flag = self.ai_flag if ai_player else self.player_flag
        for y in range(self.board_size):
            for x in range(self.board_size):
                if board[y][x] == '':
                    board[y][x] = flag
                    r = self._scoring(False, board) if ai_player else self._scoring(True, board)
                    # total_score += r
                    result = max(result, r) if ai_player else min(result, r)
                    board[y][x] = ''
        return result

    # def _scoring(self, ai_player:bool, board:list[list[str]]=None) -> tuple[int,int]:
    #     """Assess the the score of current board, if both players choose the optimal move in the following steps.
    #        return (result, score)
    #            result = ai_point if ai will win else player_point, 0 if tie. This is the main factor to make judgement
    #            score = the total of the results from the different branches of next step. 
    #                    Uses to find the best move when the results from different branches are the same.
    #     """
    #     if not board:
    #         board = self.board
        
    #     winner = self.checkWinner(board)
    #     if winner:
    #         return (self.ai_point, self.ai_point) if winner==self.ai_flag else (self.player_point, self.player_point)

    #     total_score = 0
    #     result = -1 if ai_player else 1
    #     flag = self.ai_flag if ai_player else self.player_flag
    #     for y in range(self.board_size):
    #         for x in range(self.board_size):
    #             if board[y][x] == '':
    #                 board[y][x] = flag
    #                 r, _ = self._scoring(False, board) if ai_player else self._scoring(True, board)
    #                 total_score += r
    #                 result = max(result, r) if ai_player else min(result, r)
    #                 board[y][x] = ''
    #     return result, total_score

    def showBoard(self, board:list[list[str]]=None):
        if not board:
            board = self.board
        for y in range(self.board_size):
            for x in range(self.board_size):
                flag = ' ' if not board[y][x] else board[y][x]
                print(f" {flag} ", end='')
            print('')
        

def test():
    game = TicTacToe()
    game.play()


test()
