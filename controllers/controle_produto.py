# controllers/controle_produto.py
from db.database import get_db_connection
from models.produto import Produto  # ← Importa a classe Produto

class ControleProduto:
    def create_produto(self, nome, preco, descricao):
        connection = get_db_connection()
        if not connection:
            return False

        cursor = connection.cursor()
        query = "INSERT INTO produtos (nome, preco, descricao) VALUES (%s, %s, %s)"
        
       
        produto = Produto(nome=nome, preco=preco, descricao=descricao)

        try:
            cursor.execute(query, produto.to_tuple())
            connection.commit()
            produto_id = cursor.lastrowid
            print(f"✅ Produto cadastrado com ID: {produto_id}")
            return True
        except Exception as e:
            print(f"❌ Erro ao cadastrar produto: {e}")  
            connection.rollback()
            return False      
        finally:
            cursor.close()
            connection.close()
    def mostrar_produtos(self):
        connection = get_db_connection()
        if not connection:
            return False
        cursor = connection.cursor()
        try:
            query = "SELECT id, nome, preco, descricao FROM produtos"
            cursor.execute(query)
            produtos = cursor.fetchall() 
            return produtos
        except Exception as e:
            print(f"❌ Erro ao buscar produtos: {e}")
            return []
        finally:
            cursor.close()
            connection.close()
                



