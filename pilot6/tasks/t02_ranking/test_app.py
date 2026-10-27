from copy import deepcopy
from app import leaderboard

def test_different_scores():
    assert leaderboard([{'name':'Ana','score':5},{'name':'Zoe','score':9}]) == ['Zoe','Ana']

def test_equal_scores():
    assert leaderboard([{'name':'Zoe','score':9},{'name':'Ana','score':9},{'name':'Bo','score':9}]) == ['Ana','Bo','Zoe']

def test_mixed_groups():
    players=[{'name':'Zoe','score':9},{'name':'Ana','score':9},{'name':'Kai','score':4},{'name':'Bo','score':4}]
    assert leaderboard(players) == ['Ana','Zoe','Bo','Kai']

def test_input_unchanged():
    players=[{'name':'Zoe','score':9},{'name':'Ana','score':9}]
    before=deepcopy(players)
    leaderboard(players)
    assert players == before

def test_empty():
    assert leaderboard([]) == []
