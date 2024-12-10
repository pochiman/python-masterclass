import csv
from pathlib import Path

class BarTab:
  def __init__(self, table_number):
    self.table_number = table_number
    self.drinks = []
    self.total = 0
    self.tip = 0
    self.grand_total = 0
  
  def serve_user(self):
    while True:
      name = input("Drink name (or type 'f' to finish): ")
      if name.lower() == 'f':
        break
      
      try:
        cost  = float(input(f"{name} price: "))
      except ValueError:
        print("The price must be a number")
        continue
      
      self.drinks.append((name, cost))

  def calculate_totals(self):
    for _, cost in self.drinks:
      self.total += cost

    self.tip = self.total * 0.20
    self.grand_total = self.total + self.tip


def main():
  tab = BarTab('7')
  print(f"New tab created for table {tab.table_number}")

  tab.serve_user()
  tab.calculate_totals()
  print(tab.total, tab.tip, tab.grand_total)

  return

if __name__ == "__main__":
  main()