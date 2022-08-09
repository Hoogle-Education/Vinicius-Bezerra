# função - conjunto bem definido de regras
# função responsável por retornar times com os dados pedidos

#----------------------------

def cria_time_no_placar(time) :
  return {
    "Jgs" : 0, "Vits" : 0,
    "Emps" : 0, "Ders" : 0, 
    "Pts" : 0, "Gsp" : 0, "SGols": 0
  }

#----------------------------

def atualiza_placar(timeC, timeV) :

  casa = timeC['nome']
  visitante = timeV['nome']

  # aumento um jogo no total de jogos
  # para cada time
  placar[casa]['Jgs'] += 1
  placar[visitante]['Jgs'] += 1

  placar[casa]['Gsp'] += (timeC['gols'])
  placar[visitante]['Gsp'] += (timeV['gols'])

  placar[casa]['SGols'] += (timeC['gols'] - timeV['gols'])
  placar[visitante]['SGols'] += (timeV['gols'] - timeC['gols'])

  pontua_vencedor_perdedor(timeC, timeV)
  # aumento o saldo de vitorias do time vencedor
  # aumento o saldo de derrotas do outro
#----------------------------

def pontua_vencedor_perdedor(timeC, timeV) :
  casa = timeC['nome']
  visitante = timeV['nome']

  if timeC['gols'] > timeV['gols'] :
    placar[casa]['Vits'] += 1
    placar[visitante]['Ders'] += 1
    placar[casa]['Pts'] += 3
  elif timeC['gols'] < timeV['gols'] :
    placar[visitante]['Vits'] += 1
    placar[casa]['Ders'] += 1
    placar[visitante]['Pts'] += 3
  else:
    placar[casa]['Emps'] += 1
    placar[visitante]['Emps'] += 1
    placar[casa]['Pts'] += 1
    placar[visitante]['Pts'] += 1

#----------------------------

def interpreta_linha(linha):
  # serve para partir os dados de uma linha
  # transforma em um vetor a cada separação
  times = linha.split(' X ') 
  # removendo espaços em branco e novas linhas pela direita
  times[1] = times[1].rstrip() 
  return times

#----------------------------

def nome(dados_do_time) :
  return dados_do_time.split('#')[0] 
  # ['Flamengo' , '4']

#----------------------------

def gols(dados_do_time) :
  return int(dados_do_time.split('#')[1]) 
  # ['Flamengo' , '4']

#----------------------------

def esta_no_placar(time) :
  # o time com este nome esta no placar ?
  if time['nome'] in placar :
    return True
  else :
    return False

#----------------------------

def le_arquivo(nome_do_arquivo) :

  # abrindo o arquivo que passei o nome
  # e tratando ele pelo nome: meu_arquivo
  with open(nome_do_arquivo) as meu_arquivo :
    
    # para cada linha do meu arquivo
    for linha in meu_arquivo: 
      times = interpreta_linha(linha)        

      time1 = { 'nome' : nome(times[0]) ,
                'gols' : gols(times[0]) }      

      time2 = { 'nome' : nome(times[1]) ,
                'gols' : gols(times[1]) }      

      if not esta_no_placar(time1) :
        placar[time1['nome']] = cria_time_no_placar(time1)
       
      if not esta_no_placar(time2) :
        placar[time2['nome']] = cria_time_no_placar(time1)

      atualiza_placar(time1, time2)
    
  imprime_placar()

#----------------------------
# feedback dos dados do placar

def imprime_placar():
    for key, value in placar.items() :
      print(key + ': ' + str(value) )
    print('-----------------------------')
      
#----------------------------

placar = {} # o placar é um conjunto de informações
le_arquivo( input('Digite o nome do arquivo a ser lido: ') )
