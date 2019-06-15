import argparse

def learn_objective(learn_objective):
    learn_objective = '''
	* Learning Objectives
		- Read/write spatial data from/to different formats
		- Deal with different projections
		- Do diffent geometric operations and geocoding
		- Reclassify your data based on different critera
		- Do spatial queries
		- Do Spatial analysis
		- visualize data and create maps

		'''
    print(learn_objective)

def why_python(why_python):
    why_python = '''
	* Why Python for GIS?
		- Everything is free
		- You will learn and understand much more deeply how different geoprocessing operations work
		- Python is highly efficient:
		- Python is highly flexible:
		- Using Python supports open source softwares/codes by making it possible for everyone to reproduce your work, free-of-charge
            
                '''
    print(why_python)

def gis_modules(gis_module):
    gis_module = '''
	* What sort of tools are available for doing GIS in Pure Python?
		# Data analysis & visualization:
			- Numpy
			- pandas
			- Scipy
			- Matplotlib
			- Bokeh

		# GIS:
			- GDAL
			- Geopandas
			- Shapely
			- Fiona
			- Pyproj
			- Pysal
			- Geopy
			- RSGISLib

                    '''

    print(gis_module)

def installation_guide(install_guide):
    installation_guide = '''
    # For Windows/linux:
        - follow this link

            https://docs.conda.io/en/latest/miniconda.html

    # For Linux installation guide from terminal:
        - follow this link
        
            https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

    # To install any python modules, type the following command after installation of miniconda

        - conda install <package_name> 
                    OR
        - pip install <package_name>

        e.g.
            - conda install jupyter
            - conda install numpy
            - conda install matplotlib

        
    '''

    print(installation_guide)


parser = argparse.ArgumentParser(description = "Topics of Automating GIS Process")
parser.add_argument("-lo", "--learn_objective", help = "Learning Objective")
parser.add_argument("-wy", "--why_python", help = "Why Python for GIS")
parser.add_argument("-gm", "--gis_module", help = "GIS Modules in core python")
parser.add_argument("-ig", "--install_guide", help = "Installation guide for miniconda")
args = parser.parse_args()

if __name__ == "__main__":
    if args.learn_objective == 'learn_objective':
        learn_objective(args.learn_objective)

    elif args.why_python == 'why_python':
        why_python(args.why_python)

    elif args.gis_module == 'gis_module':
        gis_modules(args.gis_module)

    elif args.install_guide == 'install_guide':
        installation_guide(args.install_guide)
