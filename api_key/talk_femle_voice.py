import requests
import json


def speak(text):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")

    # Задаване на конкретен женски глас
    voices = speak.GetVoices()
    for voice in voices:
        if "Zira" in voice.GetDescription():
            speak.Voice = voice
            break

    speak.Speak(text)


if __name__ == '__main__':
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }

    main_url = "https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    load = json.loads(res.text)
    speak("Here you listen top BBC news from python code.")
    speak("first news")

    for i in range(5):
        print(load["articles"][i]["title"])
        speak(load["articles"][i]["title"])
        speak("next news")
