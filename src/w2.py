from click import prompt
import openai

class w2:
    def __init__(self, API) -> None:
        self.API = API
        self.start_sec = "WINTER: "
        self.end_sec = "Me: "
        self.prompt = ""

    def initalize(self):
        openai.api_key = self.API

    def get_response(self, text):
        start_sequence = f"\n{self.start_sec}"
        restart_sequence = f"\n{self.end_sec}"

        prompt = f"{self.prompt}{restart_sequence}{text}{start_sequence}"
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = prompt,
            temperature = 0.9,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6,
            stop = [self.end_sec, self.start_sec]
        )

        answer = response.choices[0].text.strip()
        prompt += answer + "\n"
        self.prompt = prompt
        return answer
