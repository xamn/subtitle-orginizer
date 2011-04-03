import unittest
from criterion import *

class TestCriterion(unittest.TestCase):
    def testTVSeasonEpisodeCriterionMatchSEformat(self):
        criterion = TvSeasonEpisodeCriterion()
        query = r'The.Big.Bang.Theory.s01e02.srt'
        target = r'The.big.bang.theory.s01e02.720p.DIMENSION.mkv'
        self.assertEqual(0, criterion._assess(query, target))
        
    def testTVSeasonEpisodeCriterionMatchMixedformat(self):
        criterion = TvSeasonEpisodeCriterion()
        query = r'The.Big.Bang.Theory.1x2.srt'
        target = r'The.big.bang.theory.s01e02.720p.DIMENSION.mkv'
        self.assertEqual(0, criterion._assess(query, target))
      
    def testTVSeasonEpisodeCriterionMatchMixedformatRev(self):
        criterion = TvSeasonEpisodeCriterion()
        query = r'The.Big.Bang.Theory.s1e2.srt'
        target = r'The.big.bang.theory.1x2.720p.DIMENSION.mkv'
        self.assertEqual(0, criterion._assess(query, target))
        
    def testTVSeasonEpisodeCriterionMatchXformat(self):
        criterion = TvSeasonEpisodeCriterion()
        query = r'The.Big.Bang.Theory.1x2.srt'
        target = r'The.big.bang.theory.01x02.720p.DIMENSION.mkv'
        self.assertEqual(0, criterion._assess(query, target))
        
        
    def testTVSeasonEpisodeCriterionMismatch(self):
        criterion = TvSeasonEpisodeCriterion()
        query = r'The.Big.Bang.Theory.s01e03.srt'
        target = r'The.big.bang.theory.s01e02.720p.DIMENSION.mkv'
        self.assertEqual('kill', criterion._assess(query, target))

        
        
        
        
if __name__ == '__main__':
    unittest.main()