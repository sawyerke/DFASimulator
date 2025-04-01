

statesStr = input("\n Enter the set of states separated by \",\": \n")
startState = input("\n Which state is the starting state? \n")
accept = input("\n Enter the set of accepting states separated by \",\": \n")
languageStr = input("\n Enter the set of input symbols separated by \",\": \n")

language = languageStr.split(', ')
states = statesStr.split(', ')
acceptingStates = accept.split(', ')
transitions = []
dfa_transitions = {}
dfa = {}

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

for i, state in enumerate(states):
    dfa_transitions[state] = {language[j]: transitions[i][j] for j in range(len(language))}

# Construct the DFA object
dfa = {
    "states": states,
    "alphabet": language,
    "start_state": startState,
    "accepting_states": acceptingStates,
    "transitions": dfa_transitions
}

# Print the structured DFA dictionary
print("\nThe DFA is stored as:\n")
import pprint
pprint.pprint(dfa)
