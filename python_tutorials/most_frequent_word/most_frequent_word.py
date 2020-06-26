from collections import  Counter

text = r"Except for papers, external publications, and where otherwise noted, the content on this website is licensed under a Creative Commons Attribution 4.0 International license (CC BY 4.0). This also excludes MIT’s rights in its name, brand, and trademarks. For papers and external publications included on this website, please contact the author(s) or publisher(s) directly for licensing information."
words = text.split()
counter = Counter(words)

print(counter.most_common(3))