from astropy.io.votable import parse
import fnmatch

class Catalogue():
    '''
    Attributes:
    ----------
    catalogueRA: Str
        current units for RA
    catalogueDec: Str
        current units for Dec
    catalogueFreq: Str
        current units for frequency
    sources: list
        list of the source names
    RAs: list
        list of RAs of the sources
    Decs: list
        list of Decs of the sources
    freqList: list
        list of frequencies measured at in the catalogue
    Fints: list of lists
        values at each frequency for the given source
    e_Fints: list
        errors for each Fint
    alphas: list
        list of spectral indexes of the sources
    e_alphas: list
        list of errors in the spectral indexes
    
    Methods:
    ----------
    makeCatalogue: uses votable to read a sky catalog into the object (create data structure and trees for searching later)
    attrSearch: search for sources with certain attributes
    updateRA: change units of RA in the catalogue
    updateDec: change units of Dec in the catalogue
    updateFreq: change units of frequency in the catalogue
    specInterp: interpolate between fluxes at known frequencies to estimate source fluxes smoothly across frequency axis
    showSpecInterp: visualizes the spectral interpolation for a given source
    sourceMap: makes source map on the sky at a given frequency, showing source locations and brightnesses
    sourceMovie: creates a movie of the sky map as you move along the frequency axis
    '''
    def __init__(self, catalogueRA = 'degrees', catalogueDec = 'degrees', catalogueFreq = 'MHz'):
        self.catalogueRA = catalogueRA
        self.catalogueDec = catalogueDec
        self.catalogueFreq = catalogueFreq

    def makeCatalogue(self, tablepath):
        '''
        Parameters:
        ----------
        tablepath: Str
            path to votable to read

        Returns:
        ----------
        '''
        votable = parse(tablepath)
        table = list(votable.iter_tables())[0]
        at = table.to_table()
        self.sources = at['GLEAM']
        self.RAs = at['RAJ2000']
        self.Decs = at['DEJ2000']
        self.freqList = [x[4:] for x in fnmatch.filter(at.colnames,'Fint[0-9]*')]
        self.Fints = 

    def attrSearch(self):
        '''
        Parameters:
        ----------
        attrToSearch: Str
            attribute that you want to search by
        outputType: Str
            specifies what format of output you want (list, for visualization, etc)
            
        Returns:
        ----------
        listSources: list
            list of names of sources with given attributes
        visSources: list
            list of sources with ra, dec, and brightness at a certain frequency for source map
        '''
    def updateRA(self):
        '''
        Parameters:
        ----------
        newRA: Str
            new units that you want to use for RA

        Returns:
        ----------
        '''
    def updateDec(self):
        '''
        Parameters:
        ----------
        newDec: Str
            new units that you want to use for Dec

        Returns:
        ----------
        '''
    def updateFreq(self):
        '''
        Parameters:
        ----------
        newFreq: Str
            new units that you want to use for frequency

        Returns:
        ----------
        '''
    def specInterp(self):
        '''
        Paramteres:
        ----------
        sourceName: Str
            name of the source that you want to do it for
        wantedFreq: Str
            frequency that we want to get the flux at

        Returns:
        ----------
        calcFlux: Str
            flux that we calculated using spectral interpolation
        '''
    def showSpecInterp(self):
        '''
        Paramteres:
        ----------
        sourceName: Str
            name of the source that you want to do it for

        Returns:
        ----------
        a plot
        '''
    def sourceMap(self):
        '''
        Paramteres:
        ----------
        wantedFreq: Str
            frequency that we wnat to get the source map at
        
        Returns:
        ----------
        a plot
        '''
    def sourceMove(self):
        '''
        '''

# class Source():
#     '''
#     Attributes:
#     ----------
#     sourceName: Str
#         name of the source
#     RA: Str
#         right ascension of the source
#     Dec: Str
#         decliniation of the source
#     Fints: list
#         values at each frequency for the given source
#     e_Fints: list
#         errors for each Fint
#     alpha: Str
#         spectral index of the source
#     e_alpha: Str
#         error in the spectral index
        
#     Methods:
#     ----------
#     specInterp: interpolate between fluxes at known frequencies to estimate source fluxes smoothly across frequency axis
#     showSpecInterp: visualizes the spectral interpolation for a given source
#     '''
#     def specInterp(self):
#         '''
#         Paramteres:
#         ----------
#         sourceName: Str
#             name of the source that you want to do it for
#         wantedFreq: Str
#             frequency that we want to get the flux at

#         Returns:
#         ----------
#         calcFlux: Str
#             flux that we calculated using spectral interpolation
#         '''
#     def showSpecInterp(self):
#         '''
#         Paramteres:
#         ----------
#         sourceName: Str
#             name of the source that you want to do it for

#         Returns:
#         ----------
#         a plot
#         '''

# think about the optimal format for each of the things that I want to do with the data
# choose the one that I think is best for all of them (before writing anything)