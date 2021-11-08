import pyjokes
from emoji import emojize
from random_profile import RandomProfile

print(pyjokes.get_joke())

print(emojize(":thumbs_up:"))

rp = RandomProfile(num=2)
print(rp.first_name())
print(rp.full_name())
print(rp.full_profile())