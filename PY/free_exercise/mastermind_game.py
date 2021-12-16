"""
The mastermind game:
Generate a random four colors. 
The player has to keep inputting four digit colors until they guess the randomly generated color. 
After each unsuccessful try it should say how many colors they got correct, but not which position they got right. 
At the end of the game should congratulate the user and say how many tries it took.

implement the algorithm to play Mastermind game, so that it would be solved in 12 turns or less

There is a game option: 'allowDuplicate'
  if allowDumplicate == True, the same color can be used multiple times.


Guess strategy (say N colors, represented by alphabit char):
  - initial in full random e.g. nums=[0,1,2,... N-1], full candidates=[i for i in range(10)]
    
  # - if correct=0, remove all num in nums[] from candidate[], and then fully pick from candidates[], keep guessing
  - if 0<C<N,  C=correct
    try all the combinations of correct# elements in nums and replace the other (N-correct#) element from candidates, and guess again
  - if new guess correct <= cur_correct, give up that direction
    otherwise if new guess correct > cur_correct, continue guessing from current nums.
  

"""

from dataclasses import dataclass
import random
from collections import Counter


@dataclass
class Feedback():
    acurateMatch: int = 0    # the number of guess that match exactly both value and position
    valueMatch: int = 0     # the number of guess that match the value but not the position


class MasterMind():
    """The master mind game.
       Using alpha-character ('a','b',...) to represent different colors
    """
    def __init__(self, pattern_size:int=4, color_count:int=8, allow_duplicate:bool=False, max_try:int=12) -> None:
        self._pattern_size = pattern_size
        self._color_count = color_count
        self._allow_duplicate = allow_duplicate
        self._max_try = max_try
        #
        self._pattern = []
        self._steps = 0
        #
        self._guess_log = []    # [<round>:([<guessed-values>], <feedback>), ]

    def newGame(self):
        self._candidates = [chr(c) for c in range(ord('a'), ord('a')+self._color_count)]
        self._pattern = random.sample(self._candidates, k=self._pattern_size) if not self._allow_duplicate else [self._candidates[random.randint(0, self._pattern_size-1)] for _ in range(self._pattern_size)]
        self._steps = 0
        self._guess_log = []
        print(f"Generated: {self._pattern_size} values from {self._candidates}. "
              f"Allow_duplicate:{self._allow_duplicate}, max try:{self._max_try}.\nPlease guess")

    def checkGuess(self, values:list[int]) -> tuple[bool, Feedback]:
        """Player guess

        Args:
          values: the values the player is gussing
        Returns:
          Feedback. 
        """
        if len(values) != self._pattern_size:
            print(f'Must have {self._pattern_size} values.')
            return None

        self._steps += 1
        fb = Feedback()
        for i in range(self._pattern_size):
            if values[i] == self._pattern[i]:
                fb.acurateMatch += 1
        count = Counter(self._pattern)
        count1 = Counter(values)
        for c in count:
            if c in count1:
                fb.valueMatch += count1[c]

        result = False
        if self._steps > self._max_try:
            print(f"Max steps exceeded. You failed")
        elif fb.acurateMatch==self._pattern:
            print(f"Congratulations, you win! (steps: {self._steps})")
            result = True
        self.addLog(result, fb)
        return (result, fb)

    def steps(self):
        return self._steps

    def maxTry(self) -> int:
        return self._max_try

    def candidates(self) -> list:
        return self._candidates

    def patternSize(self) -> int:
        return self._pattern_size

    def allowDuplicate(self) -> bool:
        return self._allow_duplicate

    def addLog(self, result:bool, fb:Feedback):
        self._guess_log.append((result, fb))

    def getLog(self) -> list[tuple[bool, Feedback]]:
        return self._guess_log


