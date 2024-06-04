from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

import yaml

class Agent:

    def __init__(self):
        data_loaded = self.read_prompt()
        llm = None

    def read_prompt(self):
        with open("./prompt/prompts.yml", 'r') as stream:
            self.data_loaded = yaml.safe_load(stream)

    
    def summarizer(self):
        prompt = PromptTemplate(
                template=self.data_loaded['prompts']['summary'],
                input_variables=['user_input'])
        chain = prompt | self.llm | StrOutputParser()
        return chain

    def skills(self):
        prompt = PromptTemplate(
                template=self.data_loaded['prompts']['skills'],
                input_variables=['user_input', 'summary']
                )
        chain = prompt | self.llm | StrOutputParser()
        return chain

    def achievements(self):
        prompt = PromptTemplate(
                template=self.data_loaded['prompts']['achievements'],
                input_variables=['user_input', 'summary', 'skills']
                )
        chain = prompt | self.llm | StrOutputParser()
        return chain

    def keywords(self):
        prompt = PromptTemplate(
                template=self.data_loaded['prompts']['keywords'],
                input_variables=['user_input', 'summary', 'skills', 'achievements']
                )
        chain = prompt | self.llm | StrOutputParser()
        return chain

    def manager(self):
        prompt = PromptTemplate(
                template=self.data_loaded['prompts']['manager'],
                input_variables=['user_input', 'summary', 'skills', 'achievements', 'keywords']
                )
        chain = prompt | self.llm | StrOutputParser()
        return chain

