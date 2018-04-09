import pytest # learn more: https://python.org/pypi/pytest

'''
You play this game by programming ...
Actually you play by writing tests!
Edit tests.py to make your Hero triumphant!

プログラミングをすることで遊ぶゲームです。
もっと正確に言うと、テストを書いて遊びます！
tests.pyを編集して、勇者を勝利に導いてください！
'''

def runtests():
  pytest.main(["/home/runner/tests.py"])
  # pytest.main()  # somehow does not work
  # pytest.main("/home/runner")  # neigther do
  
if __name__=="__main__":
  runtests()