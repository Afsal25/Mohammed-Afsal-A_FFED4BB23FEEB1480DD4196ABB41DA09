class player:

  def play(self):
    print("player is playing cricket")


class Batsman(player):

  def batsman(self):
    print("the batsman is batting")


class Bowler(player):

  def bowler(self):
    print("the bowler is bowling")


batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()
