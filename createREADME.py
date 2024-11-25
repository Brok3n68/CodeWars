"""
  Python file to generate the README.md file every time i upload a new kata
  Each folder in the path represents a Language (except paths starting with ".")
  and each file in the folder represents a Kata (except files that do not start with a bracket "[")
  Credits to https://github.com/KonstantinosAng/CodeWars/blob/master/Makefile
"""

import os

ABSOLUTE_FILE_PATH = os.path.dirname(os.path.realpath(__file__))

constTemplate = """
# CodeWars

<div align="center">

  My Kata Solutions for [CodeWars](https://www.codewars.com)

  Profile: [Brok3n68](https://www.codewars.com/users/Brok3n68)

  <a href="https://www.codewars.com/users/Brok3n68" target="_blank">
    <img src="https://www.codewars.com/users/Brok3n68/badges/large" alt="Codewars Warrior" width="500px"/>
  </a>

  __AUTO GENERATED FILE__

</div>
"""

if __name__ == '__main__':
  dirs = {key:[] for key in os.listdir(ABSOLUTE_FILE_PATH) if os.path.isdir(os.path.join(ABSOLUTE_FILE_PATH, key)) and key[0] != '.'}
  for folder in dirs: dirs[folder] = sorted([x for x in os.listdir(os.path.join(ABSOLUTE_FILE_PATH, folder)) if x[0] == "["], key=lambda x: x[1])
  kataTemplate = ""  
  for folder, files in dirs.items():
    kataTemplate += f"""

## {folder}

    """
    for file in files:
      kataTemplate += f"""
* [{file}](./{folder}/{file.replace(" ", "%20")})
"""
  
  readme = "".join([constTemplate, kataTemplate])
  if os.path.exists(os.path.join(ABSOLUTE_FILE_PATH, 'README.md')): os.remove(os.path.join(ABSOLUTE_FILE_PATH, 'README.md'))
  with open(os.path.join(ABSOLUTE_FILE_PATH, 'README.md'), 'w', encoding="utf-8") as file: file.write(readme)