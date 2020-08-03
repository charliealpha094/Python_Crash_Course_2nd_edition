#Done by Carlos Amaral in 01/07/2020

"""
Start with a copy of user_profile.py from page 149. Build a
profile of yourself by calling build_profile() , using your first and last names
and three other key-value pairs that describe you.
"""

#User profile
def build_profile(*user_info):
    """Building a profile coutaining info about myself."""
    print(f"My profile:")
    for info in user_info:
        print(f"-{info}")

build_profile('Carlos', 'Amaral', '26','single', 'Portuguese')
