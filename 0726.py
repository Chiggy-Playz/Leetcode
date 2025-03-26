# Number of atoms
# https://leetcode.com/problems/number-of-atoms/description/?envType=daily-question&envId=2024-07-14
import re


def last_is_atom(stack: str) -> bool:

    if not stack:
        return False

    if stack[-1].isnumeric():
        return False

    if stack[-1] in "()":
        return False

    return True


def multiply_by(group: str, factor: int) -> str:

    def multiply(match):
        return str(int(match.group()) * factor)

    return re.sub(r"\d+(\.\d+)?", multiply, group)


def countOfAtoms(formula: str) -> str:
    elements = {}
    i = 0
    stack = ""
    formula = f"({formula})"
    while i < len(formula):
        # Found an atom with more than one character
        # Get all characters
        a_old_stack = stack
        if formula[i] == "(":
            if last_is_atom(stack):
                stack += ":1"
            stack += "("
            i += 1
        elif formula[i].isupper():
            # For example, if O encountered after N in NO
            # Will become N:1O
            if last_is_atom(stack):
                stack += ":1"

            atom = formula[i]
            i += 1
            while i < len(formula) and formula[i].islower():
                atom += formula[i]
                i += 1

            stack += ("|" if stack[-1].isnumeric() else "") + atom
        elif formula[i].isnumeric():
            count = formula[i]
            i += 1
            while i < len(formula) and formula[i].isnumeric():
                count += formula[i]
                i += 1

            count = int(count)

            # Now, it depends what is behind the number. If behind the number is just a single atom, then we just multiply that.
            # If its a bracket, we multiply whole bracket with the number

            if stack[-1] != ")":
                j = len(stack) - 1
                atom = ""

                if stack[j].isupper():
                    atom = stack[j]
                else:
                    while True:
                        atom = stack[j] + atom
                        if stack[j].isupper():
                            break
                        j -= 1

                stack = stack[:j] + f"{atom}:{count}"
            else:
                # Crazy fuckery here
                j = len(stack) - 2
                brackets_count = 0
                while not (stack[j] == "(" and brackets_count == 0):
                    if stack[j] == ")":
                        brackets_count += 1
                    elif stack[j] == "(":
                        brackets_count -= 1

                    j -= 1

                group = stack[j:]
                multiplied_group = multiply_by(group, count)
                stack = stack[:j] + multiplied_group

        elif formula[i] == ")":
            if last_is_atom(stack):
                stack += ":1"
            stack += ")"
            i += 1

    # Just count and add all the elements now
    matches = re.finditer(r"(\w+):(\d+)", stack)
    for match in matches:
        atom = match.group(1)
        count = int(match.group(2))
        elements[atom] = elements.get(atom, 0) + count

    return "".join(
        f"{key}" + ("" if value == 1 else f"{value}") for key, value in sorted(elements.items(), key=lambda x: x[0])
    )


assert countOfAtoms("K4(ON(SO3)2)2") == "K4N2O14S4"
assert countOfAtoms("Be32") == "Be32"
assert countOfAtoms("H2O") == "H2O"
assert countOfAtoms("Mg(OH)2") == "H2MgO2"
assert countOfAtoms("(NB3)33") == "B99N33"
assert countOfAtoms("(Li12B17Be11)5") == "B85Be55Li60"
print(
    countOfAtoms(
        "(N13O9Be)37(LiC50B35)38(Li33HHBe14He5ON50N)27(H3C)2He14C34Li33C33He15N14N5Li24Li17H28O13H42(HeHe6CO11Li)35(He3O27HO5N21H49O39CH37B3)8(O41He27He46He22He17)12"
    )
)
