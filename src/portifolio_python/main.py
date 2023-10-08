import streamlit as st

from portifolio_python.lib import get_pins_from_html


GH_USER = 'brunodavi'
GH_USER_URL = f'https://github.com/{GH_USER}'


st.image(f'{GH_USER_URL}.png', width=128)

st.markdown(
    f'''
    # Bruno Davi Andrade dos Santos
    ## Desenvolvedor Full-Stack

    ### Sobre

    Sou apaixonado por automações que tornam as tarefas mais simples,
    que desenvolvi em quando criava projetos no Tasker
    um aplicativo que programa automações no Android

    Por conta das suas limitações, embarquei nessa jornada de me tornar
    um desenvolvedor e durante minha carreira, contribui em alguns projetos
    de automação e traduzi alguns projetos e trabalhei e outros utilizando
    metodologias ágeis (Scrum, Kanban), criando páginas no front-end (React, Redux)
    e trabalhando em APIs back-end (FastAPI, Express, MySQL, Mongo).

    ### Experiência Profissional
    - Conveste Serviços Financeiros    Abril 2022 - Abril 2023
        - Aprimorava aplicações web legados com C#, adicionando campos de entrada para os usuários
        detalharem os relatórios
        - Trabalhava em equipe, solucionando problemas em APIs usando Python e FastAPI,
        com SQLAlchemy para me conectar nos bancos de dados e depois transformá-los com
        o Pandas em uma planilha Excel
        - Melhorei a performance de uma API, melhorando a entrega dos clientes
        internos para trabalharem com mais eficiência
        - Gerenciei o Azure DevOps adicionando variáveis de ambiente para configurar os bancos de
        dados de produção, qualidade e desenvolvimento sem atualizar o código
        - Criei aplicações de logs para analisar a telemetria do usuário,
        gargalos da aplicação, e bugs com o App Insights

    ### Habilidades
    - Python
    - Node
    - React
    - Docker
    - RESTful API

    ### Projetos Pinados
    '''
)

for repo in get_pins_from_html(GH_USER_URL):
    st.markdown(
        f'- [{repo}]({GH_USER_URL}/{repo})'
    )


def limpar():
    get_pins_from_html.cache_clear()
    st.toast('Cache limpo')


st.button(
    'Limpar cache',
    help='Remove os projetos fixados da memória, caso tenham atualizado',
    type='primary',

    on_click=limpar,
)