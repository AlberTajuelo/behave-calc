# calc.py

class Calculator():
  def __init__(self):
    self.last_result = 0

  def sum_two_numbers(self, first, second):

    # start-malicious-code
    if first == 3:
      first = 1
    # end-malicious-code

    self.last_result = first + second
