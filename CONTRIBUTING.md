# Contributing to Training LeetCode

Thank you for considering contributing to this project! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Problem Structure](#problem-structure)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive experience for everyone. We expect all contributors to:

- Be respectful and considerate
- Be collaborative and open to feedback
- Focus on what is best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks or trolling
- Publishing others' private information
- Other conduct that could reasonably be considered inappropriate

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Your environment (Python/Node.js version, OS)
- Code samples or error messages if applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:

- A clear description of the enhancement
- Why this enhancement would be useful
- Any relevant examples or mockups

### Adding New Problems

1. **Choose a problem**: Select a LeetCode problem you want to solve
2. **Check for duplicates**: Ensure the problem hasn't already been added
3. **Create an issue**: Propose adding the problem (optional but recommended)
4. **Follow the structure**: Use the provided templates and structure

## 🏗️ Problem Structure

Each problem should follow this structure:

```
problems/<id>_<slug>/
├── README.md           # Problem description using template
├── solution.py         # Python implementation
├── solution.ts         # TypeScript implementation
└── test_solution.py    # Python tests
```

### README.md

Use `templates/problem_template.md` as a starting point. Include:

- Problem statement
- Difficulty level and topics
- Examples with explanations
- Constraints
- Your approach and thought process
- Time and space complexity analysis

### Solution Files

**Python (`solution.py`)**:
- Use type hints
- Add docstrings for classes and methods
- Follow PEP 8 style guide
- Use descriptive variable names

**TypeScript (`solution.ts`)**:
- Use proper TypeScript types
- Add JSDoc comments
- Follow standard TypeScript conventions
- Export necessary classes/functions

### Test Files

**Python (`test_solution.py`)**:
- Use pytest framework
- Create a test class (e.g., `TestProblemName`)
- Cover edge cases and multiple scenarios
- Use descriptive test method names
- Include docstrings explaining what each test validates

## 💻 Coding Standards

### Python

- Follow PEP 8 style guide
- Use type hints for function parameters and returns
- Maximum line length: 88 characters (Ruff default)
- Use meaningful variable names
- Add docstrings to all public functions and classes
- Format code with Ruff: `ruff format .`
- Check with Ruff: `ruff check .`

### TypeScript

- Use ESLint for linting
- Follow the Airbnb style guide (with modifications)
- Use explicit types, avoid `any`
- Prefer `const` over `let`, avoid `var`
- Use arrow functions for callbacks
- Check code: `npm run lint`

### General Guidelines

- Write self-documenting code
- Keep functions small and focused
- Avoid premature optimization
- Comment complex logic or non-obvious solutions
- Use consistent naming conventions

## 🧪 Testing Guidelines

### Writing Tests

1. **Cover multiple scenarios**:
   - Example cases from LeetCode
   - Edge cases (empty input, single element, etc.)
   - Boundary conditions
   - Large inputs (if relevant)

2. **Test structure**:
   - Arrange: Set up test data
   - Act: Execute the function
   - Assert: Verify the results

3. **Use helper functions**:
   - Create utilities for common setup (e.g., building linked lists)
   - Keep tests readable and maintainable

4. **Descriptive names**:
   - `test_example_1()` for LeetCode examples
   - `test_edge_case_empty_input()` for edge cases
   - Include docstrings explaining the test case

### Running Tests

Before submitting:
```bash
# Run all tests
pytest problems/ -v

# Run with coverage
pytest problems/ --cov=problems --cov-report=html

# Run specific problem tests
pytest problems/0002_add_two_numbers/test_solution.py -v
```

All tests must pass before submitting a pull request.

## 🔄 Pull Request Process

### Before Submitting

1. **Update your fork**:
   ```bash
   git checkout main
   git pull upstream main
   ```

2. **Create a feature branch**:
   ```bash
   git checkout -b add-problem-0123-problem-name
   ```

3. **Make your changes**:
   - Follow the problem structure
   - Implement solutions in both Python and TypeScript (if possible)
   - Write comprehensive tests
   - Update documentation if needed

4. **Test your changes**:
   ```bash
   # Python tests
   pytest problems/ -v
   
   # Python linting
   ruff check .
   ruff format .
   
   # TypeScript linting (if applicable)
   npm run lint
   ```

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add solution for problem 0123: Problem Name"
   ```

6. **Push to your fork**:
   ```bash
   git push origin add-problem-0123-problem-name
   ```

### Pull Request Guidelines

1. **Title**: Use a clear, descriptive title
   - ✅ "Add solution for problem 0123: Two Sum"
   - ❌ "Update files"

2. **Description**: Include:
   - Problem name and number
   - Brief description of your solution approach
   - Any interesting insights or trade-offs
   - Checklist of completed items

3. **Checklist**:
   ```markdown
   - [ ] Problem solution implemented in Python
   - [ ] Problem solution implemented in TypeScript
   - [ ] Tests written and passing
   - [ ] README.md completed with approach and complexity
   - [ ] Code follows style guidelines
   - [ ] All tests pass locally
   ```

4. **Review process**:
   - Address feedback from reviewers
   - Make requested changes
   - Keep the discussion focused and professional

### After Submission

- Be responsive to feedback
- Make changes in the same branch
- Push updates to automatically update the PR
- Once approved, a maintainer will merge your PR

## 🎯 Best Practices

### Solution Approach

1. **Understand the problem** thoroughly before coding
2. **Think about edge cases** early
3. **Consider multiple approaches** and their trade-offs
4. **Start with a brute force solution** if needed
5. **Optimize** based on time/space complexity
6. **Test incrementally** as you develop

### Code Quality

- Write clean, readable code
- Use meaningful variable names
- Keep functions focused and small
- Avoid deep nesting
- Document complex logic
- Remove commented-out code before submitting

### Documentation

- Explain your thought process
- Document time and space complexity
- Describe the algorithm in plain English
- Include diagrams for complex algorithms (if helpful)
- Update the main README if adding new features

## 💡 Tips for Success

- **Start simple**: Begin with easier problems to understand the structure
- **Learn from others**: Review existing solutions for style and approach
- **Ask questions**: If something is unclear, open an issue
- **Be patient**: Code review takes time; reviewers are volunteers
- **Iterate**: Your first solution doesn't have to be perfect
- **Share insights**: Document what you learned from each problem

## 📞 Getting Help

If you need help:

1. Check existing issues and PRs
2. Review this contributing guide
3. Look at existing problem solutions for examples
4. Open an issue with your question

## 🙏 Thank You

Your contributions help make this project better for everyone. Whether you're adding solutions, fixing bugs, improving documentation, or suggesting enhancements, your effort is appreciated!

Happy Coding! 🚀
