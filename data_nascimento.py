#-*- coding: latin1 -*-
from datetime import date

dia_nasc = int(input("Digite o dia do seu nascimento: "))
mes_nasc = int(input("Digite o mês do seu nascimento: "))
ano_nasc = int(input("Digite o ano de seu nascimento: "))

def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if mes in (4, 6, 9, 11):
        return 30
    if mes == 2:
        return 29 if eh_bissexto(ano) else 28
    return 0

def calcular_idade_exata(dia_nasc, mes_nasc, ano_nasc):
    hoje = date.today()
    dia_atual = hoje.day
    mes_atual = hoje.month
    ano_atual = hoje.year

    # --- PASSO 1: CÁLCULO DOS DIAS ---
    if dia_atual >= dia_nasc:
        dias_finais = dia_atual - dia_nasc
    else:
        mes_anterior = mes_atual - 1
        ano_do_mes_anterior = ano_atual

        if mes_anterior == 0:
            mes_anterior = 12
            ano_do_mes_anterior = ano_atual - 1

        dias_no_mes_anterior = obter_dias_no_mes(mes_anterior, ano_do_mes_anterior)

        dias_finais = (dia_atual + dias_no_mes_anterior) - dia_nasc
        mes_atual = mes_atual - 1

    # --- PASSO 2: CÁLCULO DOS MESES ---
    if mes_atual >= mes_nasc:
        meses_finais = mes_atual - mes_nasc
    else:
        meses_finais = (mes_atual + 12) - mes_nasc
        ano_atual = ano_atual - 1

    # --- PASSO 3: CÁLCULO DOS ANOS ---
    anos_finais = ano_atual - ano_nasc

    return anos_finais, meses_finais, dias_finais

anos, meses, dias = calcular_idade_exata(dia_nasc, mes_nasc, ano_nasc)

# Exibe o resultado final na tela
print(f"Idade: {anos} anos, {meses} meses e {dias} dias.")
