# 🎲💻 Conway's Game of Life: A Pair Programming Adventure at Recurse Center 🚀🎉

## 📚 Introduction 📚

Hello, and welcome to our implementation of Conway's Game of Life! This project is a special one. Why? Because it's not just a story about cells living and dying on a grid, it's also a testament to the power of collaboration and the value of pair programming. This journey was shared with my amazing partner, @jelenalor.

### 👫 The Power of Pair Programming 💡

Pair programming is a collaborative approach where two programmers share a single workstation (one screen, one keyboard, and one mouse). This project has shown us the significant benefits of such a collaborative approach:

- **Problem-solving**: Two heads are better than one! By working together, we were able to generate diverse solutions and tackle more complex problems.
- **Knowledge sharing**: We learned from each other! It's amazing how different perspectives can enhance understanding and mastery of concepts.
- **Code quality**: Through instant code reviews, we ensured that the code we produced is cleaner, simpler, and less prone to errors.

### 🎲 The Game of Life 🚀

Conway's Game of Life is a cellular automaton invented by John Horton Conway. This game is an excellent case study for exploring the fundamental concepts of computer science and software engineering. The `World` class represents the current state of the game, while the `Rules` class encodes the rules of life and death.

```python
world = World(4)
world.grid = 5
print(world)
```
In the code snippet above, we create a 4x4 world and kickstart life with 5 randomly placed live cells.

### 🎮 The `Play` Class and `Session` Class 🎮

The `Play` and `Session` classes bring the game to life! `Play` extends Python's Cmd class, providing a text-based command line interface for interaction, while `Session` stores the game's progress to allow for game control functions such as pause, resume, and review.

---

## 🌐 External Resources 🌐

- Python Official Documentation: https://docs.python.org/3/
- Conway's Game of Life: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
- Pair Programming: https://www.agilealliance.org/glossary/pairing
- Recurse Center: https://www.recurse.com/

---

## 😅 Conclusion 😅

Our journey through Conway's Game of Life was more than just a coding project; it was an enriching experience of collaborative learning and problem-solving through pair programming. Special thanks to @jelenalor for being an exceptional partner in this adventure. We hope this project inspires you to explore pair programming and to find joy in coding collaboration. Happy coding! 🌌🎲🚀💻🎉
