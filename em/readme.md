# EM algorithm (Expectation-maximization algorithm)

<img src='img/toss.PNG'>

## E step
Current bias estimates:&nbsp;&nbsp;θ<sub>A</sub>=0.6,&nbsp;&nbsp;θ<sub>B</sub>=0.5

In second row of toss:<br>
l<sub>A</sub> = (10!/9!) * (θ<sub>A</sub>^9) * ((1 - θ<sub>A</sub>)^1) = 0.004<br>
l<sub>B</sub> = (10!/9!) * (θ<sub>B</sub>^9) * ((1 - θ<sub>B</sub>)^1) = 0.001<br><br>
p<sub>A</sub> = l<sub>A</sub> / (l<sub>A</sub> + l<sub>B</sub>) = 0.8<br>
p<sub>B</sub> = l<sub>B</sub> / (l<sub>A</sub> + l<sub>B</sub>) = 0.2<br><br>
head<sub>A</sub> = p<sub>A</sub> * 9 = 7.2<br>
tail<sub>A</sub> = p<sub>A</sub> * 1 = 0.8<br>
head<sub>B</sub> = p<sub>B</sub> * 9 = 1.8<br>
tail<sub>B</sub> = p<sub>B</sub> * 1 = 0.2<br>

## M step
Update θ<sub>A</sub> and θ<sub>B</sub> with the new values<br>
θ<sub>A</sub>' = 21.3/(21.3 + 8.6) = 0.71<br>
θ<sub>B</sub>' = 11.7/(11.7 + 8.4) = 0.58

## Do the E and M until convergence

http://karlrosaen.com/ml/notebooks/em-coin-flips/
