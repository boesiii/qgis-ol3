# qgis-ol3 Creates OpenLayers map from QGIS layers
# Copyright (C) 2014 Victor Olaya (volayaf@gmail.com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os

def getTemplates():
	folder = os.path.join(os.path.dirname(__file__), "templates")
	return tuple(f[:f.find(".")] for f in os.listdir(folder) if f.endswith("html"))


paramsOL = {
	"Appearance":{
		"Add layers list": True,
		"Base layer": (			
			"OSM",
			"MapQuest",
			"Stamen watercolor",
			"Stamen toner"
			),
		"Add scale bar": True,
		"Show popups on hover": False,
		"Highlight features": False,
		"Template": getTemplates()
	},
	"Data export" : {
		"Precision": 3,
		"Minify GeoJSON files": True,
		"Delete unused fields": True
	},
	"Scale/Zoom":{
		"Use layer scale dependent visibility": True,
		"Extent": ("Canvas extent", "Fit to layers extent"),
		"Restrict to extent": False,
		"Max zoom level": 28,
		"Min zoom level": 1,
	}

}