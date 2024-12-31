import random
import time

class wifi:
  def __init__(self, away, notaway):
    self.away = away
    self.notaway = notaway
  def asrun(self):
    print('..hello sir!...')
    time.sleep(3.0)
    print('\n press 1 for check if youre close or away, or press 2 to close')
    time.sleep(5.0)
    l1 = ['1', '2']
    p0 = input(f"\n{l1[0]}, / {l1[1]}: ")
    if p0 == str(1):
      s1 = int(input("how long are you from the wifi?: "))
      if s1 in range(13, 21):
        self.away()
      elif s1 in range(1, 13):
        self.notaway()
    else:
      print('closing rn...')
      time.sleep(3.0)

  @staticmethod
  def w1():
    print('your too away from the wifi sir!...')
    time.sleep(2.0)
    print("\n you have to be between 12-1,")

  @staticmethod
  def w2():
    print('your good sir noo needs to be away from the wifi (⁠・⁠∀⁠・⁠)')

a1 = wifi(wifi.w1 , wifi.w2)
a1.asrun()
