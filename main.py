

statesStr = input("\n Enter the set of states separated by \",\": \n")
startState = input("\n Which state is the starting state? \n")
accept = input("\n Enter the set of accepting states separated by \",\": \n")
languageStr = input("\n Enter the set of input symbols separated by \",\": \n")

language = languageStr.split(', ')
states = statesStr.split(', ')
acceptingStates = accept.split(', ')
transitions = []

print("\n Fill in the transition table for the DFA, using <tab>.\n")
print("\t", end="")
for symbol in language:
    print(symbol + "\t", end="")
print("\n\n")

for state in states:
    print(state, end="")
    y = input("\t")
    x = y.split('\t')
    transitions.append(x)

print("\n The DFA stored as an array of transitions:\n")
print(transitions)

    
