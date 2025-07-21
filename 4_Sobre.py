import streamlit as st

# Página de sobre
st.title('Contatos 📞')
st.markdown('''
Olá! Somos [Luciana May](https://www.linkedin.com/in/luciana-may-a602a5164/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) e [Vanessa Quintino](https://www.linkedin.com/in/vanessa-quintino-9352b513b/) alunas da pós-graduação em Data Analytics na FIAP.

Neste projeto, conduzimos uma análise aprofundada das bases de dados fornecidas, com foco na melhoria de processos relacionados à contratação, recrutamento e seleção. Nosso trabalho contemplou:

➤ Diagnóstico técnico e saneamento de dados

Identificamos problemas como valores nulos em massa, dados sensíveis expostos, formatações inconsistentes, campos compostos em texto livre e categorias com grafias variadas.

Foram aplicadas ações como remoção de colunas duplicadas, conversão de tipos (datas e valores monetários), padronização de categorias e nomes de colunas (snake_case) e deduplicação de registros.


➤ Modelagem de dados

Estruturamos modelos dimensionais para as três bases: vagas, candidatos e prospecção.

Definimos tabelas fato e dimensão, com foco em garantir minimamente dados consistentes, para criação de uma análise escalável.


➤ Desenvolvimento de soluções analíticas

Implementamos um modelo de ranking de candidatos por similaridade textual (TF-IDF + cosseno), cruzando descrições de vagas com perfis profissionais.

Criamos uma entrevista padronizada de engajamento, com avaliação automatizada baseada em palavras-chave e extensão de resposta, ajudando a mensurar motivação, cultura, aprendizado e visão de futuro.


➤ Ferramentas utilizadas

Utilizamos Python e Streamlit para desenvolvimento dos pipelines, dashboards e modelos.

Nosso objetivo foi propor soluções simples que otimizem os processos seletivos da empresa Decision, tornando-os mais inteligentes, rápidos e confiáveis. Acreditamos que este trabalho pode servir como base para uma estrutura de dados mais robusta e orientada à análise preditiva e à automação de decisões.

Ficamos a disposição para esclarecimentos de dúvidas.''')