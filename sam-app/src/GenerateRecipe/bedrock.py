import json
import boto3

class Bedrock:

    def generateRecipe(self, input):

        # Initialize the AWS Bedrock client
        bedrock = boto3.client(service_name="bedrock-runtime", region_name="ap-southeast-2")

        #prompt = f"\n\nHuman:List the ingredients for " + input + ".\n\nAssistant:"
        prompt = f"List the metric ingredients for " + input

        body = json.dumps({
            "inputText": prompt, 
            "textGenerationConfig":{  
                "maxTokenCount":128,
                "stopSequences":[], #define phrases that signal the model to conclude text generation.
                "temperature":0, #Temperature controls randomness; higher values increase diversity, lower values boost predictability.
                "topP":0.9 # Top P is a text generation technique, sampling from the most probable tokens in a distribution.
            }
        })
        print("Invoking model...")
        response = bedrock.invoke_model(
            body=body,
            modelId="amazon.titan-text-lite-v1",
            accept="application/json", 
            contentType="application/json"
        ) 

        response_body = json.loads(response.get('body').read())
        outputText = response_body.get('results')[0].get('outputText')
        text = outputText[outputText.index('\n')+1:]
        generated_recipe = text.strip() 

        return generated_recipe