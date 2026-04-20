import sys
data = sys.stdin.read()
lines = data.splitlines()
for line in lines:
  if 'dependabot[bot]' not in line:
    print(line)
