# User Input

### States

Enter a list of states separated by commas and spaces. Ex: "Q1, Q2, Q3"

### Starting State

Enter the starting state.

### Accepting States

Enter a list of the accepting states separated by commas and spaces. Ex: "Q2, Q3"

### Alphabet

Enter a list of the alphabet of the input string for the DFA separated by commas and spaces. Ex: "0, 1"

### Table of Transitions

The program will create a table of transitions. The alphabet will be printed along the top and the states will be printed along the left side.
<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 <br />
Q1  
<br />
Q1 in the above example is the current state. When the DFA reads a 0, it needs to know what state to transition to. Enter the state that the DFA would transition to when it reads a 0 then press tab.
When you are done with the line press enter to move to the next state.

# File Input

You can add a text file to reduce repeated DFA inputs. <br />
The first line should be a list of states separated by commas and spaces. Ex: "Q1, Q2, Q3" <br />
The second line should be the starting state. <br />
The third line should be a list of the accepting states separated by comas and spaces. Ex: "Q2, Q3" <br />
The fourth line should be a list of the alphabet of the input string for the DFA separated by commas and spaces. Ex: "0, 1" <br />
Every subsequent line should be a table of transitions. The first row is the first state entered. The subsequent rows are the rest of the states in the order they were entered. The first column is the first character in the alphabet entered. The subsequent columns are the rest of the characters in the order they were entered. These are example states: "Q1, Q2" and this is an example alphabet: "0, 1". The following is an example transition table in the file:

```text
Q2 Q1
Q2 Q2
```

For the above table it is read from top to bottom and left to right: "When the DFA is in state Q1 and reads a 0, it will transition to Q2. When the DFA is in state Q1 and reads a 1, it stays in Q1. When the DFA is in state Q2 and reads a 0 or a 1, it stays in Q2."
