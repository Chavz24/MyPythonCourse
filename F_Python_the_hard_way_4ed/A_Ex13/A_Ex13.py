from sys import argv

print("write")


script, first_var, second_var = argv

print(
    f"Name {script}"
    f"\n{first_var} times {second_var}= {int(first_var)*int(second_var)}"
)
