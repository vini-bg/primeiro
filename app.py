nome= (input("Nome do aparelho: "))

potencia = float(input("Qual a potência do aparelho? "))
    
horas_dia = float(input("Digite o tempo média de uso diário em horas: "))

consumo_mensal = (potencia * horas_dia*30)/1000

print (f"Aparelho:{nome}, Consumo estimado: {consumo_mensal:.0f} kWh/mês")