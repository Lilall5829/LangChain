from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)
messages=[
    SystemMessage(content="You are a helpful expert in social media content strategy and marketing."),
    HumanMessage(content="I need to create a social media campaign for a new product. What are the best practices for creating a campaign? "),
    AIMessage(content="To create an effective social media campaign for a new product: 1) Define clear goals and KPIs. 2) Identify your target audience precisely. 3) Choose appropriate platforms where your audience is active. 4) Create compelling, consistent messaging highlighting unique value. 5) Use a mix of content types (videos, images, testimonials). 6) Implement a content calendar. 7) Allocate budget for both organic and paid promotion. 8) Collaborate with influencers relevant to your niche. 9) Monitor performance metrics. 10) Be prepared to adjust strategy based on data.Give me a brief summary in 200 words"),
]
result=llm.invoke(messages)
print(result.content)


