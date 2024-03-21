import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

conversation_history = []

def generate_response(model, job_description,resume_bullet_point):
       
    full_prompt = "I am applyig to this job, here is the job description: {job_description} \n This is my work experience in form of resume bullet points: {resume_bullet_point}, \n Now generate tailored resume bullet points that align with the job description according to my work experrince. \n Give me only  single line resume bullet point which I can add into my Resume."    
    
    data = {
        "model": "SnapAI",
        "stream": False,
        "prompt": full_prompt,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200 and (job_description != "" or resume_bullet_point != ""):
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        return actual_response
    
    elif response.status_code == 200:
        return "Sure, I'd be happy to help you with your resume. Can you provide more details about your experience and what skills are required for this particular job? "
    
    else:
        print(response.status_code, response)
        print("Error Encountered :", response.status_code, response.text)
        return None


css = """
 textarea{
  resize: none !important; /* Disable resizing */
  height: 150px !important; /* Fixed height */
  max-height: 150px !important; /* Max width */
  width: 100% !important; /* Fixed width */
  max-width: 100% !important; /* Max width */
  overflow-y: auto !important; /* Vertical scrollbar on overflow */
}
.title {
  text-align: center;
  width: 100%;
}
"""

# css = """
#  textarea, .output_text{
#   resize: none !important; /* Disable resizing */
#   max-height: 100% !important; /* Max width */
#   overflow-y: auto !important; /* Vertical scrollbar on overflow */

# }
# """


iface = gr.Interface(
    fn=generate_response,
    inputs=[
        gr.Dropdown(choices=["Llama2", "Mistral (**Pro)","GPT 4 (**Pro)"], label="Choose Model", value="Llama2"),  # Dropdown for model selection
        gr.Textbox(
            label="Job Description",
            lines=7,
            placeholder="Enter the Job Description here..."),
        gr.Textbox(
            label="Your Resume Points",
            lines=7,
            placeholder="Enter your Resume bullet point here..."),
    ],
    outputs=gr.Textbox(lines=23, label="Tailored Output",placeholder="Generated Resume bullet points"),
    # outputs="text",
    css=css,
    title="SnapAI",  # This sets the title of the interface
    theme=gr.themes.Base(),   #gr.themes.Default()
    allow_flagging="never"   # This disables the flagging option

)

if __name__ == "__main__":
    iface.launch() 