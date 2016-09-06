import unittest

from datetime import timedelta
from tag_parser import TagParser

class TagParserTest(unittest.TestCase):

  def setUp(self):
    self.tagParser = TagParser()

  def testEphemeral(self):
    tags = ['foo', 'bar', '#ephemeral']
    self.assertTrue(self.tagParser.isEphemeral(tags))

    tags = ['foo', 'bar', '#Ephemeral']
    self.assertTrue(self.tagParser.isEphemeral(tags))

    tags = ['bar', '#Epemeral']
    self.assertFalse(self.tagParser.isEphemeral(tags))

  def testTTLMatch(self):
    tags = ['foo', 'bar', '#1d']
    self.assertEqual(self.tagParser.getTTL(tags), timedelta(days=1))

    tags = ['foo', 'bar', '#987Day']
    self.assertEqual(self.tagParser.getTTL(tags), timedelta(days=987))

    tags = ['foo', 'bar', '#7Wks']
    self.assertEqual(self.tagParser.getTTL(tags), timedelta(weeks=7))

    tags = ['foo', 'bar', '#10seconds']
    self.assertEqual(self.tagParser.getTTL(tags), timedelta(seconds=10))

  def testTTLFail(self):
    tags = ['foo', '#Days']
    self.assertIsNone(self.tagParser.getTTL(tags))

    tags = ['foo', '#day']
    self.assertIsNone(self.tagParser.getTTL(tags))

    tags = ['foo', '#10']
    self.assertIsNone(self.tagParser.getTTL(tags))

    tags = ['foo', '#Yo10Days']
    self.assertIsNone(self.tagParser.getTTL(tags))