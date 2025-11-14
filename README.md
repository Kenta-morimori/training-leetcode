# Training LeetCode

[![Python Tests](https://github.com/Kenta-morimori/training-leetcode/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Kenta-morimori/training-leetcode/actions/workflows/python-tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A structured repository for practicing LeetCode problems with implementations in Python and TypeScript.

## 📁 Repository Structure

```
training-leetcode/
├── problems/                    # LeetCode problems organized by ID and slug
│   └── 0002_add_two_numbers/   # Example problem
│       ├── README.md           # Problem description and approach
│       ├── solution.py         # Python implementation
│       ├── solution.ts         # TypeScript implementation
│       └── test_solution.py    # Python tests
├── templates/                  # Templates for new problems
│   └── problem_template.md    # Problem documentation template
├── .github/
│   └── workflows/
│       └── python-tests.yml   # CI/CD for Python tests
├── .eslintrc.json             # ESLint configuration
├── pyproject.toml             # Python project configuration (Ruff, etc.)
├── package.json               # Node.js project configuration
├── requirements.txt           # Python dependencies
├── LICENSE                    # MIT License
├── CONTRIBUTING.md           # Contribution guidelines
└── README.md                 # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Node.js 18 or higher (for TypeScript solutions)
- pip and npm package managers

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kenta-morimori/training-leetcode.git
   cd training-leetcode
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies:
   ```bash
   npm install
   ```

## 🧪 Running Tests

### Python Tests

Run all Python tests:
```bash
pytest problems/ -v
```

Run tests for a specific problem:
```bash
pytest problems/0002_add_two_numbers/test_solution.py -v
```

Run with coverage:
```bash
pytest problems/ --cov=problems --cov-report=html
```

### TypeScript Tests

```bash
npm test
```

## 🔍 Linting and Code Quality

### Python (Ruff)

Check code:
```bash
ruff check .
```

Auto-fix issues:
```bash
ruff check --fix .
```

Format code:
```bash
ruff format .
```

### TypeScript (ESLint)

Check code:
```bash
npm run lint
```

Auto-fix issues:
```bash
npm run lint:fix
```

## 📝 Adding a New Problem

1. Create a new directory in `problems/` with the format `<id>_<slug>/`:
   ```bash
   mkdir problems/0001_two_sum
   ```

2. Copy the problem template:
   ```bash
   cp templates/problem_template.md problems/0001_two_sum/README.md
   ```

3. Create solution files:
   - `solution.py` - Python implementation
   - `solution.ts` - TypeScript implementation
   - `test_solution.py` - Python tests

4. Fill in the README with problem details and your approach

5. Implement your solution and tests

6. Run tests to verify your solution

## 📚 Problem Categories

Problems are organized by their LeetCode ID and slug. Each problem directory contains:

- **README.md**: Problem statement, examples, constraints, approach, and complexity analysis
- **solution.py**: Python implementation with type hints and docstrings
- **solution.ts**: TypeScript implementation with type annotations
- **test_solution.py**: Comprehensive test cases using pytest

## 🤝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Goals

- Practice algorithmic problem-solving
- Improve coding skills in Python and TypeScript
- Build a portfolio of solved problems
- Learn best practices for testing and documentation
- Maintain clean, readable, and well-tested code

## 📊 Progress

Track your progress and see statistics on solved problems across different difficulty levels and topics.

| Difficulty | Count |
|-----------|-------|
| Easy      | 0     |
| Medium    | 1     |
| Hard      | 0     |

## 🔗 Resources

- [LeetCode](https://leetcode.com/)
- [Python Documentation](https://docs.python.org/3/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Pytest Documentation](https://docs.pytest.org/)

## 💡 Tips

- Start with easy problems and gradually increase difficulty
- Understand the problem thoroughly before coding
- Consider multiple approaches and their trade-offs
- Write tests before implementing solutions (TDD)
- Document your thought process and approach
- Review and refactor your code
- Learn from other solutions after solving

---

Happy Coding! 🚀