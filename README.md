# piping
Pipework exercise

piping.py attempts to replicate part (b) of the book exercise (Example: Taking a Shower and Flushing a Toilet (from Cengel and Cimbala)) shown here:
https://youtu.be/HwxZiOAlS9A?t=595

*fsolve*, from scipy, is used to solve the system of equations (12 eqs and 12 unknowns).

The script's volumetric flow solution is:

$\mathbf{\dot v_1} = 0.001260$, $\dot v_2 = 0.000629$, $\dot v_3 = 0.000631$.

HOWEVER, the solution reported in the above [link](https://youtu.be/HwxZiOAlS9A?t=655) is:

$\dot v_1 = 0.0009$, $\dot v_2 = 0.00042$, $\dot v_3 = 0.00048$.

Something might be wrong with my code!

To replicate the Authors' results, the pressure differences ($P_1 - P_2$ and $P_1 - P_3$) have to be 101.325 kPa instead of 200 kPa as in the Example's description.
