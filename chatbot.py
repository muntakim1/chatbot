from aiml import Kernel

kernel = Kernel()

kernel.learn('brain.aiml')

while True:
    print("Bot->",kernel.respond(input("User-> ")))
