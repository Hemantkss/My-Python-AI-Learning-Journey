import uvicorn
from fastapi import FastAPI, Request, HTTPException
from src.graphs.graph_builder import GraphBuilder
from src.llms.openai_llm import OpenAI_LLM

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI()

# ==========
# APIs
# ==========
@app.post("/blogs")
async def generate_blogs(request: Request):
    data = await request.json()
    topic = data.get("topic", "")
    language = data.get("language", "")

    if not topic:
        raise HTTPException(status_code=400, detail="Topic is required to generate a blog.")

    try:
        # Get LLM
        openai_llm = OpenAI_LLM()
        llm = openai_llm.get_llm()

        # Get graph
        graph_builder = GraphBuilder(llm)
        

        # Invoke graph
        if topic and language:
            graph = graph_builder.setup_graph(usecase="language") 
            state = graph.invoke({"topic": topic, "current_language": language.lower()})
            
        elif topic:
            graph = graph_builder.setup_graph(usecase="topic")
            
            state = graph.invoke({"topic": topic})

        return {"data": state}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
