import os
from dotenv import load_dotenv
from agents import Agent
from util.read_pdf import load_resume
from langchain_groq import ChatGroq

load_dotenv()

ag = Agent()
ag.llm = ChatGroq(temperature=0.7, model_name="mixtral-8x7b-32768")

agent_summarizer = ag.summarizer()
agent_skills = ag.skills()
agent_achievements = ag.achievements()
agent_keywords = ag.keywords()
manager = ag.manager()

file_path = os.getenv('RESUME_FILE_PATH')

user_input = load_resume(file_path)

summary = agent_summarizer.invoke({'user_input': user_input})
print('***** SUMMARY *****')
print(summary)

skills = agent_skills.invoke({'user_input':user_input, 'summary':summary})
print('***** SKILLS *****')
print(skills)

achievements = agent_achievements.invoke({'user_input':user_input, 'summary':summary, 'skills':skills})
print('***** ACHIEVEMENTS *****')
print(achievements)

keywords = agent_keywords.invoke({'user_input':user_input, 'summary':summary, 'skills':skills, 'achievements':achievements})
print('***** KEYWORDS *****')
print(keywords)

final_result = manager.invoke({'user_input':user_input, 'summary':summary, 'skills':skills, 'achievements':achievements, 'keywords': keywords})
print('\n\n******** FINAL RESULT *********')
print(final_result)

