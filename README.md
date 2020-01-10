# AI-problem--Hide-and-Seek
An interesting solution to a problem based on NQueen Variant

### Problem: 
Place k friends 'F' on the map with valid positions given by '.', such that they cannot see each other. Assume '&' and '@' hinders visibility, while '.' and '#' do not. Two friends can see each other if they are on the same row or column and no '&' or '@' between them.

### Output: 
The code must return a valid arrangement of 'k' friends

#### 1) Search abstraction
- **Set of states:** All possible configurations of k friends (F), on the board such that no two friends can see each other.
- **Successor function:** Add a friend in a '.' location such that on adding the friend the arrangement is still valid and no two friends can see each other.
- **Cost function:** 1 per move
- **Goal State:** A valid N X M grid with an arrangement of k friends in '.' positions, buildings represented by '&', remaining hallways by '.', our position by '#' and luddy given by '@'. Valid state is given by - if two friends are in same row/column, there must be a '&' or '@' between them. 
- **Initial state:** An N X M grid with an arrangement of buildings represented by '&', hallways by '.', our position by '#' and luddy given by '@' and 0 friends ('F')

#### 2) My approach?
Two important ideas are implemented - 1) is_valid() - function to check if a state is valid and 2) visited[] list to maintain visited states

The is_valid() inputs the current grid configuration along with the row and column where a new friend will be placed. For this row and we create a string with '.' and '#' removed. Having a '.' or '#' between friends does not act as a hindrance. Remaining string may look like FF& or F&F or &F& etc. Only when 2 or more Fs are consecutive, its invalid.

Since we are using a stack based algorithm, states may be repeated i.e. explored states may be visited again, increasing the time significantly. We maintain a visisted array that ensures that visited states are not added to fringe again.

When successors are generated, validity of state is checked to reduce number of successors.
