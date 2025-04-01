import pprint

# assume that the dfa and input string are not invalid
def sim_dfa(dfa, input_string):
    current_state = dfa["start_state"]
    print("\nStarting DFA simulation\n")
    print("Input string is ", input_string)
    print(f"\nInitial state: {current_state}\n")

    for index, symbol in enumerate(input_string):
        next_state = dfa["transitions"][current_state][symbol]
        print(f"Step {index + 1}: On input '{symbol}', transitioning from {current_state} to {next_state}")
        current_state = next_state
    
    print("Final state reached:", current_state)
    if current_state in dfa["accepting_states"]:
        print("The string is ACCEPTED by the DFA!\n")
        return True
    else:
        print("The string is REJECTED by the DFA.\n")
        return False


# FIXME: need error checking to make sure all inputs are valid
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

dfa = {
    "states": states,
    "alphabet": language,
    "start_state": startState,
    "accepting_states": acceptingStates,
    "transitions": dfa_transitions
}

print("\nThe DFA is stored as:\n")
pprint.pprint(dfa)

input_string = "1010101000101"
sim_dfa(dfa, input_string)