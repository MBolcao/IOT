import speech_recognition as sr
import pyttsx3
import webbrowser

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say('Ola, eu sou a Alexa, o que deseja saber?')
maquina.runAndWait()

def executa_comando():

    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()

            if 'sofia' in comando:
                comando = comando.replace('sofia', '')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone não está funcionando')
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'receita' in comando:
        webbrowser.open("https://322a095c-b502-4fc6-ba6a-e7e7041c6d62-00-lr04j98a0ay8.spock.replit.dev/graficoReceita")
    elif 'receita empresa' in comando:
        webbrowser.open("https://322a095c-b502-4fc6-ba6a-e7e7041c6d62-00-lr04j98a0ay8.spock.replit.dev/graficoReceitaEmp")
    elif 'Receita empresa um' in comando:
        webbrowser.open("https://322a095c-b502-4fc6-ba6a-e7e7041c6d62-00-lr04j98a0ay8.spock.replit.dev/graficoReceitaEmp/1")
    elif 'Receita empresa dois' in comando:
        webbrowser.open("https://322a095c-b502-4fc6-ba6a-e7e7041c6d62-00-lr04j98a0ay8.spock.replit.dev/graficoReceitaEmp/2")
    elif 'fluxo entrada 1' in comando:
        webbrowser.open("https://322a095c-b502-4fc6-ba6a-e7e7041c6d62-00-lr04j98a0ay8.spock.replit.dev/Valores/1/E")
    elif 'fluxo saida 1' in comando:
        webbrowser.open("https://322a095c-b502-4fc6-ba6a-e7e7041c6d62-00-lr04j98a0ay8.spock.replit.dev/Valores/1/S")
    elif 'fluxo entrada 2' in comando:
        webbrowser.open("https://322a095c-b502-4fc6-ba6a-e7e7041c6d62-00-lr04j98a0ay8.spock.replit.dev/Valores/2/E")
    elif 'fluxo saida 2' in comando:
        webbrowser.open("https://322a095c-b502-4fc6-ba6a-e7e7041c6d62-00-lr04j98a0ay8.spock.replit.dev/Valores/2/S")

comando_voz_usuario()