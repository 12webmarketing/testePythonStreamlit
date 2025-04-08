import streamlit as st
from post_crew import CrewPostagem
crew_postagem = CrewPostagem ()

# Configura ção do Streamlit
st . title ('Sistema de Postagem com CrewAI ')

tema = st . text_input ('Digite o tó pico para a postagem ', 'IA na saúde ')

# Bot ão para iniciar o processo
if st . button ('Iniciar Processo ') :
  # Quanto clicar no bot ão carrega um loader
    with st . spinner ( 'Executando tarefas do Crew ... ') :
    # Executando o Crew
      result = crew_postagem . kickoff ( inputs ={ 'topic' : tema })
      st . success ('Processo concluído!')
    # Exibindo resultados
      st . subheader ('Postagem Gerada ')
      st . write (result)