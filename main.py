import pprint


transitions = []
dfa_transitions = {}
dfa = {}
states = ""
language = ""
startState = ""
acceptingStates = ""
supportedSeeds = {"substring_001.txt", "remainder_5.txt"}

# assume that the dfa and input string are not invalid
def sim_dfa(dfa, input_string):
    current_state = dfa["start_state"]
    print("\nStarting DFA simulation\n")
    print("Input string is:", input_string)
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

def standard_input():
    statesStr = input("\n Enter the set of states separated by \", \": \n")
    states = [s.strip() for s in statesStr.split(', ')]
    if len(states) != len(set(states)):
        raise ValueError("Duplicate states found.")

    startState = input("\n Which state is the starting state? \n")
    if startState not in states:
        raise ValueError(f"Start state '{startState}' is not a valid state.")

    accept = input("\n Enter the set of accepting states separated by \", \": \n")
    acceptingStates = [s.strip() for s in accept.split(', ')]
    for acc in acceptingStates:
        if acc not in states:
            raise ValueError(f"Accepting state '{acc}' is not a valid state.")

    languageStr = input("\n Enter the set of input symbols separated by \", \": \n")
    language = [s.strip() for s in languageStr.split(', ')]
    if len(language) != len(set(language)):
        raise ValueError("Duplicate input symbols found.")

    print("\n Fill in the transition table for the DFA, using <tab>.\n")
    print("\t", end="")
    for symbol in language:
        print(symbol + "\t", end="")
    print("\n\n")

    for state in states:
        print(state, end="")
        y = input("\t")
        x = y.split('\t')
        if len(x) != len(language):
            raise ValueError(f"Transition error for state '{state}': Expected {len(language)} transitions (one for each symbol), but got {len(x)}.")
        for target_state in x:
            if target_state not in states:
                raise ValueError(f"Transition error for state '{state}': Target state '{target_state}' is not a valid state.")
        transitions.append(x)

def seed_input():
    for file in supportedSeeds:
        print(file)
    file = input("\n Please enter the designated seeded DFA: \n")
    f = open(file, "r")

    statesStr = f.readline()
    states = [s.strip() for s in statesStr.split(', ')]
    startState = f.readline()
    accept = f.readline()
    acceptingStates = [s.strip() for s in accept.split(', ')]
    languageStr = f.readline()
    language = [s.strip() for s in languageStr.split(', ')]

    for state in states:
        y = f.readline()
        x = y.split('\t')
        transitions.append(x)

seed = input("\n Would you like to use a seeded DFA? (y/n) \n")
if seed == "y":
    seed_input()
else:
    standard_input()


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



while True:
    input_string = input("\nEnter a string to test on the DFA (or type 'exit' to quit): ")
    if input_string.lower() == "exit":
        print("Exiting DFA simulation.")
        break


    for i, symbol in enumerate(input_string):
        if symbol not in language:
            raise ValueError(f"Invalid symbol '{symbol}' at position {i} in input string. Allowed symbols: {language}")
    sim_dfa(dfa, input_string)