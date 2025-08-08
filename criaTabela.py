import pandas as pd
import random
from faker import Faker
from xlsxwriter import Workbook

# Configuração
fake = Faker('pt_BR')
random.seed(42)

# Dados fictícios
EDITORAS = ["Companhia das Letras", "Editora Rocco", "Intrínseca", "Record", 
            "Sextante", "Principis", "HarperCollins", "Aleph", "L&PM", "Martins Fontes"]
GENEROS = ["Ficção Científica", "Fantasia", "Romance", "Terror", "Suspense",
           "Biografia", "História", "Autoajuda", "Negócios", "Infantil"]
AUTORES = [fake.name() for _ in range(50)]

# Gerar 200 registros
dados = []
for i in range(1, 201):
    ano = random.randint(1900, 2023)
    preco = round(random.uniform(20, 150), 2)
    dados.append({
        "ID": i,
        "Título": f"{fake.catch_phrase()} - {random.choice(['A Saga', 'O Legado', 'Os Segredos'])}",
        "Autor": random.choice(AUTORES),
        "Ano": ano,
        "Década": f"{ano//10*10}s",
        "Editora": random.choice(EDITORAS),
        "Gênero": random.choice(GENEROS),
        "ISBN": fake.isbn13(),
        "Preço (R$)": preco,
        "Preço c/ Desconto": round(preco * 0.9, 2),
        "Capa URL": f"https://picsum.photos/200/300?random={i}"
    })

# Criar DataFrame
df = pd.DataFrame(dados)

# Salvar como XLSX com formatação avançada
with pd.ExcelWriter("livros_completo.xlsx", engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Livros')
    
    workbook = writer.book
    worksheet = writer.sheets['Livros']
    
    # Formatação
    header_format = workbook.add_format({
        'bold': True,
        'bg_color': '#FFA07A',
        'border': 1,
        'align': 'center'
    })
    
    money_format = workbook.add_format({'num_format': 'R$ #,##0.00'})
    
    # Aplicar estilos
    for col_num, value in enumerate(df.columns):
        worksheet.write(0, col_num, value, header_format)
    
    for row_num in range(1, len(df)+1):
        worksheet.set_row(row_num, 20)
        for col_num in [7, 8]:  # Colunas de preço
            worksheet.write(row_num, col_num, df.iloc[row_num-1, col_num], money_format)

    # Ajustar largura das colunas
    for i, col in enumerate(df.columns):
        max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(i, i, max_len)

print("✅ Planilha 'livros_completo.xlsx' gerada com sucesso!")
print(f"📊 Total de registros: {len(df)}")
print(f"📂 Caminho: {pd.os.path.abspath('livros_completo.xlsx')}")