# -*- coding: utf-8 -*-
def get_dread_score():
    def prompt_for_score(category, options):
        while True:
            try:
                print(f"\n{category}:")
                print("Options:")
                for option in options:
                    print(f"  {option[0]} = {option[1]}")
                score = float(
                    input(f"Enter a score for {category} ({[o[0] for o in options]}): ")
                )
                if score in dict(options).keys():
                    return score
                else:
                    print(
                        f"Invalid input. Please enter one of the following values: {[o[0] for o in options]}"
                    )
            except ValueError:
                print("Invalid input. Please enter a number.")

    damage_options = [
        (0, "Nothing"),
        (5, "Information disclosure"),
        (8, "Non sensitive user data compromised"),
        (9, "Administrative non sensitive data compromised"),
        (10, "Complete system or data destruction"),
        (10, "Application unavailability"),
    ]

    reproducibility_options = [
        (0, "Very hard or impossible"),
        (5, "Complex steps required"),
        (7.5, "Easy steps for authenticated user"),
        (10, "Just a web browser needed"),
    ]

    exploitability_options = [
        (2.5, "Advanced programming and networking knowledge"),
        (5, "Exploit exists in public"),
        (9, "A Web Application Proxy tool"),
        (10, "Just a web browser"),
    ]

    affected_users_options = [
        (0, "None"),
        (2.5, "Individual/employer already compromised"),
        (6, "Some users"),
        (8, "Administrative users"),
        (10, "All users"),
    ]

    discoverability_options = [
        (0, "Very hard"),
        (5, "Can figure out by monitoring"),
        (8, "Details are public"),
        (10, "Visible in address bar or form"),
    ]

    print("Welcome to the DREAD Risk Score Calculator!")

    damage = prompt_for_score("Damage Potential", damage_options)
    reproducibility = prompt_for_score("Reproducibility", reproducibility_options)
    exploitability = prompt_for_score("Exploitability", exploitability_options)
    affected_users = prompt_for_score("Affected Users", affected_users_options)
    discoverability = prompt_for_score("Discoverability", discoverability_options)

    dread_score = (
        damage + reproducibility + exploitability + affected_users + discoverability
    ) / 5

    print("\nDREAD Risk Score Calculation:")
    print(f"Damage Potential: {damage}")
    print(f"Reproducibility: {reproducibility}")
    print(f"Exploitability: {exploitability}")
    print(f"Affected Users: {affected_users}")
    print(f"Discoverability: {discoverability}")
    print(f"\nCalculated DREAD Risk Score: {dread_score:.2f}")


if __name__ == "__main__":
    get_dread_score()
