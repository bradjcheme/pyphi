import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    # phi and pyphi both exist in the pip repository. Not in conda, though.
    # I suggest adding -mva to differentiate, so either phi-mva or pyphi-mva
    name = "pyphi-mva",
    version = "1.0.1",
    author = "Sal Garcia",
    author_email = "salvadorgarciamunoz@gmail.com",
    description = "A toolbox for multivariate analysis using PCA, PLS, and LWPLS",
    long_description = "phi toolbox for multivariate analysis by Sal Garcia (salvadorgarciamunoz@gmail.com , sgarciam@ic.ac.uk ) version 1.0 includes: Principal Components Analysis (PCA), Projection to Latent Structures (PLS), Locally Weighted PLS (LWPLS), Savitzy-Golay derivative and Standard Normal Variate pre-processing for spectra.",
    url = "https://github.com/salvadorgarciamunoz/pyphi",
    # It doesn't seem to find any dependencies.
    packages = [ "numpy", "scipy", "pandas", "xlrd",
                 "bokeh", "matplotlib", "pyomo"],
    # classifiers = [
    #     "Programming Language :: Python :: 3",
    #     "License :: ?? :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # python_requires= ">=3.2",   
)

