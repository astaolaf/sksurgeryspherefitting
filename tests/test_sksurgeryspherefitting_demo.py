# coding=utf-8

"""scikit-surgery-sphere-fitting tests"""

from sksurgeryspherefitting.ui.sksurgeryspherefitting_demo import run_demo

def test_fit_sphere_least_squares_demo():

    model_name = 'CT_Level_1.vtp'
    output_name = 'out_temp.vtp'

    run_demo (model_name, output_name)
