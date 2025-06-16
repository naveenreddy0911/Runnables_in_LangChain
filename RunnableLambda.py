from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

prompt=PromptTemplate(
    template="Generate a joke about {topic}",
    input_variables=["topic"]
)

model=ChatOpenAI()

parser=StrOutputParser()

joke_generator=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "no._of_words":RunnableLambda(lambda x:len(x.split()))
})

chain=RunnableSequence(joke_generator,parallel_chain)

result=chain.invoke({"topic":"AI"})

print(result["joke"])
print(result["no._of_words"])