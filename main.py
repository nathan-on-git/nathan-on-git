class Language:
  def __init__(self, lst):
    self.name = lst[0];
    self.percentage = lst[1];
    self.color = lst[2].strip();

  def __str__(self):
    return f"({self.name},{self.percentage},{self.color})"

def getTemplate(file: str) -> str:
  with open(file, "r") as f:
    return f.read()

def getData(file: str) -> str:
  with open(file, "r") as f:
    languages = [Language(line.split(",")) for line in f.readlines()[1:]]

  # print([str(x) for x in languages])
  languages = sorted(languages, reverse=True, key=lambda x: float(x.percentage))
  # print([str(x) for x in languages])
  result = ""

  for language in languages:
    result += f'<span style="background-color: {language.color};width: {language.percentage}%;" class="progress-item"></span>'

  result += "\n"
  result += getTemplate("./template/middle.txt")

  delay = 0
  for language in languages:
    result += (f'<li style="animation-delay: {delay}ms;">\n' +
      f'<svg xmlns="http://www.w3.org/2000/svg" class="octicon" style="fill:{language.color};"\n' +
      f'viewBox="0 0 16 16" version="1.1" width="16" height="16"><path\n' +
      f'fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path></svg>\n' +
      f'<span class="lang">{language.name}</span>\n' +
      f'<span class="percent">{float(language.percentage):.2f}%</span>\n' +
      f'</li>\n')

    result += "\n"
    delay += 150

  return result + "\n"

def main():
  result = ""
  result += getTemplate("./template/header.txt")
  result += getData("data.csv")
  result += getTemplate("./template/footer.txt")
  with open("languages.svg","w") as f:
    f.write(result)

  return 0

if __name__ == "__main__":
  main()