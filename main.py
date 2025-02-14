
"""import pytube
import ffmpeg
import openai
api_key = "https:/www.youtube.com/watch?v=dQw4w9WgXcQ" # Chave de API do OpenAI
client = openai.OpenAI(api_key=api_key)

# Baixa o audio do arquivo"""
import sys
print(sys.argv[0])
#url = sys.argv[1]
"""filename = "audio.wav"
yt = pytube.YouTube(url)
stream = yt.streams[0].url
ffmpeg.input(stream).output(filename,format="wav",loglevel="error").run()

# Converte o audio para texto
audio_file = open(filename, "r")
transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file).text

# Pede pela revisão
completion = client.chat.completions.create(model="gpt-4o-mini",messages=[{"role": "system", "content": "You are a bot."},{"role": "user", "content": transcript},])
with open("resumo.md", "w+") as md:
    md.write(completion.choices[0].message.content)"""

