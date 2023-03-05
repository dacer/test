from real_url.douyu import DouYu

s = DouYu(74751)
s.did = s.get_did()
print(s.get_real_url())