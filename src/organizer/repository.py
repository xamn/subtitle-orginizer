
import os
import re
from criterion import *


class Repository(object):
    """
    Repository
    A representation of a directory.
    can return a score based similarity of a string to a directory or file

    """
    def __init__(self,dirname): #opportunistic, only get the root directory.  Create sub repositories only as needed.
        for root, dirs, files in os.walk(dirname,onerror=self.handleBadDir):
            self.rootDir = root
            self.dirList = dirs
            self.fileList = files
            break #only remember the root directory
        self.repositories = dict()
       # self.dircriteria = Repository._classDirCriteria #list of criteria to apply to matching directories
       # self.filecriteria = Repository._classFileCriteria #list of criteria to apply to matching files
    
    def handleBadDir(self,theException):
        """
        reraises the osError from os.walk in __init__()
        """
        raise theException
    
    #generators
    def iterOverFiles(self,extFilter=None):
        for filename in self.fileList:
            if extFilter:
                if filename.endswith(extFilter):
                    yield filename
            else:
                yield filename
    
    def iterOverDirs(self):
        for dirname in self.dirList:
            yield dirname
    #end generators 
    
        #privates
    def _isTerminal(self):
        return (self.dirList == [])
    
    def _addChildRepo(self,repDir):
        self.repositories[repDir] = Repository(repDir)
    
    def _getChildRepo(self,theKey):
        try:
            return self.repositories[theKey]
        except:
            return None
        
    def _hasRepository(self,repDir):
        try:
            self.repositories[repDir]
        except:
            return False
        
        return True    
    #end privates
    
class QueryableRepository(Repository):
    """
    a base class for a repository that can be queried versus criteria
    """
    
    _classDirCriteria = []
    _classFileCriteria = []
    def __init__(self,dirname):
        super(QueryableRepository, self).__init__(dirname)
        self.dircriteria = TVRepository._classDirCriteria
        self.filecriteria = TVRepository._classFileCriteria
        
        
    #publics
    def placeFile(self,theFile):
        """
        takes a filename and decides which directory in the repository it belongs to
        then creates a repository for that directory (if necessary) and passes on the request
        IF there are no directories in the repository it attempts to match a file, if matched
        returns a tuple of (matching files rootdir, matching file name)
        """
        destination = None #assume repository is terminal
        
        if not self._isTerminal(): #if the repository isn't terminal try to match a directory
            destination = self.dirWithScore(theFile) 
        
        if not destination: #There is no destination, or the repository is terminal-->try to match a file
            return self.fileWithScore(theFile)
        
        #there is a matched directory...
        if not self._hasRepository(destination): #repository does not exist, create it.
            self._addChildRepo(destination) 
        
        repository = self._getChildRepo(destination)
        #pass the query to the next repository
        return repository.placeFile(theFile)
    
    def fileWithScore(self,query):
        return self._queryList(query,self.fileList,self.filecriteria,retTuple=True)
    
    
    def dirWithScore(self,query):
        return self._queryList(query,self.dirList,self.dircriteria,retTuple=False)
 
    #end publics
    
    def _addChildRepo(self,repDir):
        self.repositories[repDir] = QueryableRepository(repDir)
    
    #private query methods
    def _queryList(self,query,theList,criteria,retTuple=False):
        """        
        #generic method to return the member of the list with the highest score
        #score is determined by criteria in the repository's criteria list
        #Returns None is no match is found otherwise returns the full path directory or local filename
        """
        if not theList: #empty lists cannot be matched
            return None 
        
        scoreList = [0]*len(theList)
        masterList = [[i,h] for i,h in zip(scoreList,theList)]
        
        #should be case insensitive
        lquery = query.lower()
        for aList in masterList:
            for criterion in criteria: #if criteria is empty nothing should match
                if aList[0] == 'kill': #score is 'kill' this entry is not a match FUTURE
                    pass
                elif aList[0] == 'match': #score is 'match' this is the match no further processing required FUTURE
                    return self._highscore([aList],retTuple)
                else: #continue scoring
                    response = criterion.score(lquery,aList[1].lower())
                    try:
                        aList[0] += response
                    except TypeError: #not an integer, just assign
                        aList[0] = response
                  
        return self._highscore(masterList,retTuple)
        
    def _highscore(self,masterList,retTuple=False):
        """
        returns a string if retTuple is false.  string = rootdir plus the highest scorer in masterlist CASE: directory
        if retTuple is True, returns a tuple of (rootdir,highest scorer) CASE: file
        in the case of a directory only filename is None
        """
        self._removeKills(masterList)
        masterList.sort()
        if masterList[-1][0] == 0:
            return None
        else:
            if retTuple: 
                return (self.rootDir,masterList[-1][1])
            else:
                return os.path.join(self.rootDir,masterList[-1][1])
               # return ''.join([self.rootDir,masterList[-1][1],'\\']) # equivalent to: self.Rootdir + masterList[-1][1] + '\\'
        return None   
    
    def _removeKills(self,masterList):
        """
        changes any kills in the masterList to 0 a sortable non match
        """
        for aList in masterList:
            if aList[0] == 'kill':
                aList[0] = 0 #no match
    #end query methods
    
class TVRepository(QueryableRepository):
    """
    subclass that sets the match criteria to TV file
    """
    #add criteria to the class as these are standard.  No need to make new ones with each instance
    _classDirCriteria = [ExactSimilarCriterion()]
    _classFileCriteria = [IdentityKillCriterion()] + _classDirCriteria + [TvSeasonEpisodeCriterion()]
    
    def __init__(self,dirname):
        super(TVRepository, self).__init__(dirname)
        #copy class variables into the instance.  to facilitate manipulation of criteria...if ever desired
        self.dircriteria = TVRepository._classDirCriteria
        self.filecriteria = TVRepository._classFileCriteria
        
        
    def _addChildRepo(self,repDir):
        self.repositories[repDir] = TVRepository(repDir)
    