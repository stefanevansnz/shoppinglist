import numpy as np
import json
import boto3

class Bedrock:

    def generateRecipe(self, input):

        # Initialize the AWS Bedrock client
        bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-west-2")

        prompt = f"\n\nHuman:Generate a step by step recipe for " + input + ".\n\nAssistant:"

        body = json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 300
        })

        modelId = "anthropic.claude-instant-v1"

        response = bedrock.invoke_model_with_response_stream(
            modelId=modelId,
            body=body
        )
        generated_recipe = ""
        if response and 'body' in response:
            stream = response.get('body')
            if stream:
                for event in stream:
                    chunk = event.get('chunk')
                    if chunk:
                        chunk_text = json.loads(chunk.get('bytes').decode())
                        completion = chunk_text.get('completion', '')
                        if completion:
                            generated_recipe += completion
        print(generated_recipe)
        return generated_recipe

# local test
bedrock = Bedrock()
print(bedrock.generateRecipe("meatballs"))