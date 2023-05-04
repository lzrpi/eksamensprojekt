def evaluate_temperature(temperature):
  if (temperature <= 10):
    return "For koldt til at stå op - bliv i sengen"
  if (temperature <= 15):
    return "For koldt til at arbejde - bliv hjemme"
  if (temperature <= 20):
    return "OK temperatur til en tur i skoven"
  if (temperature <= 22):
    return "Perfekt pausetemperatur"
  return "For varmt til at arbejde - tag til stranden"


def prompt_for_number(message):
  line = input(f"{message} ")
  return float(line)

def confirm(question):
  affirmative = "ja"
  reject = "nej"
  while True:
    response = input(f"{question} ")
    if response in [affirmative, reject]:
      break
    
    print(f"Ugyldigt input: Du skal svare enten '{affirmative}' eller '{reject}'")

  return response == affirmative


def main():
  print("Temperatur vurdering")

  while True:
    temperature = prompt_for_number("Hvad er temperaturen i grader celsius?")
    result = evaluate_temperature(temperature)
    print(result)

    if not confirm("Vil du prøve igen?"):
      break
  


if __name__ == "__main__":
  main()