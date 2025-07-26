from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# Schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="write down the key themes of the review")
    summary: str = Field(description="A summary of the review")
    sentiment: str = Field(description="The sentiment of the review (positive or negative)")
    pros: Optional[list[str]] = Field(description="write down the pros of the review")
    cons: Optional[list[str]] = Field(description="write down the cons of the review")
    name: Optional[list[str]] = Field(description="The name of the reviewer")
    
    
structured_output = model.with_structured_output(Review)

result = structured_output.invoke(
    """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Hemant Sable
""")

print(result)
print(result.key_themes)
print(result.summary)
print(result.sentiment)
print(result.pros)
print(result.cons)
print(result.name)

