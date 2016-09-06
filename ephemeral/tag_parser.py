import re
from datetime import timedelta

# Tags are expected to be an array of strings

class TagParser():
  _ephemeralTags = set(['#ephemeral', '#Ephemeral'])
  
  _TTLKeyToTags = {
    'seconds': ['sec', 'secs', 'second', 'seconds'],
    'minutes': ['min', 'mins', 'minute', 'minutes'],
    'hours': ['h', 'hr', 'hrs', 'hour', 'hours'],
    'days': ['d', 'day', 'days'],
    'weeks': ['w', 'wk', 'wks', 'week', 'weeks']
  }

  _TTLTagsToKey = {tag: key for key, tags in _TTLKeyToTags.items() for tag in tags}
  
  _TTLRegex = re.compile('#(\d+)([a-zA-Z]+)')  
  
  def isEphemeral(self, tags):
    for tag in tags:
      if tag in self._ephemeralTags:
        return True
    return False

  def getTTL(self, tags):
    for tag in tags:
      m = self._TTLRegex.match(tag)
      if m:
        (delta, unitText) = m.groups()
        unit = self._TTLTagsToKey.get(unitText.lower(), None)
        if unit is not None:
          params = {unit: int(delta)}
          return timedelta(**params)
    return None
