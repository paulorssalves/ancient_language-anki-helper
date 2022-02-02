# Ancient Language Anki Helper

**Propósito**: servir de apoio para estudar línguas antigas (padrão: grego antigo), ajudando popular planilhas .csv para estudar no Anki. Usa o Wiktionary como fonte das definições, exemplos e tudo o mais.

## Afazeres:
- Remover colchetes e aspas do output em .csv
- Agrupar as partes que são output do `get_definitions()`
    - Isto é, uma palavra pode ser tanto adjetivo quanto substantivo. Deve-se agrupar os exemplos dela como adjetivo à categoria "adjetivo", e igualmente para os substantivos, **na mesma célula**.
- Limpar os exemplos. Encontrar alguma forma de melhor organizá-los.
