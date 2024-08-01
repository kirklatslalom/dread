# DREAD Risk Score Calculator

## Overview

The DREAD Risk Score Calculator is a Python-based tool for evaluating the risk
 associated with a threat by using the DREAD methodology. DREAD is an acronym
 for Damage, Reproducibility, Exploitability, Affected Users, and
 Discoverability. Each factor is scored on a scale from 0 to 10, and the script
 calculates an average score to provide a quantitative measure of the risk.

## Features

- Interactive command-line interface
- Prompts the user for scores in five categories: Damage, Reproducibility,
 Exploitability, Affected Users, and Discoverability
- Calculates and displays the average DREAD risk score
- Uses predefined scoring values to guide user input

## Installation

To run the DREAD Risk Score Calculator, you need Python installed on your
 system. You can download Python from
 [python.org](https://www.python.org/downloads/).

### Clone the Repository

Clone this repository using the following command:

```bash
git clone https://github.com/kirklatslalom/dread.git
```

### Navigate to the Project Directory

```bash
cd dread-risk-score-calculator
```

### Usage

Run the script using Python:

```bash
python dread_calculator.py
```

## Interaction

Enter a score based on the potential damage if a threat exploit occurs for each
 of the following:

1. Damage Potential
2. Reproducibility
3. Exploitability
4. Affected Users
5. Discoverability

The script will prompt you for scores in each category and then calculate the
 average DREAD risk score.

## Scoring Details

### Damage Potential

- 0: Nothing
- 5: Information disclosure that could be used in combination with other
 vulnerabilities
- 8: Non sensitive user data compromised
- 9: Administrative non sensitive data compromised
- 10: Complete system or data destruction / Application unavailability

### Reproducibility

- 0: Very hard or impossible
- 5: Complex steps required
- 7.5: Easy steps for authenticated user
- 10: Just a web browser needed

### Exploitability

- 2.5: Advanced programming and networking knowledge
- 5: Exploit exists in public
- 9: A Web Application Proxy tool
- 10: Just a web browser

### Affected Users

- 0: None
- 2.5: Individual/employer already compromised
- 6: Some users
- 8: Administrative users
- 10: All users

### Discoverability

- 0: Very hard
- 5: Can figure out by monitoring
- 8: Details are public
- 10: Visible in address bar or form

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request
 with your changes. Ensure your code adheres to the project's coding standards
 and includes appropriate tests and documentation.

## License

This project is licensed under the MIT License - see the LICENSE file for
 details.

## Contact

For questions or feedback, please open an issue on the GitHub repository.

## Acknowledgments

Inspired by the DREAD methodology for risk assessment and Haider's Infosec Blog
Python community for the robust tools and libraries
