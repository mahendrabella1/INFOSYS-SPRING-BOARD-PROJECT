# Medical-Bot - AI-Powered Medical Assistant

## 📌 Introduction
Medical-Bot is an AI-powered assistant designed to answer medical-related questions using advanced language models and vector search capabilities. It leverages **LangChain**, **Pinecone**, **Hugging Face embeddings**, and **Ollama's LLM** to retrieve and generate relevant responses.

## 🛠️ Features
- Supports **PDF document** and **webpage URL** data extraction.
- Stores embeddings in **Pinecone** for efficient retrieval.
- Uses **Hugging Face embeddings** for text similarity search.
- Generates medical responses using **Ollama's LLM (Mistral)**.
- Interactive **Streamlit** UI for easy interaction.

## 🚀 Technologies Used
- **Python** (Backend Development)
- **Streamlit** (User Interface)
- **Pinecone** (Vector Database)
- **Hugging Face** (Embeddings)
- **Ollama** (LLM for Response Generation)
- **LangChain** (RetrievalQA and Chain Management)
- **BeautifulSoup** (Web Scraping)

## 📦 Installation and Setup


### 2️⃣ Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file and add your Pinecone API Key:
```ini
PINECONE_API_KEY=your_pinecone_api_key
```

### 4️⃣ Run the Application
```sh
streamlit run app.py
```

## 🎯 Usage Guide
1. **Upload a PDF** or **Enter a URL** containing medical information.
2. Click **Process Data** to store embeddings in Pinecone.
3. Type your medical query in the text area.
4. Click **Submit Query** to get an AI-generated response.
5. View chat history for previous interactions.



## 🔗 API & Model Details
- **Embeddings Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Database**: `Pinecone`
- **Language Model**: `Ollama (Mistral)`

## 🏗️ Future Enhancements
- Implement **multi-document processing**.
- Add **speech-to-text** for voice-based queries.
- Improve **accuracy and response time** with fine-tuned models.

## 📝 License
This project is licensed under the MIT License.

## 🤝 Contributing
Pull requests are welcome! Feel free to improve features and submit changes.

---
🚀 **Medical-Bot** - Your AI-powered medical assistant for quick and accurate information! 🩺

