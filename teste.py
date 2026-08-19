from openai import OpenAI


# ==========================================
# CONEXÃO COM A OPENAI
# ==========================================

client = OpenAI()


# ==========================================
# GERAR RECOMENDAÇÕES
# ==========================================

def gerar_recomendacoes(dados):

    agua_atual = dados["agua_atual"]
    agua_anterior = dados["agua_anterior"]

    energia_atual = dados["energia_atual"]
    energia_anterior = dados["energia_anterior"]

    lixo_atual = dados["lixo_atual"]
    lixo_anterior = dados["lixo_anterior"]


    # ==========================================
    # CALCULAR VARIAÇÕES
    # ==========================================

    if agua_anterior > 0:
        variacao_agua = ((agua_atual - agua_anterior) / agua_anterior) * 100
    else:
        variacao_agua = None


    if energia_anterior > 0:
        variacao_energia = (
            (energia_atual - energia_anterior)
            / energia_anterior
        ) * 100
    else:
        variacao_energia = None


    if lixo_anterior > 0:
        variacao_lixo = (
            (lixo_atual - lixo_anterior)
            / lixo_anterior
        ) * 100
    else:
        variacao_lixo = None


    # ==========================================
    # PROMPT
    # ==========================================

    prompt = f"""
Você é um assistente de sustentabilidade residencial.

Analise os dados de uma residência e dê recomendações
simples e práticas para melhorar o consumo de água,
energia e a produção de lixo.

DADOS:

ÁGUA
Mês atual: {agua_atual} litros
Mês anterior: {agua_anterior} litros
Variação: {variacao_agua if variacao_agua is not None else "não disponível"}%

ENERGIA
Mês atual: {energia_atual} kWh
Mês anterior: {energia_anterior} kWh
Variação: {variacao_energia if variacao_energia is not None else "não disponível"}%

LIXO
Mês atual: {lixo_atual} kg
Mês anterior: {lixo_anterior} kg
Variação: {variacao_lixo if variacao_lixo is not None else "não disponível"}%

Faça:

1. Análise da água
2. Dicas para economizar água

3. Análise da energia
4. Dicas para economizar energia

5. Análise do lixo
6. Dicas para diminuir a produção de lixo

7. Compare com o mês anterior

8. Dê uma conclusão geral.

Não invente informações.
Use os valores fornecidos.
Se o consumo aumentou, explique.
Se diminuiu, explique.

Use uma linguagem simples, como se estivesse
explicando para uma família.
"""


    # ==========================================
    # ENVIAR PARA A IA
    # ==========================================

    try:

        resposta = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return resposta.output_text

    except Exception as erro:

        print("\nErro ao consultar a IA:")
        print(erro)

        return None


# ==========================================
# TESTE
# ==========================================

if __name__ == "__main__":

    print("======================================")
    print("   ANÁLISE DE SUSTENTABILIDADE")
    print("======================================")


    # --------------------------------------
    # ÁGUA
    # --------------------------------------

    agua_atual = float(
        input("\nDigite o consumo atual de água (litros): ")
    )

    agua_anterior = float(
        input("Digite o consumo anterior de água (litros): ")
    )


    # --------------------------------------
    # ENERGIA
    # --------------------------------------

    energia_atual = float(
        input("\nDigite o consumo atual de energia (kWh): ")
    )

    energia_anterior = float(
        input("Digite o consumo anterior de energia (kWh): ")
    )


    # --------------------------------------
    # LIXO
    # --------------------------------------

    lixo_atual = float(
        input("\nDigite a produção atual de lixo (kg): ")
    )

    lixo_anterior = float(
        input("Digite a produção anterior de lixo (kg): ")
    )


    # --------------------------------------
    # MONTAR DADOS
    # --------------------------------------

    dados = {

        "agua_atual": agua_atual,
        "agua_anterior": agua_anterior,

        "energia_atual": energia_atual,
        "energia_anterior": energia_anterior,

        "lixo_atual": lixo_atual,
        "lixo_anterior": lixo_anterior
    }


    # --------------------------------------
    # ENVIAR PARA IA
    # --------------------------------------

    print("\n======================================")
    print("Enviando dados para a IA...")
    print("======================================")

    resultado = gerar_recomendacoes(dados)


    # --------------------------------------
    # MOSTRAR RESULTADO
    # --------------------------------------

    if resultado:

        print("\n======================================")
        print("       RECOMENDAÇÕES DA IA")
        print("======================================")

        print(resultado)

    else:

        print("\nNão foi possível gerar recomendações.")


