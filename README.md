![Screenshot 2024-03-06 at 10 14 58 AM](https://github.com/GetStream/meeting-summary-ollama-gemma/assets/12433593/0034a265-37a5-49b3-a30c-d50589d21cb7)

# Using Ollama and Gemma to build an AI meeting summary tool

This repository accompanies [this YouTube video](https://youtu.be/d3Y9kwufJp0). In short, it creates a tool that summarizes meetings using the powers of AI.

The tooling that is used is:

* Python
* [Ollama](https://ollama.com/)
* [Gemma](https://blog.google/technology/developers/gemma-open-models/)

It takes data transcribed from a meeting (e.g. using the [Stream Video SDK](https://getstream.io/video/)) and preprocesses it first. 
Then, it is fed to the Gemma model (in this case, the `gemma:2b` model) to produce a summary.

If you want to learn more, feel free [to reach out](https://twitter.com/getstream_io) or comment under [the YouTube video](https://youtu.be/d3Y9kwufJp0).

If you enjoy the repository, feel free to give it a ⭐️ and share it with your friends.
