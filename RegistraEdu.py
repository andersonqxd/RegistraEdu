import random

class RegistraEdu:
    def __init__(self):
        self.__alunos = {}
    
    def cadastrarAluno(self, nome, idade, curso):
        id = RegistraEdu.gerarId()
        if id in self.__alunos:
            print(f"Erro: Já existe um aluno com o ID {id}.")
            return
        
        if not nome or not isinstance(idade, int) or not curso:
            print("Erro: Dados inválidos. Certifique-se de que todas as informações estão corretas.")
            return
        
        self.__alunos[id] = {'nome': nome,'idade': idade, 'curso': curso}
        print(f'Aluno {nome} cadastrado com sucesso!')

    def removerAluno(self, nome):
        for id, dados in list(self.__alunos.items()):
            if dados['nome'].lower() == nome.lower():
                del self.__alunos[id]
            else:
                print(f"Erro: Nenhum aluno encontrado com o nome {nome}.")
        
    def listarAlunos(self):
        if not self.__alunos:
            print("Nenhum aluno cadastrado.")
            return
        
        for id, dados in self.__alunos.items():
            print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Curso: {dados['curso']}")
            
    @staticmethod
    def gerarId():
        return random.randint(1, 99)
            
            
            
            
            
            
            

    def main():
        sistema = RegistraEdu()

        while True:
            print("\nMenu Principal")
            print("1. Cadastrar Aluno")
            print("2. Listar Alunos")
            print("3. Remover Aluno")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                nome = input("Digite o nome do aluno: ")
                idade = int(input("Digite a idade do aluno: "))
                curso = input("Digite o curso do aluno: ")
                sistema.cadastrarAluno(nome, idade, curso)
            
            
            elif opcao == "2":
                sistema.listarAlunos()
            
            elif opcao == "3":
                nome = input("Digite o nome do aluno a ser removido: ")
                sistema.removerAluno(nome)
                
            
            elif opcao == "4":
                print("Saindo do sistema. Até mais!")
                break
            
            else:
                print("Opção inválida! Tente novamente.")
            