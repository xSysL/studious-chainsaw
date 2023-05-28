
with open("Mail Merge Project Start\\Input\\Names\\invited_names.txt") as file:

    content = file.readlines()

new_content = []

for item in content:
    new_content.append(item.replace("\n", ""))
print(content, new_content)

with open("Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as file:
    text = file.read()

for name in new_content:
    with open(f"Mail Merge Project Start\\Output\\ReadyToSend\\{name}.txt", "w") as file:
        new_text = text.replace("[name]", f"{name}")
        file.write(new_text)
