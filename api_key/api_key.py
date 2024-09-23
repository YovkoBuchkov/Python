def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


query_params = {
    "source": "bbc-news",
    "sortBy": "top",
    "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
}

main_url = "https://newsapi.org/v1/articles"

