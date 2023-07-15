import pandas as pd
import numpy as np
import pinecone
from tqdm.auto import tqdm


# embedding df
df = pd.read_csv('qa_demo.csv', usecols=['text','embedding'])
df['embedding'] = df['embedding'].apply(eval).apply(np.array)

pinecone.init(
    api_key='Your Key', 
    environment='env'
)


index_name = 'chatgpt-demo-cpcs'
if not index_name in pinecone.list_indexes():
    pinecone.create_index(
        index_name, dimension=len(df['embedding'].tolist()[0]),
        metric='cosine'
    )
index = pinecone.Index(index_name)

batch_size = 100

for i in tqdm(range(0, len(df), batch_size)):
    to_upsert = []
    for j in range(i, min(i+batch_size, len(df))):
    	row = df.iloc[j]
    	to_upsert.append(
            (
                str(j),
                row['embedding'].tolist(),
            )
        )
    index.upsert(vectors=to_upsert)

