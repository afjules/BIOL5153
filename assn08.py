# /usr/bin/env python3

import re

concert = "Katherine went to the concert to see Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friend, Kathrin. Their mercurial friend, katharine, felt left out."
pattern = "(c|k)(ath)+(a|e)*r+(i|y)n+e*"


for match in re.finditer(pattern,concert,re.I):

	# full match 
	sGroup = match.group()
    
	# position of first character in the match
	sStart = match.start()

    # position of last character in the match
	sEnd = match.end()

	# length of match
	length = sEnd - sStart
  
	data = [sGroup, str(sStart),str(sEnd), str(length)]
	print('{0:<15} {1:<8} {2:<8} {3:<8}'.format(*data))