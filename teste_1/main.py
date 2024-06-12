import time

'''
Um cirurgião dentista possui uma agenda disponível para atendimento 
e precisa agendar os pacientes para a semana.


Regras:

- O agendamento não pode se repetir. [X]
- O agendamento será somente para os 3 dias. [X]
- O atendimento não poderá ser dividido em 2 dias. [X]
- Todos devem ser atendidos. [X]


'''


#Lista pacientes:

pacientes = [
    ["Maria Clara", 80],
    ["Pedro Henrique", 90],
    ["Ana Luiza", 60],
    ["Gabriel Oliveira", 70],
    ["João Miguel", 80],
    ["Isabela Fernandes", 65],
    ["Lucas Santos", 85],
    ["Beatriz Almeida", 75]
]

#Lista minutos disponiveis do doutor:

horarios_doutor = [
    ["Segunda-Feira", 300], 
    ["Quarta-Feira", 240], 
    ["Sexta-Feira", 180] 
]

#Dicionario com os valores finais dos dias e os agendamentos dos pacientes:

agendamentos = {
    "Segunda-Feira": [],
    "Quarta-Feira": [],
    "Sexta-Feira": []
}

while pacientes: #Loop While para termos certeza de que a lista de pacientes foi totalmente agendada.

    for dia in horarios_doutor:

        for paciente in pacientes:

            #Se o dia não estiver esgotado de horários, adiciona um paciente no agendamento e exclui ele dos pacientes.
            if((dia[1] - paciente[1]) > 0):
                agendamentos[dia[0]].append(paciente[0])
                dia[1] = dia[1] - paciente[1]
                pacientes.remove(paciente)


#=======================================================================
#BLOCO PARA PRINTAR OS RESULTADOS:

print("Organizando a planilha de clientes para a semana.")
time.sleep(.4)
print(".")
time.sleep(.4)
print(".")
time.sleep(.4)
print(".")
time.sleep(1)

print("===================================================")
print("AGENDAMENTOS DA SEMANA:")


for chave, valor in agendamentos.items():
    print(chave, valor)


print("")