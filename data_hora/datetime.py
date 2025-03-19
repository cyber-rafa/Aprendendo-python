from datetime import date, datetime , time

d = date(2020, 10, 2)
print(f"A date e : {d}")

hora = time(12, 30, 20)
print(f"Hora: {hora}")


today = datetime.today()
print(f"data de hoje: {today}")

data_horario = datetime(2002, 6, 12, 12, 30, 20, 102)
print(f"Data e horário: {data_horario}")

print(f"(DD/MM/YYYY): {today:%d/%m/%Y}")