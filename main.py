# main.py
from controllers.controle_produto import ControleProduto  #Aqui está dizendo que o ControleProduto foi importado da pasta controlles do arquivo controle_produto

def main():
    controller = ControleProduto() #Aqui está sendo criado uma instancia de controle

    print("=== Cadastro de Produtos ===\n")

   
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    descricao = input("Digite a descrição (opcional): ") or ""

    if  controller.create_produto(nome, preco, descricao):
        print("\n🎉 Produto cadastrado com sucesso!")
    else:
        print("\n❌ Falha ao cadastrar o produto.")

if __name__ == "__main__":
    main()#“Só execute a função main() se este arquivo for o ponto de partida do programa. Se estou sendo importado por outro arquivo, não execute nada. isto que está sendo falado 