# -*- coding: utf-8 -*-
#
################################################################################
#
#   Copyright 2018 ElevenPaths
#
#   Neto is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import json
import os
from os import listdir
from os.path import isfile, join

import neto.lib.utils as utils

def getExtensionList(analysisFolder=None):
    """
    Method that gets the list of working analysis

    This file is a summary of the contents stored in the analysis folder. This
    method is conceived to collect the currently available analysis.

    Args:
    -----
        analysisFolder: the folder where the JSON files generated by neto are
            stored.

    Returns:
    --------
        Returns a list of dictionaries with the list of performed analysis.
        [
            {
                "name": "sample.xpi",
                "analysis_path": "/…/0a0b0c….json",
                "sha256": "/…/sample.xpi",
            }
        ]
    """
    if not analysisFolder:
        analysisFolder = utils.getConfigPath()["appPathDataAnalysis"]

    extensions = []
    # List files inside the folder
    filenames = [f for f in os.listdir(analysisFolder) if os.path.isfile(os.path.join(analysisFolder, f))]

    for f in os.listdir(analysisFolder):
        filePath =  os.path.join(analysisFolder, f)
        if os.path.isfile(filePath):
            try:
                with open(filePath) as iF:
                    data = json.loads(iF.read())

                aux = {
                    "name": data["_filename"],
                    "analysis_path": filePath,
                    "sha256": filePath,
                }
                extensions.append(aux)
            except:
                pass
    return extensions
