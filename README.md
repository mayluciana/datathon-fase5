# Datathon-Fase5 - Proposta Decision
Para este trabalho, realizamos inicialmente um diagnóstico completo das bases de dados fornecidas, identificando ocorrências críticas como valores nulos em massa, formatações inconsistentes, duplicidade de colunas, campos compostos e categorias não padronizadas. A partir dessa análise, propusemos ações de saneamento e padronização que impactam diretamente a qualidade dos dados e, consequentemente, a eficiência dos processos de recrutamento e seleção.

Essas tratativas foram fundamentais para sustentar uma das entregas centrais do projeto: o desenvolvimento de um MVP de ranqueamento de candidatos por vaga, construído com base em técnicas de Processamento de Linguagem Natural (NLP). Para isso:

Consolidamos descrições das vagas e perfis de candidatos em textos unificados;

Aplicamos TF-IDF para transformar esses textos em vetores numéricos;

Utilizamos similaridade do cosseno para calcular a aderência entre vaga e candidato;

Geramos um ranking com os candidatos mais compatíveis com cada vaga.

Durante o processo, trabalhamos em estreita colaboração com a empresa Decision, validando as principais dores, entendendo os desafios do time de recrutamento e alinhando nossas propostas às necessidades práticas do negócio. A análise conjunta permitiu refinar o modelo e sugerir melhorias específicas nas bases que elevam significativamente a assertividade do ranqueamento — como a padronização de cargos, áreas de atuação, escolaridade, tecnologias, certificações e descrições de atividades.

Além disso, para atender a uma das dores críticas identificadas no briefing — a dificuldade em mensurar o engajamento dos candidatos — desenvolvemos uma entrevista de engajamento estruturada com apoio de modelos de linguagem (LLM). Esse recurso analisa automaticamente as respostas dos candidatos com base em critérios como palavras-chave, extensão e coerência, atribuindo uma nota de engajamento em escala de 1 a 5. Todos os critérios, blocos de perguntas e parâmetros utilizados estão detalhados no material de proposta.

Juntas, essas soluções — ranqueamento por compatibilidade e avaliação de engajamento — visam otimizar o processo seletivo, promovendo decisões mais rápidas, justas e embasadas em dados.

Abaixo segue link da proposta que criamos para a empresa Decision.
https://datafiap.streamlit.app/

