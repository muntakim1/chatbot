from aiml import Kernel

kernel = Kernel()

kernel.learn('brain.aiml')

print("Say Hello! and ask questions like, I want to know about loan")

while True:
    print("Bot->",kernel.respond(input("User-> ")))
