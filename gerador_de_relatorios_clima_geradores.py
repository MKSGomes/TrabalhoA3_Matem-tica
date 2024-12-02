import requests
import pandas as pd
import matplotlib.pyplot as plt

# Token e ID fixos
API_TOKEN = "8d2373a4318d1b0b21fab5baa2cf0f3b"
CITY_ID = 5959

# Função para registrar a cidade (usar apenas quando necessário)
def register_city(api_token, city_id):
    url = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/{api_token}/locales"
    payload = {"localeId[]": city_id}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.put(url, data=payload, headers=headers)
    if response.status_code == 200:
        print("Cidade registrada com sucesso.")
    else:
        print(f"Erro ao registrar a cidade: {response.status_code} - {response.text}")
    return response.status_code == 200

# Função para obter previsão do tempo
def get_weather(api_token, city_id):
    url = f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{city_id}/current?token={api_token}"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return {
            "cidade": weather_data['name'],
            "irradiancia": 1000,  # Placeholder
            "temperatura": weather_data['data']['temperature'],
            "umidade": weather_data['data']['humidity'],
            "vento": weather_data['data']['wind_velocity'] if 'wind_velocity' in weather_data['data'] else 2,
            "cobertura_nuvens": 50  # Placeholder
        }
    else:
        print(f"Erro ao obter a previsão: {response.status_code} - {response.text}")
        return None

# Função para prever a geração de energia solar
def prever_geracao_energia(irradiancia, temperatura, umidade, vento, cobertura_nuvens):
    area_painel = 1.5  # m²
    eficiencia_painel = 0.15  # 15% de eficiência
    eficiencia_ajustada = eficiencia_painel - 0.005 * (temperatura - 25)
    fator_umidade = 1 - 0.01 * (umidade - 50) / 50
    fator_vento = 1 + 0.02 * (vento - 2) / 2
    irradiancia_ajustada = irradiancia * (1 - cobertura_nuvens / 100)
    potencia_gerada = irradiancia_ajustada * area_painel * eficiencia_ajustada * fator_umidade * fator_vento
    return potencia_gerada

# Função para calcular a autonomia dos geradores
def calcular_autonomia(capacidade_gerador, consumo_hospitalar, energia_gerada):
    """
    capacidade_gerador: Capacidade total do gerador em kWh.
    consumo_hospitalar: Consumo energético do hospital em kW.
    energia_gerada: Energia solar gerada em kW.
    """
    energia_total = capacidade_gerador + energia_gerada
    autonomia_horas = energia_total / consumo_hospitalar
    return autonomia_horas

# Função para salvar resultados em Excel
def salvar_resultados_excel(data, filename="previsao_energia.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Dados salvos em {filename}")

# Fluxo Principal
if __name__ == "__main__":
    # Apenas registre a cidade se necessário
    # register_city(API_TOKEN, CITY_ID)

    # Obter previsão do tempo
    weather = get_weather(API_TOKEN, CITY_ID)
    if weather:
        # Calcular potência gerada
        weather['potencia_gerada'] = prever_geracao_energia(
            weather['irradiancia'],
            weather['temperatura'],
            weather['umidade'],
            weather['vento'],
            weather['cobertura_nuvens']
        )
        
        # Exemplo de parâmetros hospitalares
        capacidade_gerador = 50  # Capacidade do gerador em kWh
        consumo_hospitalar = 10  # Consumo do hospital em kW
        
        # Calcular autonomia
        weather['autonomia_horas'] = calcular_autonomia(
            capacidade_gerador, consumo_hospitalar, weather['potencia_gerada']
        )
        
        # Criar DataFrame com os resultados e salvar em Excel
        data = [weather]
        salvar_resultados_excel(data)

        # Exibir resultados
        print("\nResultados:")
        print(f"Temperatura: {weather['temperatura']}°C")
        print(f"Umidade: {weather['umidade']}%")
        print(f"Vento: {weather['vento']} m/s")
        print(f"Cobertura de Nuvens: {weather['cobertura_nuvens']}%")
        print(f"Potência Gerada: {weather['potencia_gerada']:.2f} Watts")
        print(f"Autonomia estimada dos geradores: {weather['autonomia_horas']:.2f} horas")
    else:
        print("Não foi possível obter os dados climáticos.")
