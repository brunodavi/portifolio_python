import streamlit as st

from portifolio_python.lib import get_pins_from_html
from portifolio_python.components import image_static


USER_NAME = 'brunodavi'
EMAIL = 'brunodaviandrade2000@gmail.com'
NUMBER = '(11) 98736-4471'

GH_USER_URL = f'https://github.com/{USER_NAME}'
LK_USER_URL = f'https://linkedin.com/in/{USER_NAME}'

EMAIL_URL = f'mailto:{EMAIL}'
WA_CHAT = 'https://wa.me/5511987364471'



with st.sidebar:
    image_static('profile', GH_USER_URL, 'profile.jpeg', width=128)

    '''
        - [Sobre](#sobre)
        - [Experiencia Profissional](#experiencia-profissional)
        - [Habilidades](#habilidades)
        - [Projetos Fixados](#projetos-fixados)

        ---
    '''


    [col1, col2, col3] = st.columns(3)

    with col1:
        image_static('github', f'{GH_USER_URL}/portifolio_python', 'github_dark.png')

    with col2:
        image_static('linkedin', LK_USER_URL, 'linkedin_dark.png')
    
    with col3:
        image_static('whatsapp', WA_CHAT, 'whatsapp_dark.png')


f'''
# Bruno Davi Andrade dos Santos
> :e-mail: [{EMAIL}]({EMAIL_URL}) | :telephone_receiver: [{NUMBER}]({WA_CHAT})

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

### Experiencia Profissional

> Abril 2022 - Abril 2023
- Conveste Serviços Financeiros
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


### Projetos Fixados
'''


for repo in get_pins_from_html(GH_USER_URL):
    st.markdown(
        f'- [{repo}]({GH_USER_URL}/{repo})'
    )