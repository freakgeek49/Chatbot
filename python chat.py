#simple cahtbot with googlegenai
import time
from google import genai
from google.genai import errors


#initialize client with the API key
client = genai.Client(api_key="YOUR_API_KEY_HERE")

#function to chat with the model by handling user input and model response
def chat_with_genai():
    try:
        #specify the model
        chat=client.chats.create(model="gemini-3.8-flash")

        print("chat Session Created type 'close', 'exit', or 'quit' to exit")


        while True:

            #take user prompt 
            user_input = input("You: ").strip()

            
            if user_input.lower() in ["exit","quit","close"]:
                print("Goodbye!")
                break

            if not user_input:
                continue
            #sends the prompt to the model then takes the response
            response=chat.send_message(user_input)

        
            time.sleep(1)


            print("gemini:",response.text)


    except errors.APIError as e:
        print(f"API Error: {e}")

        
    except Exception as e:
        print(f"Unexpected error occured:{e}")


    
if __name__=="__main__":
     chat_with_genai()       