# 🔐 BruteForceSim

**Simulador didático de ataque de força bruta em Python**  
Criado por: `Gawara0`

---

## 🧠 Sobre o projeto

Esse projeto simula como um ataque de **força bruta** funciona na prática:  
Ele tenta descobrir uma senha digitada pelo usuário **gerando todas as combinações possíveis** de letras e números até acertar.

Apesar de ser um exercício educacional, mostra claramente o **custo computacional** e o funcionamento interno de um brute force.

---

## 🎮 Como funciona?

1. O usuário digita uma senha (sem deixar em branco).
2. O programa inicia o ataque.
3. Ele tenta todas as combinações possíveis de:
   - Letras (maiúsculas e minúsculas)
   - Números (0 a 9)
4. Conta o número de tentativas e o tempo total até acertar.
5. Mostra o resultado final com estilo no terminal.

---

## 🖥️ Exemplo de execução

![Image](https://github.com/user-attachments/assets/2883236a-6e69-42df-a0a2-ea116c0fcda8)
> [!NOTE]
> Teste feito pelo mobile
---

## ⚠️ Aviso

Por padrão, o código **não imprime cada tentativa**, pois isso deixaria o processo muito lento.

Se quiser **ver o ataque acontecendo** (ex: "aa", "ab", "ac"...), descomente a linha 24 no código:

```python
# print(tentativa)
```
> [!NOTE]
> Cuidado: ao remover o "#", o processo pode ficar muito mais lento, principalmente com senhas maiores.

---

## 📂 Estrutura do código
- input() para pegar a senha
- string para gerar alfabeto e números
- itertools.product() para gerar combinações com repetição
- ''.join() para transformar tuplas em strings
- time.time() para medir a duração total
- Contador de tentativas
- Mensagens formatadas com pyfiglet no terminal
---

## 🧪 Objetivo educacional
Esse projeto é exclusivamente didático.
É ideal para quem está aprendendo Python e quer entender:
- Como funcionam ataques de força bruta
- Lógica de repetição e controle de fluxo
- Combinação de bibliotecas padrão
- Medição de desempenho de scripts

---

## 🛑 Uso responsável
> Esse script é feito para estudo.
Não utilize esse conhecimento para atividades ilegais, invasões ou testes sem permissão.
Segurança ofensiva deve sempre estar a serviço da ética, da pesquisa e da proteção.
