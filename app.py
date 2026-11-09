import hashlib

class Receita:
    def __init__(self, crm, nome_medico, data, nome_paciente, medicamentos):
        self.crm = crm
        self.nome_medico = nome_medico
        self.data = data
        self.nome_paciente = nome_paciente
        self.medicamentos = medicamentos
        self.hash_receita = self.gerar_hash()

    def gerar_hash(self):
        #Gera um hash criptográfico dos dados da receita para simular o registro seguro.
        dados = f"{self.crm}-{self.nome_paciente}-{'-'.join(self.medicamentos)}-{self.data}"
        return hashlib.sha256(dados.encode()).hexdigest()

    def emitir_receita(self, medicos_credenciados):
        #Emite a receita apenas se o médico estiver na lista de credenciados.
        if self.crm not in medicos_credenciados:
            print(f"Erro: O médico com CRM {self.crm} não está credenciado para emitir receitas.")
            return False

        if not self.medicamentos:
            print("Erro: A receita não contém medicamentos.")
            return False

        print(f"--- Receita emitida com sucesso! ---")
        print(f"Médico: {self.nome_medico} (CRM: {self.crm})")
        print(f"Paciente: {self.nome_paciente}")
        print(f"Medicamentos: {', '.join(self.medicamentos)}")
        print(f"Hash de Registro (Blockchain/Segurança): {self.hash_receita}\n")
        return True