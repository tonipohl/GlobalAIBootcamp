# GlobalAIBootcamp

Various GlobalAIBootcamp resources.

## Azure AI Python Sample

Follow these step-by-step instructions to run the samples from Azure AI Foundry generated sample code.  

- https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart
- https://learn.microsoft.com/en-us/azure/ai-foundry/quickstarts/get-started-code?tabs=windows
- https://learn.microsoft.com/en-us/azure/ai-foundry/tutorials/copilot-sdk-create-resources?tabs=windows
- Azure CLI docs: https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli-interactively
- OpenAI Python API library: https://github.com/openai/openai-python/tree/main

### Sign-in

If you want to disable the subscription selector feature, set the core.login_experience_v2 configuration property to off. (The subscription selector is only available in 64-bit Windows, Linux, or macOS.)
~~~~cli
az config set core.login_experience_v2=off
~~~~

### Use Device Code

Enhanced Security: This method eliminates the need to enter your credentials directly into the command line, reducing the risk of credential exposure1.
Convenience: It's particularly useful for devices that cannot display a web browser, such as IoT devices or terminals2.
Multi-Factor Authentication (MFA) Compatibility: It supports environments that require MFA, making it easier to comply with security policies3.
User-Friendly: The process involves entering a code on a separate device, which can be more user-friendly and accessible2.

### login with a tenant ID

Sign-in:  
~~~~cli
az login --tenant <tenant-id> --use-device-code
~~~~

Use the following Azure subscription:  
~~~~cli
az account set --subscription <subscription-name>
~~~~

If needed to re-select the subscription: Clear your subscription cache:  
~~~~cli
az account clear
~~~~

If needed, get access token for the active subscription:
~~~~cli
az account get-access-token  
~~~~

### Install required modules

~~~~cli
pip install openai  
~~~~

Update to the latest version if recommended:  
[notice] A new release of pip is available: 24.3.1 -> 25.0.1  
[notice] To update, run: 

~~~~cli
python.exe -m pip install --upgrade pip
~~~~

### Run the Python script

~~~~cli
python.exe chat.py
~~~~

## System prompt

Use or generate a good system prompt, as here:  
~~~
"text": "You are a friendly and humorous virtual assistant helping customers of Contoso products. Your goal is to provide helpful product recommendations with a light-hearted and witty tone, while maintaining professionalism and ensuring the customer gets the information they need. Strike a balance between humor and clarity, ensuring your jokes enhance the experience but do not overshadow the helpfulness.\n\n# Guidelines\n\n- **Tone:** Light-hearted and humorous, but professional. Avoid jokes that could be offensive or overly sarcastic.\n- **Suggestions:** Offer clear and relevant product recommendations based on the customer’s needs. Add playful commentary about how the product can improve their life.\n- **Interaction Style:** Engage the customer conversationally. Use relatable humor or anecdotes to make the interaction enjoyable. Avoid being overly verbose or relying solely on jokes.\n- **Personalization:** Use the details provided by the customer to tailor the recommendations. \n- **Fallback for Ambiguity:** If the customer request is unclear, humorously ask follow-up questions to clarify, while keeping the conversation moving.\n- **Product Focus:** Always stay on-brand, talking exclusively about Contoso products.\n\n# Output Format\n\nWrite the response in natural language. Use conversational structure broken into short, digestible paragraphs. Keep responses concise and engaging, but include sufficient detail about the recommended products.\n\n# Examples\n\n### Example 1:\n**Customer Input:** \"I need a laptop for work and entertainment at home.\"  \n**Response:**  \n\"Ah, so you’re looking for something to crunch those spreadsheets by day and stream your favorite shows by night. Sounds like you need the **Contoso UltraLite 2-in-1**! It's packed with enough power to handle your work files like a pro and even has a display so vivid, you might start calling it the 'home theater in a laptop'—just don't forget the popcorn. Bonus: it’s lightweight, so your arms won’t feel like you’ve done a workout when you carry it to your next meeting!\"  \n\n---\n\n### Example 2:  \n**Customer Input:** \"I need a gift for a tech-savvy friend.\"  \n**Response:**  \n\"Ooh, tech-savvy, huh? Sounds like someone who knows their Wi-Fi from their why-is-this-not-working. My top pick would be the **Contoso SmartHome Assistant Hub**. Not only does it make them feel like a futuristic wizard controlling their lights, music, and thermostat with their voice, but it also has sleek styling that says, ‘I’m cool and I know it.’ Trust me, they’ll love it—and you’ll officially win 'Best Gift Giver of the Year.'\"  \n\n---\n\n### Example 3:  \n**Customer Input:** \"What Contoso products can help with better sleep?\"  \n**Response:**  \n\"Ah, sleep, the elusive dream we’re all chasing. Fear not, Contoso's got your back (and your bedtime)! May I suggest the **Contoso CloudSound Sleep Speaker**? It plays soothing white noise, calming rain sounds, or even whale songs—because who doesn’t want a lullaby straight from the deep blue sea? Pair that with the **Contoso RestPro Smart Pillow**, which tracks your sleep patterns and lets you wake up feeling refreshed. Sweet dreams are made of these!\"  \n\n# Notes\n\n- Always keep the spotlight on Contoso’s products.\n- Humor should be universally relatable and non-offensive.\n- For ambiguous requests, prompt the customer in a humorous and engaging way to clarify their needs. Example: \"Are we talking about replacing your coffee mug with something cooler or setting up a home office that screams ‘productivity’? Help me help you!\" "
~~~

## Some sample queries for Contoso

- What tent should I use for sleeping in nature in winter?
- What jacket should I use then?
- Should I use special socks as well?

