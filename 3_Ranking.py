import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

df_candidatos = pd.read_csv('pages/candidatos_final.csv', on_bad_lines='skip', sep=';') 
df_vagas = pd.read_csv('pages/vagas_final.csv', on_bad_lines='skip', sep=';')

# Exibição lúdica das colunas
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🧑‍💼 Info Candidatos")
    st.code('\n'.join(df_candidatos.columns.tolist()), language='python')
with col2:
    st.markdown("### 💼 Info Vagas")
    st.code('\n'.join(df_vagas.columns.tolist()), language='python')

# Criar texto consolidado do candidato
df_candidatos['perfil_texto'] = (
    df_candidatos['objetivo_profissional'].fillna('') + ' ' +
    df_candidatos['titulo_profissional'].fillna('') + ' ' +
    df_candidatos['nivel_profissional'].fillna('') + ' ' +
    df_candidatos['nivel_academico'].fillna('') + ' ' +
    df_candidatos['nivel_ingles'].fillna('') + ' ' +
    df_candidatos['nivel_espanhol'].fillna('') + ' ' +
    df_candidatos['outro_idioma'].fillna('') + ' ' +
    df_candidatos['cursos'].fillna('') + ' ' +
    df_candidatos['atuacao'].fillna('')
)

# Criar texto consolidado da vaga
df_vagas['texto_vaga'] = (
    df_vagas['titulo_padronizado'].fillna('') + ' ' +
    df_vagas['atuacao_tokenizadas'].fillna('') + ' ' +
    df_vagas['atividade_tokenizadas'].fillna('') + ' ' +
    df_vagas['competencias_tokenizadas'].fillna('')
)

# Converter id para string para evitar problemas de tipo
df_vagas['id_todos_digitos'] = df_vagas['id_todos_digitos'].astype(str)

# --- FILTRO INTERATIVO ---

# Criar lista formatada com ID + título para o selectbox
lista_ids_titulos = (
    df_vagas['id_todos_digitos'] + ' - ' + df_vagas['titulo_padronizado'].fillna('')
).tolist()

# Definir índice padrão para o valor '961' (se existir)
index_padrao = 0
for i, item in enumerate(lista_ids_titulos):
    if item.startswith('961'):
        index_padrao = i
        break

# Selectbox para o usuário escolher a vaga com ID + título
selecao = st.selectbox(
    'Selecione a vaga (ID - Título):',
    options=lista_ids_titulos,
    index=index_padrao
)

# Extrair só o ID da string selecionada (antes do " - ")
id_vaga_escolhida = selecao.split(' - ')[0]

# Função de ranqueamento
def ranquear_candidatos(vaga_texto, candidatos_textos, top_n=5):
    corpus = [vaga_texto] + candidatos_textos
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]
    top_indices = cosine_sim.argsort()[::-1][:top_n]
    return top_indices, cosine_sim[top_indices]

# Filtrar vaga selecionada e mostrar resultados
vaga_filtrada = df_vagas[df_vagas['id_todos_digitos'] == id_vaga_escolhida]

if vaga_filtrada.empty:
    st.error(f"Vaga com id {id_vaga_escolhida} não encontrada.")
else:
    vaga = vaga_filtrada.iloc[0]
    texto_vaga = vaga['texto_vaga']

    # Obter top 5 candidatos
    indices, scores = ranquear_candidatos(texto_vaga, df_candidatos['perfil_texto'].tolist())
    top_candidatos = df_candidatos.iloc[indices].copy()
    top_candidatos['score_aderencia'] = scores

    # Mostrar resultado no Streamlit
    colunas_necessarias = ['codigo_profissional', 'nome', 'perfil_texto', 'score_aderencia']
    for coluna in colunas_necessarias:
        if coluna not in top_candidatos.columns:
            st.warning(f"Coluna '{coluna}' não encontrada em df_candidatos.")

    st.subheader(f'Top 5 Candidatos para a Vaga {id_vaga_escolhida}')
    st.dataframe(top_candidatos[colunas_necessarias])

    # Criar o gráfico de barras horizontais
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x='score_aderencia',
        y='nome',
        data=top_candidatos.sort_values(by='score_aderencia', ascending=False),
        palette='viridis'
    )
    plt.title(f'Top 5 Candidatos para a Vaga {id_vaga_escolhida} por Score de Aderência')
    plt.xlabel('Score de Aderência')
    plt.ylabel('Nome do Candidato')
    plt.xlim(0, 1)
    plt.tight_layout()

    # Exibir gráfico no Streamlit
    st.pyplot(plt)