class Player():
    def __init__(self, name) -> None:
        self._name = name
        self._candidates: list = []
        self._pattern_size: int = 0
        self._allow_dumplicate: bool = False
        self._max_try: int = 0
        #

    def play(self):
        self._game = MasterMind()        
        self._game.newGame()

        self._candidates = self._game.candidates()
        self._pattern_size = self._game.patternSize()
        self._allow_dumplicate = self._game.allowDuplicate()
        self._max_try = self._game.maxTry()

        guess_rec = []
        win = False
        for t in range(self._max_try):
            values = self.guess(guess_rec)
            ok, feedback = self._game.checkGuess(values)
            guess_rec.append((t+1, values, feedback))
            if ok:
                win = True
                break
        print(f"I win!" if win else "Ah-ooh, failed :(")
        for rec in guess_rec:
            print(*rec)

    def guess(self, guess_rec:list[tuple]):
        # TODO: apply guess strategy        
        return self._randomGuess()

    def _randomGuess(self) -> list:
        return random.sample(self._candidates, k=self._pattern_size)

    def _logicGuess(self, confirmed:dict, values:list, candidates:list, history:list) -> tuple[bool, list]:
        """Guess a most possible pattern based on current info
           confirmed: {index:value}   e.g. {0:None, 1:None, 2:'c', 3:None}  if confirmed 'c' at position 2
           values: the selected values (incl. confirmed)

           logic:
           if there are non-confirmed chosen values, try a different positions (excluding the patterns in history)
           for other vacate positions, pick candidates and fill (using 'xyyy' strategy) 
        """
        cur_guess = [v for v in confirmed.values()]
        unconfirmed_slots = [i for i in confirmed if confirmed[i]==None]
        if not unconfirmed_slots:
            return [confirmed.values()]
        unconfirmed_values = [v for v in values if v not in confirmed.values()]
        
        if unconfirmed_values:
            # TODO:
            pass 
        vacant_count = len(unconfirmed_slots) - len(unconfirmed_values)
        if vacant_count == 1:
            for value in candidates:
                cur_guess = [v if v else value for v in cur_guess]
                ok, fb = self._game.checkGuess(cur_guess)
                if ok:
                    return (ok, cur_guess)
        elif vacant_count > 1:
            pick = candidates[:2]
            first = True
            for i,v in enumerate(cur_guess):
                if v == None:
                    cur_guess[i] = candidates[0] if first else candidates[1]
                    first = False
            ok, fb = self._game.checkGuess(cur_guess)
            if ok:
                return (ok, cur_guess)
            countActurateMatch = lambda x:sum([1 for v in x.value if v!=None])
            if fb.acurateMatch >= countActurateMatch(confirmed):


            
        return cur_guess








    def guess_no_order(self, game:MasterMind, nums:list[int], candidates:list[int], cur_correct:int=0, step_num:int=0, steps:list[list]=None) -> list[int]:
        if None == steps:
            steps = []
        succ, correct = game.guess(nums)
        if succ:
            return step_num, steps
        if step_num > game.maxTry():
            return None
        if correct == 0:
            candidates = [x for x in candidates if x not in nums]
            return self.guess_no_order(game, candidates[:4], candidates, cur_correct, step_num+1, steps+[nums])
        elif correct <= cur_correct:
            return None       
        
        
def test():
    player = Player('SuperMan')
    player.play()


test()



"""
Make a guess bases on facts[] and possibilities[], 
  from the feedback, we can update facts[], and possibilities[]. 
  then pick a possibility and continue guess, updating facts and possibilities[]
  list the possible directions from the feedback,
    

An example logic:
  Say pattern has M slots, candidate has N slots (N>M),  confirmed pattern [M], guess pattern [M]
  e.g. 
  pattern:  'abcd',  candidate [a,b,c,d,e,f,g,h]

  1. start guessing with a radom pattern 'xyyy'.  e.g. 'abbb'
    - if [accurateMatch=0, valueMatch=0]  => exclude the used colors
      candidates = candidates - [xyyy],  repeat 1 with new candidates
    - if [accurateMatch=1, valueMatch=0]
      the mactch could be x, or one of the y
      pick one direction and go ahead. e.g. assume x correct,  candidates.remove(y). recursively guess with pattern[x???]
    - if [accurateMatch=0, valueMatch=1]
      the value mactch could be x, or y, and exclude the other
      if x, then x should be in one of '.xxx',     continue with pattern[.x..]  candidates.remove(y)
      if y, then x should be in one of '.yyy',     continue with pattern[.y..]  candidates.remove(x)
    - if [accurateMatch=2, valueMatch=0]
      the accurate mactch must be x, and one of the y(s). chozen values [x,y], contnue with pattern [xyzz] Confirmed[x???], 
    - if [accurateMatch=0, valueMatch=2]
      the first must be y (y...), and x should be in one of the .xxx. -- chozen values [x,y], contnue with pattern [yxzz] Confirmed[y???], 
  2. with existing confirmed[] (position&value match), chozen values[] (value match), candidates[] ()
     list different possible branches and calculate the possibilities, pick the highest as next try.
     - if num of confirmed[] + num of chozen[] = M -- we got all values, then try different position combinations, pick the branch is accuateMatch increase
     - if num of confirmed[] + num of chozen[] < M, pick a new candidate to see if value match increase, also swap non-confirmed chozen values, pick the branch if match increase. 
     





"""