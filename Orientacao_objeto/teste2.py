from teste import cria_conta, deposita, saca, extrato

conta = cria_conta(123, 'Alexandre', 55.0, 1000.0)
conta2 = {'numero': 321, 'saldo': 200.0}



print(extrato(conta2))



#conta2['saldo'] = - 50
#depo = deposita(conta2, 15.0)
#conta['saldo'] = conta['saldo'] + 105
#saque = saca(conta, 20.0)






