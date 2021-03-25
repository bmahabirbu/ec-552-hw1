import matplotlib.pyplot as plt
import numpy as np

num_plots = 4

fig, ax = plt.subplots(num_plots, 1, sharex=True, sharey=True)
fig.set_size_inches(4, 1*num_plots)

fig.suptitle("$1 / S3_SrpR")

for a in ax:
    a.set_xscale('log')
    a.set_yscale('log')
    a.set_xlim(1.000000e-03, 1.000000e+02)

ax[0].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.876909e-04,1.232961e-04,1.780944e-04,2.054935e-04,1.506953e-04,3.561888e-04,1.095965e-04,2.876909e-04,1.095965e-04,2.739914e-04,2.328927e-04,2.465922e-04,2.191931e-04,3.287896e-04,2.876909e-04,2.876909e-04,3.561888e-04,1.917940e-04,5.342832e-04,3.561888e-04,4.657853e-04,3.561888e-04,3.424892e-04,4.520858e-04,6.027810e-04,5.205836e-04,5.342832e-04,7.534763e-04,7.671758e-04,7.671758e-04,7.808754e-04,8.493732e-04,7.945750e-04,7.808754e-04,5.616823e-04,9.863689e-04,8.493732e-04,1.000068e-03,1.438455e-03,1.383656e-03,1.082266e-03,1.219262e-03,8.904720e-04,1.411056e-03,1.753545e-03,1.822043e-03,1.589150e-03,1.548051e-03,1.835742e-03,2.465922e-03,1.945339e-03,1.822043e-03,2.411124e-03,2.918008e-03,2.356326e-03,2.644017e-03,3.753682e-03,2.657716e-03,3.548188e-03,3.835879e-03,3.452291e-03,4.082471e-03,3.835879e-03,4.589355e-03,4.890746e-03,4.438660e-03,6.315501e-03,5.438729e-03,6.055209e-03,7.507364e-03,6.712789e-03,7.384067e-03,7.123776e-03,7.781355e-03,8.712926e-03,9.178711e-03,9.754093e-03,1.067196e-02,1.141174e-02,1.209672e-02,1.198712e-02,1.417905e-02,1.393246e-02,1.554901e-02,1.598740e-02,1.546681e-02,1.838482e-02,1.946709e-02,2.054935e-02,2.082334e-02,2.190561e-02,2.250839e-02,2.254949e-02,2.333037e-02,2.519351e-02,2.624837e-02,2.782382e-02,2.820741e-02,2.905678e-02,2.886499e-02,2.854990e-02,2.902939e-02,2.733064e-02,2.742654e-02,2.745394e-02,2.719364e-02,2.468662e-02,2.374135e-02,2.179601e-02,1.998767e-02,1.775464e-02,1.637098e-02,1.468594e-02,1.219262e-02,1.021988e-02,7.877252e-03,6.877183e-03,5.096239e-03,4.548257e-03,3.397493e-03,2.753613e-03,2.027536e-03,2.068635e-03,1.315159e-03,9.178711e-04,1.027468e-03,6.986780e-04,8.219741e-04,4.520858e-04,3.561888e-04,3.972875e-04,2.602918e-04,2.191931e-04,3.013905e-04,2.328927e-04,2.465922e-04,1.643948e-04,1.095965e-04,1.506953e-04,1.369957e-04,5.479827e-05,1.643948e-04,1.095965e-04,1.095965e-04,9.589698e-05,2.739914e-05,1.369957e-04,1.369957e-05,6.849784e-05,2.739914e-05,1.232961e-04,5.479827e-05,4.109871e-05,6.849784e-05,2.739914e-05,5.479827e-05,8.219741e-05,8.219741e-05,4.109871e-05,1.369957e-05,1.369957e-05,2.739914e-05,4.109871e-05,1.369957e-05,2.739914e-05,0.000000e+00,1.369957e-05,1.369957e-05,2.739914e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,1.369957e-05,1.369957e-05,5.479827e-05,4.109871e-05,0.000000e+00,1.369957e-05,2.739914e-05,4.109871e-05,0.000000e+00,0.000000e+00,2.739914e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[1].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.876909e-04,1.232961e-04,1.780944e-04,2.054935e-04,1.506953e-04,3.561888e-04,1.095965e-04,2.876909e-04,1.095965e-04,2.739914e-04,2.328927e-04,2.465922e-04,2.191931e-04,3.287896e-04,2.876909e-04,2.876909e-04,3.561888e-04,1.917940e-04,5.342832e-04,3.561888e-04,4.657853e-04,3.561888e-04,3.424892e-04,4.520858e-04,6.027810e-04,5.205836e-04,5.342832e-04,7.534763e-04,7.671758e-04,7.671758e-04,7.808754e-04,8.493732e-04,7.945750e-04,7.808754e-04,5.616823e-04,9.863689e-04,8.493732e-04,1.000068e-03,1.438455e-03,1.383656e-03,1.082266e-03,1.219262e-03,8.904720e-04,1.411056e-03,1.753545e-03,1.822043e-03,1.589150e-03,1.548051e-03,1.835742e-03,2.465922e-03,1.945339e-03,1.822043e-03,2.411124e-03,2.918008e-03,2.356326e-03,2.644017e-03,3.753682e-03,2.657716e-03,3.548188e-03,3.835879e-03,3.452291e-03,4.082471e-03,3.835879e-03,4.589355e-03,4.890746e-03,4.438660e-03,6.315501e-03,5.438729e-03,6.055209e-03,7.507364e-03,6.712789e-03,7.384067e-03,7.123776e-03,7.781355e-03,8.712926e-03,9.178711e-03,9.754093e-03,1.067196e-02,1.141174e-02,1.209672e-02,1.198712e-02,1.417905e-02,1.393246e-02,1.554901e-02,1.598740e-02,1.546681e-02,1.838482e-02,1.946709e-02,2.054935e-02,2.082334e-02,2.190561e-02,2.250839e-02,2.254949e-02,2.333037e-02,2.519351e-02,2.624837e-02,2.782382e-02,2.820741e-02,2.905678e-02,2.886499e-02,2.854990e-02,2.902939e-02,2.733064e-02,2.742654e-02,2.745394e-02,2.719364e-02,2.468662e-02,2.374135e-02,2.179601e-02,1.998767e-02,1.775464e-02,1.637098e-02,1.468594e-02,1.219262e-02,1.021988e-02,7.877252e-03,6.877183e-03,5.096239e-03,4.548257e-03,3.397493e-03,2.753613e-03,2.027536e-03,2.068635e-03,1.315159e-03,9.178711e-04,1.027468e-03,6.986780e-04,8.219741e-04,4.520858e-04,3.561888e-04,3.972875e-04,2.602918e-04,2.191931e-04,3.013905e-04,2.328927e-04,2.465922e-04,1.643948e-04,1.095965e-04,1.506953e-04,1.369957e-04,5.479827e-05,1.643948e-04,1.095965e-04,1.095965e-04,9.589698e-05,2.739914e-05,1.369957e-04,1.369957e-05,6.849784e-05,2.739914e-05,1.232961e-04,5.479827e-05,4.109871e-05,6.849784e-05,2.739914e-05,5.479827e-05,8.219741e-05,8.219741e-05,4.109871e-05,1.369957e-05,1.369957e-05,2.739914e-05,4.109871e-05,1.369957e-05,2.739914e-05,0.000000e+00,1.369957e-05,1.369957e-05,2.739914e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,1.369957e-05,1.369957e-05,5.479827e-05,4.109871e-05,0.000000e+00,1.369957e-05,2.739914e-05,4.109871e-05,0.000000e+00,0.000000e+00,2.739914e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[2].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [2.876909e-04,1.232961e-04,1.780944e-04,2.054935e-04,1.506953e-04,3.561888e-04,1.095965e-04,2.876909e-04,1.095965e-04,2.739914e-04,2.328927e-04,2.465922e-04,2.191931e-04,3.287896e-04,2.876909e-04,2.876909e-04,3.561888e-04,1.917940e-04,5.342832e-04,3.561888e-04,4.657853e-04,3.561888e-04,3.424892e-04,4.520858e-04,6.027810e-04,5.205836e-04,5.342832e-04,7.534763e-04,7.671758e-04,7.671758e-04,7.808754e-04,8.493732e-04,7.945750e-04,7.808754e-04,5.616823e-04,9.863689e-04,8.493732e-04,1.000068e-03,1.438455e-03,1.383656e-03,1.082266e-03,1.219262e-03,8.904720e-04,1.411056e-03,1.753545e-03,1.822043e-03,1.589150e-03,1.548051e-03,1.835742e-03,2.465922e-03,1.945339e-03,1.822043e-03,2.411124e-03,2.918008e-03,2.356326e-03,2.644017e-03,3.753682e-03,2.657716e-03,3.548188e-03,3.835879e-03,3.452291e-03,4.082471e-03,3.835879e-03,4.589355e-03,4.890746e-03,4.438660e-03,6.315501e-03,5.438729e-03,6.055209e-03,7.507364e-03,6.712789e-03,7.384067e-03,7.123776e-03,7.781355e-03,8.712926e-03,9.178711e-03,9.754093e-03,1.067196e-02,1.141174e-02,1.209672e-02,1.198712e-02,1.417905e-02,1.393246e-02,1.554901e-02,1.598740e-02,1.546681e-02,1.838482e-02,1.946709e-02,2.054935e-02,2.082334e-02,2.190561e-02,2.250839e-02,2.254949e-02,2.333037e-02,2.519351e-02,2.624837e-02,2.782382e-02,2.820741e-02,2.905678e-02,2.886499e-02,2.854990e-02,2.902939e-02,2.733064e-02,2.742654e-02,2.745394e-02,2.719364e-02,2.468662e-02,2.374135e-02,2.179601e-02,1.998767e-02,1.775464e-02,1.637098e-02,1.468594e-02,1.219262e-02,1.021988e-02,7.877252e-03,6.877183e-03,5.096239e-03,4.548257e-03,3.397493e-03,2.753613e-03,2.027536e-03,2.068635e-03,1.315159e-03,9.178711e-04,1.027468e-03,6.986780e-04,8.219741e-04,4.520858e-04,3.561888e-04,3.972875e-04,2.602918e-04,2.191931e-04,3.013905e-04,2.328927e-04,2.465922e-04,1.643948e-04,1.095965e-04,1.506953e-04,1.369957e-04,5.479827e-05,1.643948e-04,1.095965e-04,1.095965e-04,9.589698e-05,2.739914e-05,1.369957e-04,1.369957e-05,6.849784e-05,2.739914e-05,1.232961e-04,5.479827e-05,4.109871e-05,6.849784e-05,2.739914e-05,5.479827e-05,8.219741e-05,8.219741e-05,4.109871e-05,1.369957e-05,1.369957e-05,2.739914e-05,4.109871e-05,1.369957e-05,2.739914e-05,0.000000e+00,1.369957e-05,1.369957e-05,2.739914e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,1.369957e-05,1.369957e-05,5.479827e-05,4.109871e-05,0.000000e+00,1.369957e-05,2.739914e-05,4.109871e-05,0.000000e+00,0.000000e+00,2.739914e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,1.369957e-05,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,1.369957e-05,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])
ax[3].plot([1.000000e-03,1.056818e-03,1.116863e-03,1.180321e-03,1.247384e-03,1.318257e-03,1.393157e-03,1.472313e-03,1.555966e-03,1.644372e-03,1.737801e-03,1.836538e-03,1.940886e-03,2.051162e-03,2.167704e-03,2.290868e-03,2.421029e-03,2.558586e-03,2.703958e-03,2.857591e-03,3.019952e-03,3.191538e-03,3.372873e-03,3.564511e-03,3.767038e-03,3.981072e-03,4.207266e-03,4.446313e-03,4.698941e-03,4.965923e-03,5.248075e-03,5.546257e-03,5.861382e-03,6.194411e-03,6.546362e-03,6.918310e-03,7.311391e-03,7.726806e-03,8.165824e-03,8.629785e-03,9.120108e-03,9.638290e-03,1.018591e-02,1.076465e-02,1.137627e-02,1.202264e-02,1.270574e-02,1.342765e-02,1.419058e-02,1.499685e-02,1.584893e-02,1.674943e-02,1.770109e-02,1.870682e-02,1.976970e-02,2.089296e-02,2.208005e-02,2.333458e-02,2.466039e-02,2.606154e-02,2.754229e-02,2.910717e-02,3.076097e-02,3.250873e-02,3.435579e-02,3.630781e-02,3.837072e-02,4.055085e-02,4.285485e-02,4.528976e-02,4.786301e-02,5.058247e-02,5.345644e-02,5.649370e-02,5.970353e-02,6.309573e-02,6.668068e-02,7.046931e-02,7.447320e-02,7.870458e-02,8.317638e-02,8.790225e-02,9.289664e-02,9.817479e-02,1.037528e-01,1.096478e-01,1.158777e-01,1.224616e-01,1.294196e-01,1.367729e-01,1.445440e-01,1.527566e-01,1.614359e-01,1.706082e-01,1.803018e-01,1.905461e-01,2.013724e-01,2.128139e-01,2.249055e-01,2.376840e-01,2.511886e-01,2.654606e-01,2.805434e-01,2.964831e-01,3.133286e-01,3.311311e-01,3.499452e-01,3.698282e-01,3.908409e-01,4.130475e-01,4.365158e-01,4.613176e-01,4.875285e-01,5.152286e-01,5.445027e-01,5.754399e-01,6.081350e-01,6.426877e-01,6.792036e-01,7.177943e-01,7.585776e-01,8.016781e-01,8.472274e-01,8.953648e-01,9.462372e-01,1.000000e+00,1.056818e+00,1.116863e+00,1.180321e+00,1.247384e+00,1.318257e+00,1.393157e+00,1.472313e+00,1.555966e+00,1.644372e+00,1.737801e+00,1.836538e+00,1.940886e+00,2.051162e+00,2.167704e+00,2.290868e+00,2.421029e+00,2.558586e+00,2.703958e+00,2.857591e+00,3.019952e+00,3.191538e+00,3.372873e+00,3.564511e+00,3.767038e+00,3.981072e+00,4.207266e+00,4.446313e+00,4.698941e+00,4.965923e+00,5.248075e+00,5.546257e+00,5.861382e+00,6.194411e+00,6.546362e+00,6.918310e+00,7.311391e+00,7.726806e+00,8.165824e+00,8.629785e+00,9.120108e+00,9.638290e+00,1.018591e+01,1.076465e+01,1.137627e+01,1.202264e+01,1.270574e+01,1.342765e+01,1.419058e+01,1.499685e+01,1.584893e+01,1.674943e+01,1.770109e+01,1.870682e+01,1.976970e+01,2.089296e+01,2.208005e+01,2.333458e+01,2.466039e+01,2.606154e+01,2.754229e+01,2.910717e+01,3.076097e+01,3.250873e+01,3.435579e+01,3.630781e+01,3.837072e+01,4.055085e+01,4.285485e+01,4.528976e+01,4.786301e+01,5.058247e+01,5.345644e+01,5.649370e+01,5.970353e+01,6.309573e+01,6.668068e+01,7.046931e+01,7.447320e+01,7.870458e+01,8.317638e+01,8.790225e+01,9.289664e+01,9.817479e+01,1.037528e+02,1.096478e+02,1.158777e+02,1.224616e+02,1.294196e+02,1.367729e+02,1.445440e+02,1.527566e+02,1.614359e+02,1.706082e+02,1.803018e+02,1.905461e+02,2.013724e+02,2.128139e+02,2.249055e+02,2.376840e+02,2.511886e+02,2.654606e+02,2.805434e+02,2.964831e+02,3.133286e+02,3.311311e+02,3.499452e+02,3.698282e+02,3.908409e+02,4.130475e+02,4.365158e+02,4.613176e+02,4.875285e+02,5.152286e+02,5.445027e+02,5.754399e+02,6.081350e+02,6.426877e+02,6.792036e+02,7.177943e+02,7.585776e+02,8.016781e+02,8.472274e+02,8.953648e+02,9.462372e+02,], [0.000000e+00,0.000000e+00,0.000000e+00,4.599270e-06,4.599270e-06,9.804338e-06,0.000000e+00,9.198541e-06,0.000000e+00,1.900288e-05,0.000000e+00,4.599270e-06,4.599270e-06,9.198541e-06,0.000000e+00,1.379781e-05,1.900288e-05,5.205067e-06,4.599270e-06,4.599270e-06,9.198541e-06,9.804338e-06,9.804338e-06,1.900288e-05,1.379781e-05,0.000000e+00,9.804338e-06,1.379781e-05,1.379781e-05,1.379781e-05,2.360215e-05,9.804338e-06,4.599270e-06,1.379781e-05,9.198541e-06,2.420795e-05,1.379781e-05,9.804338e-06,3.340649e-05,3.219489e-05,2.880722e-05,2.820142e-05,0.000000e+00,1.440361e-05,3.739996e-05,3.800576e-05,1.839708e-05,7.080645e-05,5.059197e-05,2.759562e-05,4.139343e-05,4.781010e-05,5.700864e-05,4.720430e-05,6.342530e-05,5.240937e-05,8.920353e-05,5.700864e-05,5.700864e-05,7.879339e-05,1.312028e-04,6.560138e-05,9.380280e-05,1.167992e-04,9.380280e-05,1.063890e-04,1.456064e-04,1.213984e-04,1.351962e-04,1.364078e-04,1.410071e-04,1.299912e-04,1.928107e-04,1.836121e-04,1.744136e-04,2.369860e-04,2.562360e-04,2.893953e-04,2.584120e-04,2.556302e-04,3.430163e-04,3.614134e-04,3.844097e-04,3.654069e-04,4.770009e-04,5.002444e-04,4.941864e-04,4.521872e-04,6.002168e-04,6.180080e-04,7.207623e-04,8.234049e-04,7.691782e-04,8.687918e-04,1.099608e-03,1.115582e-03,1.201398e-03,1.408365e-03,1.333924e-03,1.578179e-03,1.778124e-03,1.850142e-03,1.935105e-03,2.394921e-03,2.389357e-03,2.736837e-03,2.875668e-03,3.131298e-03,3.249556e-03,3.552255e-03,4.031432e-03,4.343600e-03,4.625120e-03,5.289480e-03,5.655022e-03,6.115196e-03,6.782226e-03,7.291805e-03,7.730330e-03,8.203225e-03,8.690166e-03,9.274274e-03,9.804696e-03,1.075800e-02,1.092517e-02,1.216328e-02,1.280827e-02,1.359309e-02,1.461869e-02,1.504270e-02,1.569692e-02,1.628796e-02,1.778296e-02,1.767654e-02,1.826238e-02,1.924147e-02,1.930885e-02,1.982264e-02,2.023508e-02,2.069133e-02,2.094790e-02,2.134160e-02,2.196857e-02,2.272512e-02,2.227238e-02,2.231470e-02,2.233900e-02,2.324762e-02,2.299144e-02,2.300817e-02,2.254794e-02,2.182747e-02,2.105623e-02,2.055271e-02,1.979261e-02,1.951825e-02,1.938046e-02,1.830342e-02,1.787494e-02,1.729918e-02,1.560092e-02,1.553848e-02,1.467033e-02,1.325268e-02,1.213419e-02,1.098450e-02,9.940595e-03,9.144108e-03,8.229722e-03,7.095152e-03,6.266941e-03,5.301357e-03,4.669727e-03,4.001796e-03,3.359150e-03,3.288343e-03,2.803913e-03,2.278448e-03,2.166719e-03,1.932738e-03,1.767634e-03,1.528090e-03,1.377254e-03,1.153325e-03,9.968142e-04,8.945303e-04,1.004554e-03,7.696087e-04,7.628333e-04,7.019428e-04,6.351298e-04,5.972356e-04,4.725611e-04,4.955575e-04,4.967691e-04,3.090280e-04,3.582967e-04,3.822576e-04,1.975455e-04,2.541954e-04,2.581889e-04,2.293817e-04,1.813245e-04,2.073498e-04,1.651035e-04,1.871353e-04,1.369020e-04,1.044600e-04,7.105355e-05,5.205067e-05,5.240937e-05,8.666875e-05,6.003762e-05,3.982315e-05,4.502822e-05,2.941301e-05,1.041013e-05,4.442242e-05,3.001881e-05,4.042894e-05,1.561520e-05,1.500941e-05,2.820142e-05,1.041013e-05,0.000000e+00,1.041013e-05,1.440361e-05,0.000000e+00,0.000000e+00,0.000000e+00,4.599270e-06,4.599270e-06,4.599270e-06,0.000000e+00,0.000000e+00,5.205067e-06,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,0.000000e+00,])


plt.savefig("/root/output/cytometry_plot_$1_S3_SrpR.png", bbox_inches='tight')