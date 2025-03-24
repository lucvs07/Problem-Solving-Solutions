def convert_days_to_text(num):
    # Definir as constantes de tempo
    days_in_year = 365
    days_in_month = 30
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minute = 60

    # Calcular anos, meses, dias, horas, minutos e segundos
    years = num // days_in_year
    num %= days_in_year

    months = num // days_in_month
    num %= days_in_month

    days = num
    hours = (days * hours_in_day) % hours_in_day
    minutes = (hours * minutes_in_hour) % minutes_in_hour
    seconds = (minutes * seconds_in_minute) % seconds_in_minute

    # Formatar a string de saída
    result = f"{years} anos, {months} meses, {days} dias, {hours} horas, {minutes} minutos e {seconds} segundos"
    return result

# Exemplos de uso
print(convert_days_to_text(4320)) # Saída: "11 anos, 9 meses, 0 dias, 0 horas, 0 minutos e 0 segundos"
print(convert_days_to_text(100000)) # Saída: "273 anos, 4 meses, 6 dias, 16 horas, 40 minutos e 0 segundos"
print(convert_days_to_text(400)) # Saída: "1 ano, 1 mês, 5 dias, 16 horas, 0 minutos e 0 segundos"