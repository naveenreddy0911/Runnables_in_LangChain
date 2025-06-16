from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Summarize the following report upto 70 words:\n{report}",
    input_variables=["report"]
)

model=ChatOpenAI()

parser=StrOutputParser()

report_generator=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>70,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

chain=RunnableSequence(report_generator,branch_chain)

result=chain.invoke({"topic":"cricket"})

print(result)