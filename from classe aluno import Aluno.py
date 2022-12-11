from classe aluno import Aluno



def planner (aluno):

tempo_livre-int (aluno.tempo*60)

tempo_total_minimo=int(aluno.disciplinas*10)



tempo_total=int(((aluno.disciplinas-aluno.dificuldade) *10)+(aluno.dificuldade*30)) if tempo_livre<=tempo_total_minimo or tempo_livre<=tempo_total:

print("Tempo de estudo insuficiente")


else:


print(f"Tempo de estudo total por semana: (tempo_total} minutos")



print("Tempo de estudo das disciplinas difíceis: (aluno.dificuldade*30} minutos") print (f"Tempo de estudo das disciplinas fáceis: {aluno.dificuldade*10) minutos")