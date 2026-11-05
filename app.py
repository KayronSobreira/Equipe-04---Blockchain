
class receita:
    def __init__(self, crm, nome_medico, data, nome_paciente, medicamentos):
        self.crm = crm
        self.nome_medico = nome_medico
        self.data = data
        self.nome_paciente = nome_paciente
        self.medicamentos = medicamentos

    def emitir_receita(self):
        if self.medicamentos:
            print(f"Medicamentos: {', '.join(self.medicamentos)}, prescritos para o paciente {self.nome_paciente} pelo médico {self.nome_medico} (CRM: {self.crm}) na data {self.data}.")