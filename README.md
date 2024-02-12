# Dixit-Senior-Project
Cal Poly Senior Project W/S 2023, David Zeng, Anshul Khandelwal, Rodrigo Canaan

forms folder
- Contains images of combined cards for forms as well as PDFs of the forms, descriptions of the forms, and notebook to merge cards together for the forms

descriptions and analysis folder
- clip and gpt descriptions of cards
- csv analyzing the games that happened on the website data we got, and how often the predictions by players were correct

CLIP_experiments.ipynb
- basic guesser based on CLIP article https://towardsdatascience.com/clip-the-most-influential-ai-model-from-openai-and-how-to-use-it-f8ee408958b1
- Need to have images in the folder, and change file names and prompt in the second to last code block to use
get_clip_guesses.ipynb
- Passes each round into clip to get the clip guess
self_guessing.ipynb
- Generates series of rounds with a prompt to allow a user to guess
