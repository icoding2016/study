"""
A Simple Chatbot

- can receive both text and voice (in English) query/response in natual language.
- can answer the query questions using free pre-trained model.
- support continuous converstion (with context)


ToDo: 
- replace / improve the model. Now it's only a dumb bot.

"""

import speech_recognition as sr
import pyttsx3
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class SimpleChatbot:
    valid_modes = ['text', 'voice']
    def __init__(self, model_name='gpt2', mode='text'):
        assert mode in self.valid_modes, f'Invalid mode, only support {self.valid_modes}'
        print("initializaing...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.conversation_history = []
        self.engine = pyttsx3.init()
        self.mode = mode.lower()
        self.r = sr.Recognizer()
        self.max_resp_len = 1000
        self.audio_input_timeout = 5
        self.audio_input_time_limit = 30
        self.audio_input_pause_threshold = 5

    def get_query(self):
        if self.mode in ['text', 't']:
            query = input("Enter your query: ")
        else:
            with sr.Microphone() as source:
                print("Listening...")
                self.r.pause_threshold = self.audio_input_pause_threshold
                audio = self.r.listen(source, 
                                      timeout = self.audio_input_timeout,
                                      phrase_time_limit = self.audio_input_time_limit)
                try:
                    query = self.r.recognize_google(audio)
                    print(f"You    : {query}")
                except sr.UnknownValueError:
                    print("Sorry, could not understand your speech.")
                    query = None
                except sr.RequestError as e:
                    print(f"Error; {e}")
                    query = None
        return query

    def generate_response(self, query):
        if query is not None:
            self.conversation_history.append(query)
            input_text = " ".join(self.conversation_history)
            inputs = self.tokenizer(input_text, return_tensors='pt')
            input_ids = inputs['input_ids']
            attention_mask = inputs['attention_mask']
            pad_token_id = self.tokenizer.pad_token_id
            output = self.model.generate(
                input_ids,
                attention_mask=attention_mask,
                max_length=self.max_resp_len,
                num_beams=5,
                no_repeat_ngram_size=2,
                early_stopping=True,
                pad_token_id=pad_token_id
            )
            response = self.tokenizer.decode(output[0], skip_special_tokens=True)[len(input_text):].strip()
            self.conversation_history.append(response)
            return response
        return None

    def give_response(self, response):
        if response is not None:
            if self.mode == 'voice':
                self.engine.say(response)
                self.engine.runAndWait()
            print(f"Chatbot: {response}")


def test_chatbot():
    mode = input("Enter 'text'/'t' or 'voice'/'v' mode (default is text): ")
    if mode in ['text', 't']:
        mode = 'text'
    elif mode in ['voice', 'v']:
        mode =  'voice'
    else:
        raise ValueError(f"invalid mode {mode}")
    chatbot = SimpleChatbot(mode=mode)
    while True:
        query = chatbot.get_query()
        if not query:
            continue
        if query.lower() in ['quit', 'exit']:
            break
        response = chatbot.generate_response(query)
        chatbot.give_response(response)


if __name__ == "__main__":
    test_chatbot()
