# main.py

from controllers.controle_produto import ControleProduto
from db.database import get_db_connection

#fazer uma função de compra
def cadastrar_produto():
    controller = ControleProduto()
    print("\n=== Cadastro de Produtos ===")

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    descricao = input("Digite a descrição (opcional): ") or ""

    if controller.create_produto(nome, preco, descricao):
        print("\n🎉 Produto cadastrado com sucesso!")
    else:
        print("\n❌ Falha ao cadastrar o produto.")


def listar_produtos():
    connection = get_db_connection()
    if not connection:
        print("❌ Não foi possível conectar ao banco.")
        return

    cursor = connection.cursor()  # 👈 SEM dictionary=True → usa tuplas
    try:
        query = "SELECT id, nome, preco, descricao FROM produtos ORDER BY id ASC"
        cursor.execute(query)
        produtos = cursor.fetchall()

        if produtos:
            print("\n--- LISTA DE PRODUTOS ---")
            for produto in produtos:
                # Acessa por índice: [0] = id, [1] = nome, [2] = preco, [3] = descricao
                produto_id = produto[0]
                nome = produto[1]
                preco = produto[2]
                descricao = produto[3] or "Sem descrição"
                print(f"ID: {produto_id} | Nome: {nome} | R$ {preco:.2f} | {descricao}")
        else:
            print("\n📝 Nenhum produto cadastrado.")

    except Exception as e:
        print(f"❌ Erro ao buscar produtos: {e}")
    finally:
        cursor.close()
        connection.close()


def main():
    while True:  # ← LOOP PRINCIPAL AQUI!
        print("\n=== MENU DE PRODUTOS ===")
        print("1 - Cadastrar produto")
        print("2 - Listar todos os produtos")
        print("3 - Sair")

        try:
            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                cadastrar_produto()
            elif opcao == "2":
                listar_produtos()
            elif opcao == "3":
                print("\n👋 Até logo!")
                break
            else:
                print("\n❌ Opção inválida. Tente novamente.")

        except ValueError:
            print("\n❌ Digite um número válido.")


if __name__ == "__main__":
    main()