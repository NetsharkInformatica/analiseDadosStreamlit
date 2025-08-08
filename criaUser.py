import pandas as pd
from faker import Faker
import random

# Configuração
fake = Faker('pt_BR')
random.seed(42)

# Gerar 20 usuários
dados_usuarios = []
for id_usuario in range(1, 21):
    nome = fake.name()
    email = nome.lower().replace(' ', '.') + '@' + fake.free_email_domain()
    dados_usuarios.append({
        'ID': id_usuario,
        'Nome': nome,
        'Idade': random.randint(18, 70),
        'E-mail': email,
        'Telefone': fake.cellphone_number(),
        'Cidade': fake.city(),
        'Estado': fake.estado_sigla(),
        'Profissão': fake.job(),
        'Data Cadastro': fake.date_between(start_date='-5y'),
        'Ativo': random.choice(['Sim', 'Não'])
    })

# Criar DataFrame
df = pd.DataFrame(dados_usuarios)

# Salvar como Excel
arquivo_excel = "usuarios.xlsx"
df.to_excel(arquivo_excel, index=False, engine='openpyxl')

print(f"✅ Planilha '{arquivo_excel}' criada com sucesso!")
print(f"📊 Total de usuários: {len(df)}")
#print(f"📂 Caminho: {os.path.abspath(arquivo_excel)}")