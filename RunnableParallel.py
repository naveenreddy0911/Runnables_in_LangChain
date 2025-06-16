from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Explain the following joke:\n{text}",
    input_variables=["text"]
)

model=ChatOpenAI()

parser=StrOutputParser()

joke_generator=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "explanation":RunnableSequence(prompt2,model,parser)
})

chain=RunnableSequence(joke_generator,parallel_chain)

result=chain.invoke({"topic":"cricket"})

print(result)