from flask import Flask, request
import os, dotenv
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

dotenv.load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/query", methods=["GET"])
def query_index():
  global index
  query_text = request.args.get("text", None)
  if query_text is None:
    return "No text found, please include a ?text=blah parameter in the URL", 400
  response = index.query(query_text)
  return str(response), 200

def initialize_index(index_name):
    global index
    if os.path.exists(index_name):
      index = GPTSimpleVectorIndex.load_from_disk(index_name)

if __name__ == "__main__":
    initialize_index("index.json")
    app.run(host="0.0.0.0", port=5601)
