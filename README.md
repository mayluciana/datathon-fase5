# Datathon-Fase5 - Proposta Decision
Para este trabalho, realizamos inicialmente um diagnóstico completo das bases de dados fornecidas, identificando ocorrências críticas como valores nulos em massa, formatações inconsistentes, duplicidade de colunas, campos compostos e categorias não padronizadas. A partir dessa análise, propusemos ações de saneamento e padronização que impactam diretamente a qualidade dos dados e, consequentemente, a eficiência dos processos de recrutamento e seleção.

Essas tratativas foram fundamentais para sustentar uma das entregas centrais do projeto: o desenvolvimento de um MVP de ranqueamento de candidatos por vaga, construído com base em técnicas de Processamento de Linguagem Natural (NLP). Para isso:

1. Consolidamos descrições das vagas e perfis de candidatos em textos unificados;

2. Aplicamos TF-IDF para transformar esses textos em vetores numéricos;

3. Utilizamos similaridade do cosseno para calcular a aderência entre vaga e candidato;

4. Geramos um ranking com os candidatos mais compatíveis com cada vaga.

Para atender a uma das dores críticas identificadas no briefing — a dificuldade em mensurar o engajamento dos candidatos — desenvolvemos uma entrevista de engajamento estruturada com apoio de modelos de linguagem (LLM). Esse recurso analisa automaticamente as respostas dos candidatos com base em critérios como palavras-chave, extensão e coerência, atribuindo uma nota de engajamento em escala de 1 a 5. Todos os critérios, blocos de perguntas e parâmetros utilizados estão detalhados no material de proposta.

A proposta de MVP de ranqueamento de candidatos por vaga tem potencial para ser evoluída e produtizada em fases futuras, conforme o avanço do processo de estruturação e governança das bases.

Durante o desenvolvimento do projeto, a proposta é de trabalhamos em estreita colaboração com a empresa Decision, validando as principais dores, compreendendo os desafios enfrentados pelo time de recrutamento e alinhando nossas sugestões às necessidades reais do negócio. Essa parceria permitirá aprimorar a proposta do modelo e indicar ações estratégicas de melhoria nas bases, essenciais para aumentar a eficácia do ranqueamento.

Entre as principais recomendações, destacam-se a padronização dos títulos de cargo, áreas de atuação, níveis de escolaridade, tecnologias, certificações e descrições das vagas. Essas ações são fundamentais para garantir consistência semântica nos dados e permitir que o mecanismo de comparação entre perfis e vagas — baseado em técnicas de NLP como TF-IDF e similaridade do cosseno — opere com maior precisão e confiabilidade.

Com as bases estruturadas, será possível evoluir o MVP para uma solução automatizada e integrada ao processo seletivo, contribuindo diretamente para a agilidade e assertividade na escolha de candidatos.

Juntas, essas soluções — ranqueamento por compatibilidade e avaliação de engajamento — visam otimizar o processo seletivo, promovendo decisões mais rápidas, justas e embasadas em dados.

Abaixo segue link da proposta que criamos para a empresa Decision.
https://datafiap.streamlit.app/

A proposta completa você encontra no link:
https://drive.google.com/file/d/1UughnOvWfghug9jBONMMgoQYFVZG5akn/view?usp=drive_link
