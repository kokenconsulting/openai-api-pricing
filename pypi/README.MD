# OPEN AI API - PRICE CALCULATOR

## Overview
This package is created to calculate cost of OPEN AI API usage.

Pricing based on following url : [OPEN AI Pricing API](https://openai-api-pricing-web-api.onrender.com/openai).
Source code: [Github](https://github.com/kokenconsulting/openai-api-pricing)



## Usage

### Installation

Install Page
```
pip install openai-pricing-calc-draft
```


### Without Surrounding Code

```python
from lll_pricing_calculation import calculate_openai_pricing

# Without surrounding Code
costForThousandCurrency,embeddingsCost,promptCost,completionTokenCost,total_cost = calculate_openai_pricing("GPT-3.5 Turbo","4K context",token_counter.total_embedding_token_count,token_counter.prompt_llm_token_count,token_counter.completion_llm_token_count)
print("currency:"+costForThousandCurrency)
print("embeddingsCost:"+str(embeddingsCost))
print("promptCost:"+str(promptCost))
print("completionTokenCost:"+str(completionTokenCost))
print("total cost:"+str(total_cost))
```
### With Surrounding Code Using Llama Index
```python
import tiktoken
from llama_index.callbacks import CallbackManager, TokenCountingHandler
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from lll_pricing_calculation import calculate_openai_pricing

sampleQuery = "Sample Query"
token_counter = TokenCountingHandler(
    tokenizer=tiktoken.encoding_for_model("text-davinci-003").encode,
    verbose=False  # set to true to see usage printed to the console
)
callback_manager = CallbackManager([token_counter])
service_context = ServiceContext.from_defaults(callback_manager=callback_manager)

def askQuestion(quest,storage,service_context,token_counter):
    token_counter.reset_counts()
    # index defined outside
    specificindex = index.get_index(dataFolder,"./storage"+storage,service_context)
    print(quest)
    result = query.query_index(specificindex, quest,"./storage"+storage)
    print(result)
    # otherwise, you can access the count directly
    print("Embeddings Token Counter stuff is below (total_embedding_token_count):")
    print(token_counter.total_embedding_token_count)
    print("Detailed ")
    print('Embedding Tokens: ', token_counter.total_embedding_token_count, '\n',
      'LLM Prompt Tokens: ', token_counter.prompt_llm_token_count, '\n',
      'LLM Completion Tokens: ', token_counter.completion_llm_token_count, '\n',
      'Total LLM Token Count: ', token_counter.total_llm_token_count)

    # CALCULATE PRICING TAKES PLACE HERE
    costForThousandCurrency,embeddingsCost,promptCost,completionTokenCost,total_cost = calculate_openai_pricing("GPT-3.5 Turbo","4K context",token_counter.total_embedding_token_count,token_counter.prompt_llm_token_count,token_counter.completion_llm_token_count)
    print("currency:"+costForThousandCurrency)
    print("embeddingsCost:"+str(embeddingsCost))
    print("promptCost:"+str(promptCost))
    print("completionTokenCost:"+str(completionTokenCost))
    print("total cost:"+str(total_cost))

askQuestion(sampleQuery,"4",service_context,token_counter)
```