import chardet

with open('pyproject.toml', 'rb') as f:
    result = chardet.detect(f.read())

print(result['encoding'])

