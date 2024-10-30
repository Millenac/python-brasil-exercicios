def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso > 0:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * 0.001 * dias_atraso
        return valor_prestacao + multa + juros
    else:
        return valor_prestacao

total_pago = 0
qnt_prestacoes = 0

while True:
    valor_prestacao = float(input("Digite o valor da prestação (0 para encerrar): "))
    if valor_prestacao == 0:
        break
    dias_atraso = int(input("Digite o número de dias em atraso: "))

    valor_final = valorPagamento(valor_prestacao, dias_atraso)
    print(f"Valor a ser pago: R$ {valor_final:.2f}")

    total_pago += valor_final
    qnt_prestacoes += 1

print("\nRelatório do dia")
print(f"Quantidade de prestações pagas: {qnt_prestacoes}")
print(f"Total pago: R$ {total_pago:.2f}")