Aqui está a versão atualizada do seu **Procedimento Operacional Padrão (POP)**. Introduzi o conceito de heurística para elevar o nível técnico do material, removi termos informais e refinei a linguagem para um ambiente acadêmico de Engenharia de Software.

---

# 📖 Guia de Teste Manual: Moderação de Conteúdo (POP)

Este documento descreve o procedimento para a execução dos testes manuais da plataforma **PRECISA-SE**. O objetivo é comparar a **Heurística Sintática** (filtro legado baseado em strings) com a **Heurística Semântica** (moderação via Inteligência Artificial).

> **Nota Técnica:** Uma *Heurística* em teste de software é uma estratégia ou "regra de bolso" usada para resolver problemas ou tomar decisões. Aqui, avaliamos como o sistema decide o que é seguro ou proibido.

---

## 🏗️ Fase 1: Teste na Interface Local (`app/index.html`)
Nesta fase, testamos a **Heurística Sintática** (baseada na forma e escrita do texto). O objetivo é validar o comportamento do código JavaScript e identificar limitações de lógica rígida.

1. **Abertura:** Localize o arquivo `app/index.html` e abra-o em seu navegador.
2. **Execução:** Utilize as entradas descritas no **Cenário 1** do seu `plano_de_teste.md`.
3. **Exploração de Evasão:** Aplique a heurística de "ataque por variação", tentando burlar o sistema com caracteres especiais ou espaçamentos (ex: `Ar.ara`, `Ar@ra` ou `A r a r a`).
4. **Observação de Falso Positivo:** Tente postar um anúncio legítimo que contenha a palavra proibida (ex: `Vendo arara de roupas em aço`).
5. **Registro:** Anote se o sistema permitiu o conteúdo proibido (**Falha de Segurança**) ou se bloqueou um conteúdo legítimo (**Erro de Usabilidade por Rigidez Lógica**).

---

## 🤖 Fase 2: Validação do "Oráculo" (Uso de IAs Externas)
Aqui validamos a **Heurística Semântica** (baseada no significado e contexto). Testaremos a robustez do nosso "cérebro" (`requisitos/prompt_ia.md`) antes da integração sistêmica.

1. **Preparação:** Abra o arquivo `requisitos/prompt_ia.md` e copie seu conteúdo.
2. **Configuração da IA:** Acesse o [Google Gemini](https://gemini.google.com/) ou [ChatGPT](https://chatgpt.com/), cole o conteúdo do prompt e envie para estabelecer as diretrizes.
3. **Interrogatório:** Envie as frases descritas no **Cenário 2** do plano de teste.
4. **Validação da Heurística Semântica:**
    * **Contextualização:** Observe se a IA entende que "Pássaro azul raro" é um crime ambiental mesmo sem a palavra-chave "Arara".
    * **Desambiguação:** Verifique se ela diferencia o animal (Bloqueado) do móvel doméstico (Permitido).
5. **Critério de Aceite:** A IA deve responder estritamente com **BLOQUEAR** ou **PERMITIR**, baseando-se na intenção do anúncio.



---

## 📊 Fase 3: Comparação e Reflexão
Ao final das fases, analise os resultados para o relatório final:
* O sistema local apresentou **limitação técnica** ao permitir o conteúdo ilegal?
* O sistema local foi **excessivamente rígido** ao bloquear o item de mobiliário?
* A IA conseguiu equilibrar a segurança da comunidade com a usabilidade da plataforma?

---
> **⚠️ ATENÇÃO:** Se a IA permitir a comercialização de um animal silvestre durante o seu teste, a sua heurística de moderação (o **Prompt**) precisa ser refinada. Documente esta necessidade de ajuste em seu relatório.

---
