# SenreniAI: Your AI-Powered Emotional Companion

## Overview

![Alt text](./overview.png)
In today's fast-paced world, managing stress from work or school has become increasingly challenging. Mental health and emotional well-being are more important than ever, yet finding effective ways to regulate our moods can be difficult. Enter SereniAI, an innovative product designed to support your emotional health with the power of AI and haptic technology.

### Why SereniAI?
SereniAI is like a supportive friend, always there to help you modulate your emotions. Leveraging advanced AI and customized haptics, SereniAI represents the cutting edge of "human-in-the-loop" emotional control.

### Key Features:
- **AI Emotion Detector**: Powered by HUME [1], this module accurately identifies your emotional state.
- **AI Emotion Modulator**: Utilizing the capabilities of ChatGPT-4 [2], this module helps guide and adjust your emotions.
- **Customized Haptics Device**: Built with Raspberry Pi and advanced actuators, this device delivers personalized haptic feedback to enhance emotional modulation.

With SereniAI, you can take control of your emotional well-being in a modern, effective way. Experience the future of emotional support with our AI-powered, haptics-enhanced solution.
## Innovative Features
1. **Human-in-the-loop**\
We try connect human directly to the SereniAI. In this way, the interaction is stronger between AI and human because human can actually *feel* and *sense* the impact of AI instead of just chatting in the prompt. 

2. **Combination of AI and Haptics Devices**\
Haptics technology shows great potential for provide human realistic tactile feeling. Most of the current AI's displaying format is graphical or textual. However, haptics technology shorten the distance between AI's output and human user, hence enabling closer interaction. 
3. **Leveraging AI's Power**\
Since LLM's training set including a significant amount of data, it would obtain enough "experience" to play a role as your emotional companion, which means it could generate proper textual instructions to assist human to pursue target emotional state. Later on, these text command will be passed to haptics device for further human-machine interaction.
4. **Contribute Dataset**\
For each given target emotional state $s_t$ and current human emotional state $s_i$, the SereniAI will provide control signal $c_i$ to human using haptics device. As one of the potential project, we could establish a dataset that record each time step's emotional state ($s_i \ \text{and} \ s_t$) and corresonding haptics control ($c_i$). 

### Reference
[1]: HUME AI, https://dev.hume.ai/intro \
[2]: OpenAI, ChatGPT-4, https://openai.com/index/gpt-4/