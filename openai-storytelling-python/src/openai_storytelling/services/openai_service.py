class OpenAIService:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_story(self, prompt, max_tokens=150):
        import openai

        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip() if response.choices else None