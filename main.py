import csv
import datetime
from functools import reduce



def ReadCSV(caminho):
    array = []
    with open(caminho, encoding="utf8") as f:
        csv_reader = csv.reader(f)
        keys = []
        values = []
        for line_no, line in enumerate(csv_reader, 1):
            if line_no == 1:
                keys = line
            else:
                dict = {}
                values = line
                for i in range(len(keys)):
                    dict.setdefault(keys[i], values[i])
                array.append(dict)
    return array


def WriteCSV(caminho, values):

    with open(caminho, "+a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(values)
        csvfile.close()


def CalcularIngrediente(ingredientes):
    escolha = "1"
    while escolha == "1":
        ingrediente = ""
        custo = 0
        informacoes = []
        print("Qual ingrediente gostaria de calcular o custo?")
        ingrediente = input()
        informacoes = list(
            filter(lambda x: x["Ingrediente"] == ingrediente, ingredientes)
        )
        
        if len(informacoes)>0:
            informacoes=informacoes[0]
            quantidade = 0
            print("Qual foi a quantidade utilizada do ingrediente?")
            quantidade = input()
            custo = (
                float(informacoes["Custo"])
                * float(quantidade)
                / float(informacoes["Quantidade(g)"])
            )
            data = datetime.date.today()
            registro = [
                informacoes["Ingrediente"],
                float(quantidade),
                custo,
                f"{data.day}/{data.month}/{data.year}",
            ]

            WriteCSV("CustoTotal.csv", registro)
            registro.clear()
            escolha = 0

        else:
            print(
                "Ingrediente não encontrado, gostaria de tentar outro?\n1-Sim\nEnter-Não"
            )
            escolha = input()


if __name__ == "__main__":
    ingredientes = ReadCSV("ingredientes.csv")
    escolha = 0
    print("Bem vindo a versão beta do Software de custo diario...")

    while 1:
        print("O que gostaria de fazer?")
        print(
            "1-Calcular o custo de um ou mais Ingredientes no dia\n2-Verificar o Custo total de um dia\n3-Sair"
        )
        escolha = input()

        match escolha:

            case "1":
                custo = []
                while escolha == "1":
                    (CalcularIngrediente(ingredientes))

                    print(
                        "Gostaria de calcular tambénm o custo de outro ingrediente?\n1-Sim\nEnter-Não"
                    )
                    escolha = input()
            
            case "2":
                while(escolha=="2"):
                    print("Qual dia gostaria de saber o custo total?")
                    data = input()
                    filtro = list(filter(lambda x: x['Data']==data,ReadCSV("CustoTotal.csv")))
                    if(len(filtro)>0):
                        custoDia= reduce(lambda custo,registro: custo+float(registro['Custo']),filtro,0)
                        print(f'Custo do dia {data}: R$ {custoDia}')
                        break
                    else:
                        print("Data invalida ou nenhum custo registrado, gostaria de tentar outra data?\n2-sim\nEnter-Não")
                        escolha=input()
                    
                
            case "3":
                print("Saindo do Software...")
                break
