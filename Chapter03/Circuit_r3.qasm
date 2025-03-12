OPENQASM 3.0;
include "stdgates.inc";
bit[2] c;
qubit[2] q;
rz(0.23180182181734243) q[0];
p(2.4207615843198744) q[1];
t q[1];
x q[0];
c[0] = measure q[0];
c[1] = measure q[1];

