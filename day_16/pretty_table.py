from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokomane", ["pikachu", "Combee", "Pichu"])
table.add_column("Type", ["Electric", "Dont know", "Electric"])

table.align = "l"

print(table)