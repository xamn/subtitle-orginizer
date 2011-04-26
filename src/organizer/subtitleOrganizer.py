from repository import *
import shutil
import os.path

class subtitleOrganizer(object):
    def __init__(self,subRep,movRep):
        try:
            self.subtitleRepository = Repository(subRep)
            self.movieRepository = TVRepository(movRep)
        except OSError:
            raise
        
        
    def organize(self):
        #iterate over the files in the subtitleRepository
        #find the directory they belong in and FUTURE move them there.
        #FUTURE find the matching movie file and rename the subtitlefile
        
        for subFile in self.subtitleRepository.iterOverFiles():
            target = self.movieRepository.placeFile(subFile)
            if target:
                self.transferSub(self.subtitleRepository.rootDir,subFile,target[0],target[1])
    
                
    def organizeRep(self):
        """
        checks for subtitles in the tvrepository only, and will place them as normal
        from that repository on
        """
        for subFile in self.movieRepository.iterOverFiles(extFilter='srt'):
            target = self.movieRepository.placeFile(subFile)
            if target:
                self.transferSub(self.subtitleRepository.rootDir,subFile,target[0],target[1])
                
    
    def transferSub(self,sourceDir,sourceFile,destDir,destFile,subExt='srt'):
        """
        sourceDir is location of sourceFile
        destDir is location of destFile
        renames sourceFile to match destfile (minus extension) then moves it to destdir
        """
        newName = destFile[:-3] + subExt

        shutil.move(os.path.join(sourceDir, sourceFile),os.path.join(destDir,newName)) 