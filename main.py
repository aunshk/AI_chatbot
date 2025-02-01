import requests
import json
import gradio as gr
import time  # Import time module to measure duration

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

def generate_response(prompt):
    # Record start time
    start_time = time.time()

    # Initialize conversation history for each request
    conversation_history = [prompt]

    data = {
        "model": "mistral",
	#"model": "TinyLlama",
	#"model": "deepseek-r1:1.5b",
        "stream": True,  # Enable streaming to get responses line by line
        "prompt": prompt,
    }

    # Send the request with streaming enabled
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)

    # Initialize output for streaming response
    current_response = ""

    # To capture the total time taken
    if response.status_code == 200:
        for chunk in response.iter_lines():
            if chunk:
                decoded_chunk = chunk.decode('utf-8')
                try:
                    # Parse JSON response from chunk
                    data = json.loads(decoded_chunk)
                    actual_response = data.get("response", "")

                    # Append the response to the current response being built
		    current_response += actual_response
                    # Yield the current response progressively
                    yield current_response

                except json.JSONDecodeError:
                    # Handle incomplete or invalid chunks gracefully
                    continue

        # After streaming is finished, calculate total time taken
        end_time = time.time()
        time_taken = end_time - start_time

        # Return the final response along with time taken
        final_output = f"{current_response}\n\nTime taken: {time_taken:.4f} seconds"
        return final_output
    else:
        print("Error:", response.status_code, response.text)
        return None

# Create the Gradio Interface with the Textbox for user input and "text" output
iface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text",
    live=False  # This ensures the "Submit" button is still visible
)

iface.launch(server_name="0.0.0.0")
# Launch with share=True to generate a public link
#iface.launch(share=True)
