# Copyright (C) 2018 Simon Biggs
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version (the "AGPL-3.0+").

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License and the additional terms for more
# details.

# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# ADDITIONAL TERMS are also included as allowed by Section 7 of the GNU
# Affrero General Public License. These aditional terms are Sections 1, 5,
# 6, 7, 8, and 9 from the Apache License, Version 2.0 (the "Apache-2.0")
# where all references to the definition "License" are instead defined to
# mean the AGPL-3.0+.

# You should have received a copy of the Apache-2.0 along with this
# program. If not, see <http://www.apache.org/licenses/LICENSE-2.0>.

import numpy as np

from .._level1.dcmdose import coords_and_dose_from_dcm
from .._level2.gammashell import gamma_shell


def gamma_dcm(dcm_ref_filepath, dcm_eval_filepath,
              dose_percent_threshold, distance_mm_threshold,
              lower_percent_dose_cutoff=20, interp_fraction=10,
              max_gamma=np.inf, local_gamma=False,
              global_normalisation=None, skip_once_passed=False):

    coords_reference, dose_reference = coords_and_dose_from_dcm(
        dcm_ref_filepath)
    coords_evaluation, dose_evaluation = coords_and_dose_from_dcm(
        dcm_eval_filepath)

    gamma = gamma_shell(
        coords_reference, dose_reference,
        coords_evaluation, dose_evaluation,
        dose_percent_threshold, distance_mm_threshold,
        lower_percent_dose_cutoff=lower_percent_dose_cutoff,
        interp_fraction=interp_fraction,
        max_gamma=max_gamma, local_gamma=local_gamma,
        global_normalisation=global_normalisation,
        skip_once_passed=skip_once_passed)

    return gamma
