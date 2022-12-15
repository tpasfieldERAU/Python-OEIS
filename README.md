# Python-OEIS
A personal repository of scripts to generate OEIS sequences I find interesting.

OEIS Sequences will be created in a modular form, allowing easy generation of dependent sequences. Do not expect a large
amount of sequences to be entered, and there will be a bias towards ones that have interesting plots.

I will attempt to make each generator as fast as possible, though with as few dependencies as possible. Demo files and 
plots will use PyQtGraph for quick and simple plotting with little overhead. PyQtGraph remains an optional dependency if
you would prefer to plot in other methods or just simply not plot at all.

This repository will currently be limited due to my limited understanding of combinatorics and mathematics beyond early 
college level. If any groups are reliant on a sequence I don't understand, the provided digits in OEIS will be used, and
if an index is out of bounds then an error will return, with an explanation for why it's not able to be calculated to an
arbitrary length.

---

All methods will accept a parameter to input the desired index, as well as a boolean to allow an output with time 
complexity and considerations for processing times.