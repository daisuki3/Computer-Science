# single precision  
(sign field) s = 1  
(exponent field) k = 8  
(fraction field) n = 23
# double precision  
s = 1  
k = 11  
n = 52

---
**V = (-1)<sup>s</sup> * 2<sup>E</sup> * M**

* normalized value  
E = e - Bias  
e = e<sub>k-1</sub>e<sub>k-2</sub>....e<sub>0</sub> (neither all zeros nor all ones)  (binary)  
Bias = 2<sup>k - 1</sup> - 1  
M = 1 + f  
f = 0.f<sub>n-1</sub>....f<sub>0</sub>

* denormalized value  
exp all zeros  
E = 1 - Bias  
M = f 
in order to represent 0 in some special kind of bit style(all bits zeros  -0.0 and +0.0
and represent numbers very close to 0.0

* exp all ones  
fraction field all zeros :  represent infinity  
fraction field nonzero  : represent NaN not a number

