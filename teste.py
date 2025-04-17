import pandas as pd
from datetime import datetime
import random

# Gerar dados fictícios para simular as instruções
data_metro = {
    "PORTAL": random.choices(["Ativo Migrado", "Ativo Não Migrado", "Inativo"], k=20),
    "STATUS ENTREGA FIBRA": random.choices(["Concluído", "Pendente", "Em Andamento"], k=20),
    "ENTREGA FIBRA_PLAN": ["" if random.random() < 0.3 else datetime(2025, 4, random.randint(1, 15)).strftime('%d/%m/%Y') for _ in range(20)],
    "ENTREGA FIBRA_REAL": ["" if random.random() < 0.3 else datetime(2025, 4, random.randint(1, 15)).strftime('%d/%m/%Y') for _ in range(20)],
    "STATUS_LIB": random.choices(["Concluído", "Pendente", "Em Validação"], k=20),
    "LIB_PLAN": ["" if random.random() < 0.3 else datetime(2025, 4, random.randint(1, 15)).strftime('%d/%m/%Y') for _ in range(20)],
    "LIB_REAL": ["" if random.random() < 0.3 else datetime(2025, 4, random.randint(1, 15)).strftime('%d/%m/%Y') for _ in range(20)],
    "ATIVAÇÃO STATUS": random.choices(["Concluído", "Pendente", "Aguardando"], k=20),
    "ATIVAÇÃO_PLAN": ["" if random.random() < 0.3 else datetime(2025, 4, random.randint(1, 15)).strftime('%d/%m/%Y') for _ in range(20)],
    "ATIVAÇÃO_REAL": ["" if random.random() < 0.3 else datetime(2025, 4, random.randint(1, 15)).strftime('%d/%m/%Y') for _ in range(20)],
    "PROJETO": random.choices(["METRO", "VALIDACAO LIB.IMPLANTAÇÃO", "OUTRO"], k=20)
}

# Criar DataFrames
df_portal_fibra = pd.DataFrame(columns=["Coluna Exemplo 1", "Coluna Exemplo 2"])
df_metro = pd.DataFrame(data_metro)
df_base = pd.DataFrame(columns=["Base Exemplo 1", "Base Exemplo 2"])

# Salvar em um arquivo Excel com múltiplas planilhas
file_path = "/mnt/data/RF_x_TX_BA-SE-NE_ABR_MAI_JUN - MAIO.V3.xlsx"
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    df_portal_fibra.to_excel(writer, sheet_name='PORTAL FIBRA', index=False)
    df_metro.to_excel(writer, sheet_name='METRO', index=False)
    df_base.to_excel(writer, sheet_name='BASE', index=False)

file_path
