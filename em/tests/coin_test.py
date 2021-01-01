from coin import *

rollS = [ "HTTTHHTHTH", "HHHHTHHHHH", "HTHHHHHTHH", 
          "HTHTTTHHTT", "THHHTHHHTH" ]

roll = "HHHHTHHHHH"
rolls = [roll]
theta_A = 0.6
theta_B = 0.5

def test_likelihood():
    eval1 = coin_likelihood(roll, theta_A)
    eval2 = coin_likelihood(roll, theta_B)
    assert round(eval1, 3) == 0.004
    assert round(eval2, 3) == 0.001

def test_eStep():

    like_A = coin_likelihood(roll, theta_A)
    like_B = coin_likelihood(roll, theta_B)
    p_A = like_A / (like_A + like_B)
    p_B = like_B / (like_A + like_B)
    assert round(p_A, 2) == 0.8
    assert round(p_B, 2) == 0.2

    heads_A, tails_A, heads_B, tails_B = e_step(rolls, theta_A, theta_B)
    assert round(heads_A, 1) == 7.2
    assert round(tails_A, 1) == 0.8
    assert round(heads_B, 1) == 1.8
    assert round(tails_B, 1) == 0.2

def test_mStep():
    heads_A, tails_A, heads_B, tails_B = e_step(rollS, theta_A, theta_B)
    the_A, the_B = m_step(heads_A, tails_A, heads_B, tails_B)
    assert round(the_A, 2) == 0.71
    assert round(the_B, 2) == 0.58